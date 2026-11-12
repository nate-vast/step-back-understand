pi answer-A: 1 1 1 2 2 2 1 1 = 11
pi answer-B: 0 1 1 2 2 2 0 1 = 9
mcdoom answer-A: 2 1 1 2 0 1 2 2 = 11
mcdoom answer-B: 2 1 1 1 0 1 2 2 = 10
rust answer-A: 1 2 1 2 0 0 1 2 = 9
rust answer-B: 1 2 1 2 0 0 2 2 = 10
CONTRADICTIONS
- mcdoom/answer-A.md: "McDoom writes on nylon-string guitar and voice, and on this album those two parts were recorded first." The key (Q3) says recording started by cutting live drums with Victor Axelrod; the songs were *written* on voice and guitar, but the voice and guitar were not tracked first.
- mcdoom/answer-A.md: "put out two EPs (collected on a self-titled release in 2025)" and mcdoom/answer-B.md: "her early releases were collected on a self-titled compilation in 2025". The key (Q6) calls the self-titled release her 2022 debut EP, followed by *With Strings* (2023). Possible conflict: neither write-up mentions a 2022 self-titled EP.
- mcdoom/answer-A.md: quotes the label as saying it "lays the harmony of folk over the rhythm of dub". The key's label-notes wording is "the harmony of one laid over the rhythm of the other". This is a paraphrase presented as a quote. The meaning matches.
- pi/answer-B.md: "Version 1.0.1 added per-project MCP config (`.pi/mcp.json`), MCP OAuth". The key says its docs describe 1.0 as released at the v1.0.0 tag, and Q8 treats `.pi/mcp.json` as a 1.0 project-trust resource. pi/answer-A.md also puts MCP OAuth in 1.0. Possible conflict about version attribution.
- rust/answer-A.md: "`'static` means 'valid for the whole program', as with string literals." This is true of `&'static` references. Read as the meaning of a `'static` bound, it is the misconception key Q5 corrects, because `T: 'static` does not mean the value lives for the whole program.
- rust/answer-B.md (own knowledge, minor): the `fn bad() -> &String { ... &s }` example fails first with "missing lifetime specifier", before the borrow checker reports a dangling reference. The concept is right, but the snippet does not show the error it describes.
- No factual errors found in rust/answer-A.md beyond the item above. Dates checked: NLL in Rust 1.31 / 2018 edition, the 2015 edition in 2019, the AST borrowck removed in 2022, Stacked Borrows POPL 2020, Tree Borrows PLDI 2025, Wadler 1990. The claims about Polonius alpha in nightly (August 2026) and the 2026 goals in A and B are past my knowledge, so I did not verify them.
NOTES
- pi Q1: A's "call the model, run the tools it asks for, repeat until it stops" gives the cycle but neither the active-branch history nor the stop condition, so 1. B never describes the loop; it mentions only steering "after the current tool call" and session trees, so 0.
- pi Q2: both have "JS orchestrating tools; only the output reaches context". Neither states the sandbox limits (no fs/network/Node). A at least says "JavaScript sandbox inside the harness" and B says only "run by the harness". Strictly both get 1. A is the stronger of the two 1s.
- pi Q3: both name only deferred and Codemode-only. Neither names direct or hidden, and neither states clearly that Codemode is the default. Both get 1.
- pi Q5: A is brief ("one person in a terminal", "stays minimal", "experimental"), but it covers what did not fit and the reason, so 2.
- pi Q7: A has a high-profile HN result (">1,000 points") and two doubts (an unverified user count and shipping features it once rejected), but no reply from the makers, so 1. B has no reception at all.
- pi Q8: both say no permission prompts, full access, and use a container (the safety half). A implies a project mcp.json needs trust; neither covers print mode, extensions skipped or AGENTS.md still loading. Both get 1.
- mcdoom Q2: B has voice and guitar, McDoom singing parts for Wright, and the link to the "sung" quality. Its "basic shape settled before anything else" is not the lyrics-first rule, so strictly 1. A lacks both the rule and the sing-for-Wright method; it only says parts are multitracked vocals. A gets 1 for having the starting point plus Wright on most instruments and her layering harmonies.
- mcdoom Q3: both have only multiple mics plus "with Wright / home studio". No Axelrod drums, no tape and digital, no mixing story. Both get 1.
- mcdoom Q4: A gives the father's bass coming through the floor while she played folk records upstairs, plus the reason of introducing listeners to Jamaican music, so 2. B has rich family and mento detail plus the "introduce people" reason, but never says where her folk side came from, so strictly 1.
- mcdoom Q5: neither explains the title or Aggie, so 0 for both.
- mcdoom Q6: both have the 2022 start, two EPs, debut LP and Jagjaguwar. Neither says the dub/reggae half is new relative to the folk EPs, so 1 for both.
- mcdoom Q8: neither discusses live sets, but both give the needed basis: songs built from voice and guitar outward that "would stand up with one guitar", with layered vocals and dub bass added on top. Both get 2.
- rust Q1: neither says the move/copy bytes are identical or explains why Copy excludes Drop. B's "never a second owner who might free it twice" comes closest. Both get 1.
- rust Q4: neither says `'a` is instantiated per call to the shorter overlap. Both state the relationship ("valid only while both inputs are") and per-function checking against the signature, so both get 2. A also says explicitly that `'a` "doesn't set how long anything lives"; B does not, which makes B's 2 borderline.
- rust Q7: B says RefCell checks at run time and panics, Cell never hands out inner references, and "all preserve the same invariant", so 2. It lacks UnsafeCell, not-Sync and overhead, so the 2 is borderline. A names the mechanisms but not the cost (runtime panics instead of compile errors), so 1.
- rust Q3: both explain NLL liveness well. Neither covers a Drop impl extending the borrow, so 1 each.
- Length was not rewarded. A's Pi and Rust write-ups are much longer but add little on the quizzed points.
