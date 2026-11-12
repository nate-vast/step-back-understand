pi: B > A (clear)
mcdoom: A > B (slight)
rust: B > A (clear)

Judge: opus (blind). Read A before B for each question. Word counts: pi A 1953 / B 1484; mcdoom A 1157 / B 1450; rust A 2411 / B 1464.

## pi: B > A (clear)

**Main reason.** B opens with a thesis ("a tiny, stable core that it writes code against, and let everything else be code that you or the agent adds") and then shows each feature following from it, including the 1.0 changes, which it presents as "ways to add capability without growing the core" rather than as reversals. A carries more facts but reads like release notes plus a dossier. B also explains terms a newcomer needs: it defines MCP ("the standard for connecting agents to external tool servers") and describes Codemode as "one tool for writing a short JavaScript program... that calls the MCP tools." A uses MCP for paragraphs before ever saying what it is. B costs about 25% less reading time and leaves me understanding more.

- **A strength:** the "Why it is this way" section is real explanation, especially the MCP refusal and its reversal told as one story with the three stated reasons.
- **A weakness:** too much reference material for someone learning the subject (upgrade gotchas, OAuth RFC 9207, CLI subcommands, token counts), and MCP is never defined.
- **B strength:** a single organising idea that every section returns to, and jargon explained in plain words.
- **B weakness:** Pi Durable gets a fairly thin treatment, and the opening sentence is abstract until the core section makes it concrete.

**Flags.**
- A, padding / facts without explanation: the "Upgrade gotchas" list (`typeof tools.x` vs `"x" in tools`, credential keying), the OAuth hardening details, both install commands, the "~5,300 to ~3,300 tokens" example, the 1.0 feature list (cache warming, fullscreen TUI, given without a why).
- A, about other things than the subject: most of "Context". It covers Earendil's co-founder's disputed surname, investors, whether the deal was an acquisition, and Lefos. None of it helps me understand Pi.
- B, minor: the "Four ways to run it" and "Steering" bullets list features without explaining them, and the 1.0.1 changelog items (Nix flake) are filler.

## mcdoom: A > B (slight)

**Main reason.** Both answers give the same core picture: folk on top, Jamaican low end beneath, with mento as the root that makes the two fit. A gets there in about 300 fewer words and has the single best explanatory image: the father's sound-system bass "came up through her bedroom floor while she listened to folk records upstairs," which the album "recreates." B's three-layer framework is clearer as a structure, and it has a sharper insight that A only hints at: the bass and counter-lines start as sung parts. But B then spends space on hedged extras. On balance A is the better trade of understanding for time.

- **A strength:** tight cause-and-effect ("built from the voice outward", then the childhood house, then the grandfather), and it ends with a concrete way to listen.
- **A weakness:** the tracklist and the early biography paragraph are bare facts, and its explanation of how the voice shapes the arrangement is thinner than B's.
- **B strength:** the three-layer framework, and the best explanation of the vocal-first arrangement (Bacharach framing a light voice, the problem a soft voice poses).
- **B weakness:** longer, it leaves out the bedroom-floor origin story, and it pads the back half with speculative "other things."

**Flags.**
- A, list of facts: the full tracklist in "What it is"; the list of review outlets that had *not* reviewed it.
- B, padding / about other things: the "Other things in the mix" section (Popol Vuh, the Kate Bush resemblance B itself says to treat as only a resemblance, "jazz training probably shows... though she hasn't spelled out how"); the Cocteau Twins album-by-album asides (*Milk & Kisses*, *Victorialand*).
- B, minor: the "(I haven't heard the album)" caveat is honest but adds nothing for the reader.

## rust: B > A (clear)

**Main reason.** B gives the same core understanding as A in about 60% of the words: the rule, why aliasing plus mutation is the danger, lifetimes, NLL, and what it still rejects. Every section ties back to its opening claim that "the rule itself, and checking it locally at compile time" explain most of what feels strange. The escape-hatches section is the clearest example: Rc, RefCell and the others are "tools that *move the check* rather than abandon it," which helps a newcomer understand them instead of just listing them. A is excellent and more complete, but it reads like a reference chapter. Compiler internals, the type-theory family tree, early `@T`/`~T` pointers, Stacked and Tree Borrows, and the 2026 roadmap are far more than someone trying to understand the checker needs.

- **A strength:** the depth is accurate and well explained. Calling `&mut` "unique" rather than "mutable", and the explanation of why NLL rejects problem case #3 (flow-insensitive constraints), are both very good. The error-pattern table is useful in practice.
- **A weakness:** length. Roughly a third of it is history, internals and roadmap that a learner doesn't need on a first read.
- **B strength:** the one-rule framing holds the whole piece together, it puts ownership before borrowing, and its advice to "think in terms of last use" when reading errors is practical.
- **B weakness:** small technical slip. `fn bad() -> &String` fails first with "missing lifetime specifier", not with the dangling-reference error the text describes. It also never shows the conditional-return code it discusses.

**Flags.**
- A, about other things than the subject: "Where the ideas came from" (Wadler 1990, affine types, ML Kit, early `@T`/`~T`), the Stacked Borrows / Tree Borrows / RustBelt / Miri paragraph, and "What's coming" (view types, place-based lifetimes). These are interesting, but they are context, not the borrow checker.
- A, list of facts: the version-history bullets (Rust 1.31, "came to 2015 edition in 2019, old checker removed in 2022"), and the Polonius nightly/`-Zpolonius=off` details.
- A, mild padding: "The short version" at the end repeats the opening.
- B: little padding. The "References" list and the Polonius status paragraph are about the right length.
