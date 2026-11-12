pi answer-A: 1 1 1 2 2 2 1 1 = 11
pi answer-B: 0 1 1 2 1 2 0 1 = 8
mcdoom answer-A: 2 1 1 1 0 1 2 2 = 10
mcdoom answer-B: 2 1 1 2 0 1 2 2 = 11
rust answer-A: 1 2 1 2 0 0 1 2 = 9
rust answer-B: 1 2 1 2 0 0 1 2 = 9
CONTRADICTIONS
- mcdoom answer-A: "That reads as the best clue to the title, though she hasn't explained it directly." The key says she did explain it (Rolling Stone: the dark, rainy road image, "all the songs ended up being about that").
- mcdoom answer-A (minor): "done by hand on analogue equipment". The key says tracking was "to tape and digital both".
- mcdoom answer-B: "on this album those two parts [nylon guitar and voice] were recorded first. Everything else was added afterwards". The key says recording started by cutting live drums with Victor Axelrod.
- mcdoom answer-B (possible): "two EPs (collected on a self-titled release in 2025)". The key gives a self-titled debut EP in 2022 and With Strings in 2023. A 2025 compilation is not in the key, and the wording blurs which release was self-titled.
- pi answer-B (minor): "MCP servers put every tool description into context on every turn". The key and source say every session.
- pi answer-A (hedge, not a hard contradiction): "Reports give his surname as either Sidoti or Daymond Hanna" and "Reports call it either an acquisition or Zechner joining as a shareholder". The key states Colin Daymond Hanna and an acquisition.
- rust answer-B (misleading, by the key and general knowledge): "`'static` means 'valid for the whole program', as with string literals." This is true of `&'static T` but, given as the general meaning, it leads a reader to the misconception the Q5 key warns against (that `T: 'static` means the value lives for the whole program).
- rust answer-A (oversimplification, not strictly false): "a borrow lasts from where it is created to its last use". This ignores drop-liveness: a Drop impl extends the borrow to the drop point (the Q3 key).
- No other factual errors found in either Rust write-up. NLL dates, two-phase borrows, Stacked/Tree Borrows venues, Wadler 1990, and @T/~T history all check out. The Polonius-alpha-on-nightly (Aug 2026) claims cannot be checked from my knowledge and were not penalized.
NOTES
- pi Q1: A gets 1 for "call the model, run the tools it asks for, repeat until it stops". It has the cycle, but not that history comes from the session's active branch, and the stop condition is vague. B never describes the loop (only steering/queueing and session trees), so 0. This is the most borderline zero.
- pi Q2: both say "sandbox on the harness side" and "only the result enters context", but neither states the sandbox limits (QuickJS, no fs/network/timers). The rubric example demands those, so both get 1 by the same strict reading.
- pi Q3: neither states that `codemode` exposure is the default. A covers deferred/tool_search, Codemode-only, and "sees directly" (direct). B covers only deferred. Both get 1. A is the stronger 1.
- pi Q4: B's "MCP itself had changed" plus "the work needed to fix that was useful anyway" counts as two reasons, so 2.
- pi Q5: A gets 2 ("built for one person in a terminal" vs long-running, multi-steered; "separate package so the coding agent itself stays minimal"). B gives 1: it says what was wanted and that Durable is not a replacement, but never says why it did not fit the coding agent's scope.
- pi Q7: A gets 1. It has the HN headline, the unverified user count, and "ships features it once rejected", but no maker reply. B has nothing on reception.
- pi Q8: both say per-project mcp.json needs trust, AGENTS.md loads, there are no permission prompts, and to use a container. Neither says `.pi/extensions/` is skipped or mentions print-mode behaviour, so 1 each.
- mcdoom Q2: neither has the lyrics-first rule. A has the sung-melody-to-Wright method. B frames the parts as literally sung vocals rather than instrument parts born as sung melodies. 1 each.
- mcdoom Q3: neither mentions the Axelrod/Ticklah drums or the mix restart after her parents' comment. Each has self-recording plus multiple mics (2 of 4), so 1.
- mcdoom Q4: B gets 2. It has the father's bass through the floor "while she listened to folk records upstairs" as the folk side, plus wanting to bring listeners to Jamaican genres as the reason. A frames the folk side as the grandfather's mento and Pentangle rather than something she found on her own, so 1.
- mcdoom Q5: A gives "inheritance/ancestors" as a guess and says she never explained the title. It links to family, but it has neither the light-as-loved-ones nor the accept-you theme, so a strict 0. B has nothing.
- mcdoom Q6: both have the EPs, debut album and first on Jagjaguwar. Neither says the dub/reggae bass is what's new relative to the EPs, so 1.
- mcdoom Q7: both get 2 with Line of Best Fit 7/10, hybrid praise, Clash "natural/unified" or "storytelling", and the over-lush reservation. Explicit voice/production praise in the reception section is thin in both.
- mcdoom Q8: neither makes the prediction, but both contain the voice-and-guitar origin and the dub/harmony layers, so a reader can derive it. B states it almost directly ("arrangement grows around a performance that already works on its own"). 2 each.
- rust Q1: both say moved-from bindings are unusable at compile time. Neither covers same-bytes or why Copy excludes Drop. 1 each.
- rust Q4: both say "'a doesn't set how long anything lives... valid only while both inputs are" and that functions are checked against signatures. That is taken as the overlap region, so 2 each, though neither says "instantiated per call".
- rust Q7: A covers runtime enforcement, RefCell panics and "only when it is checked changes", but not Cell, UnsafeCell or !Sync. B covers Cell copying in/out and RefCell runtime checks, but no costs. 1 each.
- rust Q5/Q6: neither write-up covers `T: 'static` or variance at all.
