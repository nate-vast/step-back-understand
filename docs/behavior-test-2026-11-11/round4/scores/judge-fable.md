pi: B > A (clear)
mcdoom: B > A (slight)
rust: B > A (clear)

Judged blind, reading B before A for each question, from the seat of a capable adult who does not know the subject. Nothing was checked against outside sources, so factual disagreements between answers are noted but not resolved.

## 1. Rust's borrow checker

**Preferred: B, clear.**

**Main reason.** B states the rule once, then shows that each later topic follows from it, so I finish with a model I can use on a real error. Its "think in terms of last use" passage is the best example: it says a borrow error points at three places and that the third, the later use, is what keeps the borrow alive. A covers more ground and is accurate in feel, but roughly a third of it (compiler internals, type-theory ancestry, unsafe aliasing models, the roadmap) is beyond what a newcomer needs, and it costs about twice the reading time.

**Strengths and weaknesses.**
- B: Biggest strength is the single thread from rule to consequences, including the point that the escape hatches (`RefCell`, `Mutex`, `unsafe`) move the check to a different time or place and keep the rule. Biggest weakness is that it never shows the fix for its first example; A's "move the `println!` above the `push` and it compiles" is the one thing I missed.
- A: Biggest strength is the error-pattern table (message, what it usually means, typical fix), which is directly usable. Biggest weakness is breadth: it reads as a survey of everything about the borrow checker, so the central idea arrives diluted and the "why" comes only after the internals.

**Flags.**
- A, padding: "The short version" at the end restates the opening.
- A, more about other things than the subject: Stacked Borrows, Tree Borrows, Miri flags and RustBelt; Wadler's linear types and the early `@T` / `~T` pointer kinds; view types and place-based lifetimes in "What's coming".
- A, list without explanation: the three-step "collect constraints, solve, check accesses" account and the two-phase-borrows bullet are stated, and a newcomer cannot do anything with them.
- B: the Cyclone paragraph is a small detour, though it is short and tied back to lifetimes.
- The two answers differ on Polonius status. B says an alpha is in nightly and not yet stable. A says it was turned on by default in nightly in August 2026 and names a flag to switch it off. I could not verify either.

## 2. June McDoom, *Follow the Light*

**Preferred: B, slight.**

**Main reason.** B explains cause and effect in the sound, where A mostly describes it. Two examples: an airy voice "doesn't punch through a dense mix, so the album is built around it rather than over it", and dub "puts the bass first, so a fragile vocal can drift above it without the song losing its footing". B also says up front that the writer has not heard the album, which makes me trust the rest more. The preference is only slight because A is shorter and holds the single most illuminating detail in either answer.

**Strengths and weaknesses.**
- B: Biggest strength is the three-layer frame, where the opening paragraph says which audible quality each layer produces and each section then pays that off. Biggest weakness is that the biographical "why" is thin: it mentions her father's DJ sets and misses the story A tells.
- A: Biggest strength is the childhood-home image, with her father's three sound systems sending bass up through her bedroom floor while she listened to folk records upstairs, which explains the folk-over-dub structure in one picture. Biggest weakness is that the reception and context sections are a fact sheet, and some claims are asserted without support (jazz training "helps explain the harmonic sophistication").

**Flags.**
- A, list without explanation: the full tracklist; the review roundup in "Context and reception".
- A, padding: "As of mid-November 2026, Pitchfork, the Guardian and Paste had not reviewed it"; the Margo Guryan tribute credit.
- B, padding: "Other things in the mix" is mostly hedged name-checks (jazz training "probably shows", Popol Vuh, the Kate Bush resemblance) that do not add to the three-layer explanation.
- B: the closing paragraph partly repeats the "Grandpa" point made two sections earlier.
- Neither answer drifts off the subject. The dub and mento background in both is needed to understand the record.

## 3. Pi 1.0

**Preferred: B, clear.**

**Main reason.** B opens with the design bet (a tiny stable core the model writes code against, everything else added as code) and then explains every feature and omission as a consequence of it, so the 1.0 changes make sense when they arrive. The Codemode passage is the clearest example: instead of putting every MCP tool definition in front of the model, it gets one tool for writing a short JavaScript program that calls them, which removes the context cost that kept MCP out. A holds more facts and a good "Why it is this way" section, but that section comes after long feature and changelog lists, so the reasons arrive after the things they explain.

**Strengths and weaknesses.**
- B: Biggest strength is that it reads the two headline changes as extensions of the minimal approach, not reversals of it, and it is explicit that Pi Durable is a separate thing and why. Biggest weakness is that the "Other features to know" bullets (providers, steering keys, run modes) are a list, and it is light on the four-package layering that A lays out well.
- A: Biggest strength is the three stated reasons for the MCP reversal and the package breakdown (`pi-ai`, `pi-agent-core`, `pi-tui`, `pi-coding-agent`), which show how the pieces fit. Biggest weakness is that it is a reference sheet written for someone who already uses Pi: much of the reading time goes to details a newcomer cannot use.

**Flags.**
- A, list without explanation: the "What 1.0 adds" bullets (RFC 9207 `iss` checks, per-server credentials, `pi mcp add|remove|list|login|logout`); "Upgrade gotchas"; the Pi Durable bullets on Immer-like drafts and `requestId` idempotency keys.
- A, more about other things than the subject: the "Context" section on Earendil's founders, the uncertain surname, the backers, Lefos, Hacker News points, and whether the deal was an acquisition.
- A, padding: repeated verification hedges ("not audited", "not independently verified", "check before citing it") and the note on press reports of the release date.
- B: the "Getting started" install lines are slightly outside "help me understand", though they are two sentences and end on a useful point about the intended path.
- B's disclaimer that it is drawn from posts and not from running Pi is useful and brief.
