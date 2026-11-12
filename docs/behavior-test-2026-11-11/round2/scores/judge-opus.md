pi: B > A (clear)
mcdoom: B > A (slight)
rust: A > B (slight)

# Judge notes (opus, blind)

## pi: B > A (clear)

**Why:** B gives one frame for the whole thing: Pi is a deliberate counter-design to Claude Code. It then hangs every feature and every omission on that frame, so I come away understanding why Pi is the way it is, not only what it contains. Its Codemode explanation is concrete. The demo pulls 167 Linear issues through MCP, classifies them in the sandbox and returns one summary ("156 neutral, 11 mildly frustrated") instead of 167 tool results. That makes "intermediate results stay out of context" click in a way A's abstract description ("combine their results in code") does not. A covers more facts at about the same length, but many of them are reference material a newcomer can't use yet.

- **A strength:** The most complete reference. It covers the four-package layering, the "You Said No MCP!" reasoning in three points, and Pi Durable's design in detail.
- **A weakness:** Dense, and front-loaded with specifics (RFC 9207 `iss` checks, credential keying, the `typeof tools.x` migration) before the reader has a model to put them in.
- **B strength:** A clear through-line (Claude Code frustration, then minimal core, then extensions, then MCP only once Codemode keeps context lean), plus a closing "how to think about it" that says who Pi suits.
- **B weakness:** Thinner on Pi Durable and the package architecture. It also spends a paragraph on Codemode's resemblance to Cloudflare's and Anthropic's work that the makers don't cite.

**Flags:**
- A, "Upgrade gotchas" and install commands: changelog material, padding for someone trying to understand the tool.
- A, "Context" section: the founder-surname uncertainty (Sidoti vs Daymond Hanna), the backer list and the HN point count are facts without explanation, and mostly about Earendil rather than Pi.
- A, "What 1.0 adds": largely a list (cache warming, fullscreen TUI, mid-conversation system messages) with little why. The why arrives later, in a separate section.
- B, the Emacs comparison ("it's mine") and the Cloudflare/Anthropic Code Mode paragraph drift toward other things, though both do help place Pi.
- B, the steering keys (Enter / Alt+Enter) and "four ways to run it" lean toward a feature list.

## mcdoom: B > A (slight)

**Why:** B gets the same core understanding across in about 70% of the words. Folk harmony sits on top and dub rhythm underneath, and both trace back to the family. B also has the best single explanatory image of either answer: her father's sound-system bass came "up through her bedroom floor while she listened to folk records upstairs," and the album recreates that arrangement. That one line explains the record's structure better than A's longer account of the same household. A teaches the background genres more deeply, but it spends a lot of its length on reference records.

- **A strength:** Real teaching about the source traditions. It explains what dub engineers actually did, and what mento is and how it relates to reggae ("the same family line, about sixty years apart"). It ends with a good synthesis of "what's her own."
- **A weakness:** Section 3 becomes a tour of influences (Victorialand's sparseness, Popul Vuh's *Hosianna Mantra*, Minnie Riperton, Spector, Kate Bush), which is more about other records than this one.
- **B strength:** Tight, well ordered (in short, then what it is, how it works, why it sounds this way). The bedroom-floor image explains a lot, and it ends with a practical listening route ("Dream Dub" and "Grandpa" back to back).
- **B weakness:** Shallower on the genres themselves: dub and mento each get a single sentence of definition. The "What it is" bio paragraph is a run of career facts.

**Flags:**
- A, section 3 (the Cocteau Twins/Victorialand detail, Popul Vuh, Minnie Riperton, Spector) is mostly about other artists' records.
- A, the hedging about which track holds the grandfather voice note, and about the title's meaning, costs words without adding understanding.
- B, "What it is" (release year 2022, the 2025 self-titled compilation, the Sub Pop Margo Guryan tribute, single release months) is a list of facts without explanation.
- B, "As of mid-November 2026, Pitchfork, the Guardian and Paste had not reviewed it" is padding.
- B, the Apple Music comparisons (Judee Sill, Nina Simone, Alton Ellis) are name-drops with no explanation.

## rust: A > B (slight)

**Why:** A covers what the borrow checker is, how it works and why it exists, in about 1,550 words against B's 2,400. It builds in a clean order: ownership, then shared-XOR-mutable, then lifetimes, then why safe code gets rejected, then the escape hatches. Its framing "the rule never goes away; only when it is checked changes" makes interior mutability click in one line. B is excellent and teaches more (lexical-to-NLL history, the conditional-return code, the error table), but much of the extra length goes to internals, research lineage and the roadmap. Those are worth knowing but not needed for a first understanding.

- **A strength:** Compact and well sequenced. Each rule comes with its reason (the vector reallocation example, why data races become unexpressible), and the "tools for when ownership doesn't fit" section is practical.
- **A weakness:** The conditional-return case and Polonius are described only in prose, so the best-known remaining limitation stays abstract.
- **B strength:** The richest "why" (per-function locality explained as a deliberate trade-off, `&mut` as unique), a real code example of the NLL limitation, and a useful table mapping error messages to fixes.
- **B weakness:** Length. The MIR constraint-solving steps, Stacked/Tree Borrows, RustBelt, early `@T`/`~T` pointers and the 2026 goals list push it well past what a newcomer needs.

**Flags:**
- B, "How it works inside the compiler" (collect constraints, solve, check accesses) is implementation detail that adds little for the asker.
- B, "What it does not cover: unsafe" (Stacked Borrows POPL 2020, Tree Borrows PLDI 2025, Miri flags, RustBelt) reads as research citations rather than explanation.
- B, "What's coming" (view types, place-based lifetimes) is a roadmap list about future features rather than the current checker.
- B, "Where the ideas came from" (Wadler 1990, early Rust pointer kinds) leans toward history for its own sake, though the region-vs-borrow distinction is a good point.
- A, the parenthetical about Cyclone combining regions with reference counting is a small aside about another language.
- A, "What is distinctive about it" partly repeats the lineage already given in the lifetimes section.
