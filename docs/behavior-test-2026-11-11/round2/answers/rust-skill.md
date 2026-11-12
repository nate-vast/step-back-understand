# Understanding Rust's borrow checker

The borrow checker is the part of the Rust compiler that proves, before your program runs, that every reference points at live data and that no data is changed while someone else is reading it. It is how Rust gets memory safety without a garbage collector. Most of its behaviour, including the errors that feel arbitrary at first, follows from one rule and one question.

## The foundation: ownership

Every value in Rust has exactly one owner, usually a variable. When the owner goes out of scope, the value is dropped and its memory freed. Assigning or passing a value moves it by default, and the old variable can no longer be used:

```rust
let a = String::from("hi");
let b = a;          // ownership moves to b
println!("{a}");    // error: a was moved
```

If you know C++, this is RAII and move semantics, both of which Rust lists among its C++ influences. The difference is that a moved-from C++ object still exists and can be touched by mistake, while Rust makes use-after-move a compile error. Single ownership is what makes freeing memory automatic and safe: exactly one place is responsible for each value, so it is freed exactly once.

Moving everything around would be unworkable, so Rust lets you *borrow*: take a reference to a value without taking ownership. The borrow checker's job is to police those references.

## The core rule: shared XOR mutable

At any point, a value can have either:

- any number of shared references (`&T`), or
- exactly one mutable reference (`&mut T`),

but never both. And every reference must be valid, meaning it cannot outlive the value it points to.

The reason for "shared XOR mutable" is that nearly every memory bug in C and C++ comes from mutation while something else holds a pointer. Push onto a vector while holding a reference to one of its elements, and the push may reallocate the buffer, leaving your reference pointing at freed memory:

```rust
let mut v = vec![1, 2, 3];
let first = &v[0];
v.push(4);              // error: cannot borrow `v` as mutable
println!("{first}");    //        because it is also borrowed as immutable
```

In C++ this compiles and is undefined behaviour (iterator invalidation). Rust rejects it because `first` (shared) and `push` (mutable) overlap. The same rule also rules out data races. A data race needs two accesses at the same time, at least one a write, with no synchronization. If a mutable reference is always exclusive, two threads cannot both hold access where one of them writes, so safe code cannot express a data race.

So `&` and `&mut` are better read as "shared" and "exclusive" than as "read-only" and "writable". Exclusivity is the guarantee; the permission to write follows from it.

## Lifetimes: how long a borrow lasts

To check overlap, the compiler needs to know how long each borrow lasts. That span is its *lifetime*. Inside a function you almost never write lifetimes; the compiler works them out.

Since 2018 the borrow checker has used **non-lexical lifetimes (NLL)**: a borrow lasts from where it is created to its last use, not to the end of the enclosing block. This compiles:

```rust
let mut s = String::from("hello");
let r1 = &s;
let r2 = &s;
println!("{r1} and {r2}");  // last use of r1, r2
let r3 = &mut s;            // fine: the shared borrows are already over
r3.push('!');
```

NLL works by running the check on the compiler's control-flow graph (MIR) rather than on the source's nesting. It asks, at each point in the program, which borrows might still be used later along some path. That is also why a borrow can be live in one `match` arm and dead in another.

Lifetimes become visible at function boundaries, because the compiler checks each function on its own and needs the signature to say how outputs relate to inputs:

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

`'a` does not set how long anything lives. It is a constraint: the returned reference is valid only while both inputs are. Callers are then checked against that promise without the compiler looking inside `longest`. Most signatures need no annotations, thanks to *elision rules*: with a single reference input, the output borrows from it; with `&self`, the output borrows from `self`.

The idea of tagging each pointer with the region of memory it points into, and checking that the region outlives every use of the pointer, comes from region-based memory management; Rust names the research languages ML Kit and Cyclone as its sources here. Cyclone, a safe dialect of C, wrote the region into pointer types and rejected dangling dereferences at compile time. Rust's lifetimes are the same idea, inferred within function bodies and written only in signatures.

## Why it rejects code that looks fine

The borrow checker is conservative. It must reject every unsafe program, so it also rejects some safe ones it cannot prove safe. A few patterns account for most of the friction:

- **Methods borrow the whole struct.** Inside one function, `&mut s.a` and `&mut s.b` can coexist because the compiler can see the fields are disjoint. A method taking `&mut self` borrows all of `self`, because the checker trusts the signature and does not look inside the method. The usual fix is to borrow the fields directly or split the struct.
- **Conditional returns of a borrow.** The classic case is "look up a key; if found, return a reference to it; otherwise insert and return that." NLL treats the first lookup's borrow as live for the rest of the function, because it might be returned, so the insert is rejected even on the path where nothing was returned.
- **Self-referential structs and graphs with back-pointers** don't fit single ownership plus scoped borrows at all.

Some exceptions are built in where the rule would be needlessly strict. `v.push(v.len())` compiles because of *two-phase borrows*: the mutable borrow for `push` is only reserved while the argument `v.len()` is evaluated, and becomes an active, exclusive borrow when the call itself starts.

The conditional-return case is what the next-generation checker, **Polonius**, is for. Polonius tracks borrows by where they flow, not only by where they are live, so it sees that the borrow is dead on the insert path. The Rust team turned "Polonius Alpha" on by default in nightly in August 2026, with stable Rust still on NLL, and said it was aiming to stabilize before the end of the year. Even so, it does not accept everything, and some linked-list cursor patterns are still rejected.

## Tools for when ownership doesn't fit

When the static rules can't express what you need, Rust gives you types that move the check or change the ownership model:

- **`Rc<T>` / `Arc<T>`**: shared ownership with reference counting, for data with several owners. (Cyclone combined regions with unique pointers and reference counting in a similar way.)
- **`RefCell<T>` / `Mutex<T>` / `RwLock<T>`**: *interior mutability*. They enforce the same shared-XOR-mutable rule at run time instead of compile time, panicking (`RefCell`) or blocking (`Mutex`) when it would be violated. The rule never goes away; only when it is checked changes.
- **Indices or handles instead of references**: store items in a `Vec` and refer to them by index. This is the standard way to build graphs and trees with back-links, because an index is a plain number and borrows nothing.
- **Cloning**: often the simplest fix when the data is small.
- **`unsafe`**: lets you dereference raw pointers that the checker ignores. You take on the proof yourself, and the standard library uses it to build the safe types above.

## Working with it

- Read errors as "these two borrows overlap." The compiler points at the borrow's creation, the conflicting use, and the later use that keeps the first borrow alive. Usually the fix is to end the first borrow sooner: copy out the value you need, reorder statements, or limit the borrow to a smaller block.
- Prefer owned data in structs (`String` rather than `&str`) until you have a reason to borrow. Structs that hold references carry lifetime parameters through every use.
- Design for one clear owner per piece of data. Code that fights the checker is often trying to have several parts of a program mutate the same thing. That design is fragile in any language, and Rust just makes you say how it is coordinated.

## What is distinctive about it

None of its ingredients is new: moves from C++, regions from ML Kit and Cyclone, uniqueness from linear-type research. What Rust added is putting them together in a mainstream language: one aliasing rule, inferred inside functions and declared only at the boundaries, with a precision (NLL, two-phase borrows, and soon Polonius) that keeps rising so ordinary code passes without annotations.

## References

- The Rust Book, "References and Borrowing": https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html
- RFC 2094, Non-lexical lifetimes: https://rust-lang.github.io/rfcs/2094-nll.html
- Rust Blog, "Enabling the next iteration of the borrow checker on nightly" (Aug 2026): https://blog.rust-lang.org/2026/08/04/enabling-polonius-alpha-on-nightly
- rustc dev guide, "Two-phase borrows": https://rustc-dev-guide.rust-lang.org/borrow-check/two-phase-borrows.html
- The Rust Reference, "Influences": https://doc.rust-lang.org/reference/influences.html
- Grossman et al., "Region-Based Memory Management in Cyclone" (PLDI 2002): https://www.cs.umd.edu/~mwh/papers/cyclone_regions_tr.pdf
