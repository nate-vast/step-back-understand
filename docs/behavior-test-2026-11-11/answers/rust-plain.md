The borrow checker is the part of the Rust compiler that proves, before your program runs, that no reference ever points at freed memory or at data something else is changing. It does this by enforcing three rules.

## The three rules

1. **Every value has exactly one owner.** When the owner goes out of scope, the value is freed. Assigning or passing a value moves ownership, unless the type is `Copy` (integers, `bool`, `char` and similar), in which case it is copied.
2. **You can borrow a value as either any number of shared references (`&T`) or one exclusive reference (`&mut T`), never both at once.**
3. **A reference cannot outlive the value it points to.**

It helps to read `&T` as "shared" and `&mut T` as "exclusive" rather than "immutable" and "mutable". The checker is tracking who else can see the data, and mutation is only safe when nobody else can.

## What each rule looks like when you break it

**Use after move (rule 1):**

```rust
let s = String::from("hi");
let t = s;           // ownership moves to t
println!("{s}");     // error[E0382]: borrow of moved value: `s`
```

Fix it by borrowing (`let t = &s;`) or by cloning (`let t = s.clone();`) if you need two independent copies.

**Shared and exclusive at the same time (rule 2):**

```rust
let mut v = vec![1, 2, 3];
let first = &v[0];     // shared borrow starts
v.push(4);             // error[E0502]: cannot borrow `v` as mutable
println!("{first}");   // ...because the shared borrow is still used here
```

This is a real bug the checker is catching: `push` may reallocate the vector, which would leave `first` pointing at freed memory.

A borrow lasts until its last use, not until the end of the block. If you delete the `println!` line, or move it above the `push`, the code compiles.

**A reference that outlives its value (rule 3):**

```rust
fn longest(a: &str, b: &str) -> &str {   // error[E0106]: missing lifetime specifier
    if a.len() > b.len() { a } else { b }
}
```

The compiler cannot tell whether the result borrows from `a` or `b`, so it cannot check callers. You tell it with a lifetime annotation:

```rust
fn longest<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() > b.len() { a } else { b }
}
```

Lifetime annotations do not change how long anything lives. They only describe how the lifetimes relate, here "the result is valid as long as both inputs are". Most functions don't need them because the compiler infers the common cases.

## What to do when it rejects your code

Roughly in the order to try them:

- **Shorten the borrow.** Finish using the reference before you mutate, or copy the value out (`let first = v[0];`) instead of holding a reference.
- **Return or pass owned values** (`String` rather than `&str`, for example) when the data needs to outlive the function that made it.
- **Clone.** It is often cheap, and it is a fine way to get unstuck while learning.
- **Borrow smaller pieces.** Inside one function the checker knows `self.a` and `self.b` are separate, but a method call like `self.get_a()` borrows all of `self`.
- **Store indices or keys instead of references** for graphs, trees with parent links, and other structures where items point at each other.
- **Use `Rc<RefCell<T>>`, or `Arc<Mutex<T>>` across threads,** when you really need shared mutable data. These enforce the same rules at runtime instead of compile time.

The checker is conservative, so it sometimes rejects code that would have been safe. When that happens, restructuring is usually easier than arguing with it, and the error messages generally name both conflicting borrows and often suggest the fix.

If you have a specific error you're stuck on, paste the code and the message and I can walk through what the checker is seeing.
