# Understanding Rust's borrow checker

## What it is

The borrow checker is the part of the Rust compiler that checks how references are used. Before your program runs, it proves two things:

1. **No reference outlives the data it points to.** You can't get a dangling pointer or use something after it's freed.
2. **No data is both shared and mutated at the same time.** At any point a value can have either any number of read-only references (`&T`) or exactly one mutable reference (`&mut T`), never both.

If the compiler can't prove both, it rejects the program. All of this happens at compile time, so the program carries no runtime cost from it: no garbage collector, no reference counts, no lock checks.

One distinction clears up a lot of confusion. **Ownership** and **borrowing** are related but separate mechanisms:

- **Ownership** says every value has one owner and is dropped (freed) when the owner goes out of scope. Assigning or passing a non-`Copy` value *moves* it, and the old name becomes unusable.
- **Borrowing** lets you use a value through a reference without taking ownership. The borrow checker is the analysis that polices borrows.

## The rules in practice

```rust
let mut v = vec![1, 2, 3];

let first = &v[0];      // shared borrow of v starts
v.push(4);              // ERROR: needs &mut v while `first` is still in use
println!("{first}");    // ...because `first` is used here
```

This isn't pedantry. `push` may reallocate the vector's buffer, which would leave `first` pointing at freed memory. In C++ this is the well-known iterator-invalidation bug. In Rust it doesn't compile.

Move the `println!` above the `push` and the program compiles. The borrow `first` is no longer used after the print, so it has ended before the mutation.

The checker reasons in terms of **loans** and **lifetimes**:

- Writing `&v` or `&mut v` creates a *loan* of `v`, which is either shared or mutable.
- Each reference has a *lifetime*: the region of the program during which it may be used. In the compiler and in newer writing this is often called an *origin*.
- While a loan is live, any action on `v` that conflicts with it is an error. Mutating, moving or dropping `v` conflicts with a shared loan. Any access at all to `v` except through the reference conflicts with a mutable loan.

### Lifetime annotations

Inside a function body the compiler infers everything. At function boundaries it needs a signature to work from, since it checks each function on its own and never looks inside the functions it calls:

```rust
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

`'a` doesn't set how long anything lives. It's a constraint: the returned reference is valid only while both inputs are. Callers are checked against that contract. Most signatures need no annotation thanks to *lifetime elision* rules (for example, a single input reference, or `&self` on a method, supplies the output lifetime).

Lifetimes also appear in types: `struct Parser<'a> { input: &'a str }` says a `Parser` can't outlive the string it borrows. `'static` means "valid for the whole program", as with string literals.

### Reborrowing and splitting

- **Reborrowing.** Passing `&mut *r`, or passing `r` where a `&mut` is expected, creates a shorter-lived borrow derived from `r`. While the reborrow is live, `r` itself is frozen. When it ends, `r` is usable again.
- **Field splitting.** Within one function, the checker tracks *places* (paths like `self.a` and `self.b`), not just whole variables. So `let a = &mut s.a; let b = &mut s.b;` is fine. What it can't do is see across a function call: a method taking `&mut self` borrows *all* of `self`, which is the source of the familiar "can't call this method while a field is borrowed" error.
- **Two-phase borrows.** `v.push(v.len())` compiles even though `push` takes `&mut v` and `v.len()` reads `v`. For such autoref method calls the compiler reserves the mutable borrow first and activates it only after the arguments have been evaluated.

## How it works inside the compiler

The modern borrow checker runs on **MIR** (Mid-level Intermediate Representation), a simplified control-flow graph of each function in which every `if`, `match`, loop and `?` is an explicit edge between basic blocks. Roughly:

1. **Collect constraints.** Each reference type gets a lifetime variable. Subtyping and assignments produce *outlives* constraints (`'a: 'b`, meaning `'a` must last at least as long as `'b`). *Liveness* adds the rule that if a reference may be used later, its lifetime must include the current point.
2. **Solve.** The compiler computes the smallest set of program points each lifetime must cover that satisfies every constraint.
3. **Check accesses.** At every point it computes which loans are in scope, then checks each read, write, move and drop against those loans.

Because lifetimes are sets of points in the control-flow graph rather than blocks of source text, this design is called **non-lexical lifetimes (NLL)**.

## Why it is this way

### The core idea: aliasing XOR mutation

Most memory-safety bugs and all data races need two ingredients at once: **aliasing** (two paths to the same memory) and **mutation** (one of them writes). Use-after-free, iterator invalidation and data races are all versions of "someone changed or freed this while someone else was looking at it." Garbage-collected languages remove the "freed" half and leave the races. Rust's bet was to forbid the combination itself, statically.

That's why `&mut` is better understood as **unique** than as "mutable". The Rust team argued this openly in 2014, in Niko Matsakis's "Focusing on ownership" and the debate around it. The proposal to rename `&mut` to something like `&uniq` was dropped, but the reading stuck. Two consequences follow:

- **Thread safety falls out of the same rule.** A `&mut T` can't coexist with any other reference, so two threads can't race on it. Together with the `Send` and `Sync` traits, this is how Rust rules out data races at compile time ("fearless concurrency").
- **Shared mutation is opt-in and explicit.** When you really need it, *interior mutability* types (`Cell`, `RefCell`, `Mutex`, atomics) give mutation through `&T`. Each one restores safety its own way: copying values in and out, checking borrows at runtime, or locking.

### Why compile time, and why so strict

Rust was meant for systems programming, where C and C++ live: no garbage collector, predictable performance, direct control of memory layout. That rules out runtime tracing. Ownership gives deterministic cleanup (in the same family as C++'s RAII), and the borrow checker lets cheap, plain-pointer references coexist with that cleanup safely.

The checker is deliberately **conservative**. Any static analysis must either reject some correct programs or accept some wrong ones, and Rust always chooses to reject. The other key design choice is that checking is **local to each function**: a function is checked against its signature, never its callers' or callees' bodies. That keeps compile times reasonable, makes errors point at one place, and means changing a function's body can't break code elsewhere as long as the signature holds. The cost is the field-borrow problem above: the signature `&mut self` is all a caller sees.

### Where the ideas came from

- **Region-based memory (Cyclone, the ML Kit).** Rust's lifetimes descend from *regions* in research languages, especially Cyclone, a safe dialect of C. Cyclone tied pointers to named, scoped regions of memory and statically stopped you from dereferencing a pointer after its region was freed. Rust's reference cites Cyclone as an influence for this. The difference is that a Rust lifetime describes how long a **borrow** may be used, not where memory was **allocated**, which is why lifetimes in Rust are pure compile-time constraints with no allocation meaning.
- **Linear, affine and uniqueness types.** Rust's "a value is moved and can't be used again" rule is an *affine* type discipline (use at most once). It descends from work on linear types such as Wadler's 1990 "Linear types can change the world!" and on uniqueness types. Unique ownership makes it safe to mutate or free in place, since nobody else can observe it. Borrowing is the escape hatch that lets you use a value temporarily without giving up ownership. Pure linear typing without it would be unbearably restrictive.
- **Early Rust.** The first Rust versions (around 2010–2012) had several pointer kinds, including garbage-collected `@T` and owned `~T`, and a weaker alias analysis. Over 2012–2014 the language converged on today's design: owned values, `Box`, and the two reference types `&T` and `&mut T`, with the borrow checker carrying the safety argument. The garbage-collected pointer was removed from the language entirely.

## A brief history of the checker itself

- **Lexical lifetimes (Rust 1.0, 2015).** A borrow lasted until the end of the enclosing block (`{ ... }`), even if the reference was never used again. The `v.push` example above was rejected even after moving the `println!`, and people added artificial blocks to end borrows early.
- **Non-lexical lifetimes (RFC 2094; Rust 2018 edition, Rust 1.31).** The checker moved to MIR, and borrows ended at their last use. Most of the old "fighting the borrow checker" cases went away. NLL came to the 2015 edition in 2019, and the old checker was removed in 2022.
- **What NLL still rejects.** The famous leftover is a *conditional return of a borrow* (problem case #3 in the NLL RFC):

  ```rust
  fn get_or_default<'r>(map: &'r mut HashMap<K, V>, key: K) -> &'r mut V {
      match map.get_mut(&key) {
          Some(v) => v,                       // borrow returned to caller
          None => {
              map.insert(key.clone(), V::default()); // NLL: ERROR, map still borrowed
              map.get_mut(&key).unwrap()
          }
      }
  }
  ```

  This is safe: in the `None` branch the first borrow is dead. But NLL's lifetime constraints are *flow-insensitive*. Since the borrow may be returned, its lifetime must last to the end of the function on every path. The usual workaround is to look the key up twice, or to use the `entry` API.

- **Polonius.** Polonius is the next-generation formulation. It asks "which loans could flow into this reference at this point?" and tracks that per program point, so it can see that the loan doesn't reach the `None` branch. An early Datalog-based prototype was too slow for production. A 2023 reformulation built on NLL's infrastructure, called **Polonius alpha**, was turned on by default in nightly Rust in August 2026. The team's stated plan is to stabilize it before the end of 2026. It accepts the conditional-return case and related patterns such as some lending iterators. Its main cost is extra compile time on borrow-heavy crates. On nightly, `-Zpolonius=off` switches back to NLL.

## What it does not cover: `unsafe`

The borrow checker only checks safe code. Inside `unsafe` blocks you can use raw pointers (`*const T`, `*mut T`), which it doesn't track. This is how `Vec`, `RefCell` and the rest of the standard library are built. The contract is that `unsafe` code must uphold the same aliasing guarantees the checker assumes, because the optimizer relies on them (for example, assuming a `&mut T` aliases nothing).

What exactly those rules are for unsafe code is still not formally settled. Two research models, **Stacked Borrows** (POPL 2020) and its successor **Tree Borrows** (PLDI 2025), define them precisely. You can test your unsafe code against them with the **Miri** interpreter (`cargo +nightly miri test`; Tree Borrows is enabled with `-Zmiri-tree-borrows`). In a separate line of work, the RustBelt project has formally proved the soundness of the core type system and of key standard-library abstractions.

## Working with it, not against it

When the checker says no, it's usually pointing at one of a few real situations:

| Error pattern | Usually means | Typical fix |
|---|---|---|
| "cannot borrow as mutable because it is also borrowed as immutable" | A reference is still used after a mutation | Finish using the reference first, re-fetch it after, or use indices |
| "borrowed value does not live long enough" | A reference escapes the scope of its data | Return an owned value (`String`, `Vec`), or move the data to a longer-lived owner |
| Can't call a `&mut self` method while a field is borrowed | Function boundaries borrow the whole struct | Split the struct, borrow the fields directly, or write a free function taking only the fields it needs |
| Self-referential struct won't compile | Rust can't yet express a struct holding references into itself | Store indices or offsets, use `Rc`/arena allocation, or a crate built for this |
| Graph or cyclic structures | Shared ownership with mutation | `Rc<RefCell<T>>` / `Arc<Mutex<T>>`, or arenas with indices |
| Conditional borrow return (map lookup then insert) | A known NLL limitation | The `entry` API, a double lookup, or Polonius once stable |

Some habits that help:

- Prefer owned data in structs. Put lifetimes on types only for short-lived views like parsers and iterators.
- Clone small things when it keeps the design simple. It's often cheaper than you think.
- Treat `&mut` as "exclusive access". Asking "who else could be looking at this?" usually explains the error.

## What's coming

The Rust project's 2026 goals, grouped as "The Borrow Checker Within", aim to make the checker accept more correct code without weakening its guarantees:

- **Polonius alpha:** stabilize it and write a formal model of it.
- **View types:** let a method say which fields of `self` it borrows, which fixes the field-borrow problem across function boundaries.
- **Longer term:**
  - full Polonius, for cases the alpha still rejects, such as some linked-list traversals;
  - **place-based lifetimes**, which would let you write something like `'self.text` instead of an abstract `'a`;
  - support for self-referential (internal-reference) structs.

## The short version

The borrow checker enforces one idea: **a value may be aliased or mutated, but never both at once, and no reference may outlive what it points to.** That idea comes from research on regions and linear types. Rust makes it practical through an analysis that runs on each function's control-flow graph and needs annotations only at function boundaries, and the analysis has been getting steadily less conservative, from lexical scopes to NLL and now to Polonius. It gives memory safety and freedom from data races with no runtime cost. The price is that you have to make ownership and sharing explicit, and sometimes restructure code that's correct but that the checker can't yet prove correct.
