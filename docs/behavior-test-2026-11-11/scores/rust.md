WRITEUPS
answer-A: 1 2 1 2 0 0 1 2 = 9
answer-B: 1 2 1 1 0 0 1 1 = 7
ERRORS
- No clear factual errors in either write-up. Minor imprecisions only:
- A: "Niko Matsakis, who designed most of the borrow checker" is an overstatement. He was the main designer of the model and of NLL, but many people built the checker.
- A: "Polonius Alpha ... was enabled on nightly in August 2026 with the team aiming to stabilize by the end of the year". This is after my knowledge cutoff and I cannot check it. The write-up itself says stabilization is unconfirmed.
- A: "Cyclone's regions ... allowed any number of mutable pointers into the same data" oversimplifies. Cyclone also had unique pointers. The contrast it draws is still fair.
- B: "The compiler cannot tell whether the result borrows from `a` or `b`" suggests the compiler would otherwise read the body. In fact, lifetime elision looks only at the signature, by design. This is misleading by omission rather than false. Also, the E0106 example is labeled as breaking "a reference that outlives its value" (rule 3), but E0106 is a missing-annotation error, not an outlives error.
- B: "`Arc<Mutex<T>>` ... enforce the same rules at runtime" is loose. A `Mutex` gives only exclusive access, not shared-reader access. `RwLock` is the one that mirrors shared XOR mutable.
NOTES
- q1: Neither write-up mentions `Drop`, double free or bitwise copies, so neither can earn 2. B shows the move/Copy distinction and the E0382 use-after-move error. A says only that the checker verifies "a value is not used after it has been moved". Both get 1 for the first key point (a move makes the source unusable at compile time). A's 1 is generous.
- q2: A clearly gets 2 (Vec reallocation, the enum variant and map-entry cases, an explicit "not just data races"). B gets 2 more narrowly: it has the Vec reallocation example with a single thread and freed memory, but no explicit contrast with data races and no enum case.
- q3: Both explain that a borrow ends at its last use rather than at the end of scope. A also mentions the control-flow graph and the set of points where the reference may still be used. Neither covers `Drop` making the end-of-scope drop a use, so both get 1.
- q4: A gets 2. It says annotations never make anything live longer, that "a function is generic over the regions its arguments come from" (the lifetime is filled in at each call), and that "each function is checked on its own, against the signatures". B gets 1. It has "do not change how long anything lives" and "valid as long as both inputs are", but its reason the signature is needed is "cannot tell ... so it cannot check callers". That frames it as the compiler being unable to work it out from the body, not as a deliberate per-function contract.
- q5 and q6: Neither write-up mentions `T: 'static`, `&'static T` or variance.
- q7: A says `RefCell` enforces the rule at runtime and panics on a violation. B says only that `Rc<RefCell<T>>` enforces the rules at runtime. Neither mentions `Cell`, `UnsafeCell`, `Sync` or the runtime overhead, so both get 1. A is the stronger of the two 1s.
- q8: A gets 2, which is borderline. It says a `&mut self` method "locks every field" and to "borrow fields separately instead of going through a method" (disjoint field borrows). The principle (each function is checked on its own against signatures) appears in a different section, so the reader has to connect the two. B gets 1. It states the field-vs-method behavior clearly but gives no reason for it.
