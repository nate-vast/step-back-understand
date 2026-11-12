# Rust's borrow checker

The borrow checker is a compile-time pass that proves two things about every reference in your program: it never outlives the data it points to, and nobody changes that data while someone else is looking at it. It has no runtime cost and leaves nothing in the compiled binary. If it cannot prove both, the program does not compile.

## The model: every `&` is a loan

Writing `&x` or `&mut x` takes out a loan on `x`. The loan lasts as long as the resulting reference might still be used. While it is live, some things you would otherwise be allowed to do with `x` are forbidden. An error means you did one of them.

```rust
let mut v = vec![1, 2, 3];
let first = &v[0];     // shared loan on v starts
v.push(4);             // error[E0502]: cannot borrow `v` as mutable
println!("{first}");   // ...because the loan is still needed here
```

This is a real bug, not pedantry. `push` may move the vector's buffer to a bigger allocation, which would leave `first` pointing at freed memory. C++ compiles the equivalent code and calls it iterator invalidation.

Delete the last line and the program compiles. That shows the second half of the model: a loan ends at the reference's last use, not at the closing brace.

## Rule 1: shared or mutable, never both

At any moment a value can have any number of `&T` references or exactly one `&mut T`. So `&mut` really means "exclusive", and `&` means "shared".

The usual explanation is data races, but the example above has one thread. The deeper reason is that mutation can change the shape of data (grow a vector, replace an enum variant, remove a map entry) and any other pointer into it then points at garbage. Niko Matsakis, who designed most of the borrow checker, proposed in 2012 that `&mut` be the only way to mutate what it points at, for exactly this reason.

It helps to think of it as a reader-writer lock that is checked at compile time and then erased. Rust's standard library uses the same rule in two other places: `RefCell` enforces it at runtime and panics on a violation, and `RwLock` enforces it across threads. When the compiler cannot see that your code is safe, those are the same rule at a later checkpoint.

The exclusivity also pays for itself in speed: because a `&mut` cannot be aliased, the compiler can keep values in registers and reorder memory operations that a C compiler has to leave alone.

## Rule 2: references cannot outlive their data

Returning a reference to a local variable is rejected, because the local is freed when the function returns.

Lifetimes (`'a`) are how the checker tracks this. A lifetime is not a duration you assign. It is a name for the stretch of code where a reference is valid, and annotations never make anything live longer. Rust took this from region-based memory management in the research language Cyclone, where every pointer type carries the name of the region it points into. That is why `'a` is written like a generic type parameter: a function is generic over the regions its arguments come from.

It also explains when you have to write one. Each function is checked on its own, against the signatures of what it calls, so the signature must say how the returned reference relates to the inputs:

```rust
fn longest<'a>(a: &'a str, b: &'a str) -> &'a str
```

This reads: the result is valid only while both `a` and `b` are. When there is only one possible answer, the compiler fills it in and you write nothing.

What Rust added is the combination. Cyclone's regions stopped dangling pointers but allowed any number of mutable pointers into the same data. Rust ties Rule 1 and Rule 2 together in one analysis.

## How it decides

The checker runs on MIR, the compiler's simplified control-flow graph, not on your source text. For each loan it computes the set of points in that graph where the reference may still be used, then walks every statement looking for a conflicting access at one of those points. It also checks that variables are initialized before use and that a value is not used after it has been moved.

The original checker used lexical scopes, so loans lasted until the closing brace. The control-flow version ("non-lexical lifetimes", shipped in 2018) is why the example above compiles once the `println!` is gone.

## Where it rejects correct code

The checker is conservative. If it cannot prove safety, it refuses, so some valid programs fail:

- **Conditional returns.** "Look up a key; if found, return the reference, otherwise insert and return" is rejected on stable Rust, because the returned loan is treated as live on the branch that does not return it. The next version of the checker, Polonius Alpha, accepts it. It was enabled on nightly in August 2026 with the team aiming to stabilize by the end of the year. I could not find confirmation that it has reached a stable release.
- **Methods borrow the whole struct.** Calling `self.foo()` with `&mut self` locks every field, even if `foo` touches one.
- **Cycles and self-references.** A struct that points into itself, or a graph with back-pointers, has no single owner for the loans to hang from.

The usual fixes, roughly in order: end the borrow sooner, copy or clone the small thing you needed, borrow fields separately instead of going through a method, store indices instead of references, and finally `Rc<RefCell<T>>`, which moves the same rule to runtime.

## Sources

- [The Rust Book: References and Borrowing](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)
- [Rustc Dev Guide: the borrow checker](https://rustc-dev-guide.rust-lang.org/borrow-check.html)
- [RFC 2094: Non-lexical lifetimes](https://rust-lang.github.io/rfcs/2094-nll.html)
- [Rust Reference: Influences](https://doc.rust-lang.org/reference/influences.html) and [Cyclone for C Programmers](https://cyclone.thelanguage.org/wiki/Cyclone%20for%20C%20Programmers/)
- [Niko Matsakis, "Imagine never hearing the phrase 'aliasable, mutable' again" (2012)](https://smallcultfollowing.com/babysteps/blog/2012/11/18/imagine-never-hearing-the-phrase-aliasable/)
- [Rustonomicon: Aliasing](https://doc.rust-lang.org/nomicon/aliasing.html) and [`std::cell`](https://doc.rust-lang.org/std/cell/index.html)
- [Rust Blog: Enabling the next iteration of the borrow checker on nightly (Aug 2026)](https://blog.rust-lang.org/2026/08/04/enabling-polonius-alpha-on-nightly/)
