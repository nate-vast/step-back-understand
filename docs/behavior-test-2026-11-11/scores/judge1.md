pi: C > B > A (slight)
mcdoom: C > A > B (clear)
rust: A > B (clear)

# Judge 1

## 1. Pi 1.0

**Ranking:** C > B > A. The gap between C and B is slight.

**Main reason:** C is the only answer that explains the mechanisms behind the feature list. Each design choice is tied to a reason, so afterwards I can see why Pi works the way it does and not just what it has. The clearest example is the cache section. It explains that a prompt prefix is billed cheaply only if it stays identical, and that Anthropic's cache expires after five minutes. It then shows why deferred tools, appended system messages and cache warming all follow from that ("If a test suite runs for seven minutes, the cache expires..."). B has the same insight in compact form ("nearly all of them serve one goal: keep what the model sees small, cheap and under your control") and costs about half the reading. That is why the preference over B is only slight.

- **A.** Strength: complete and well organized; works as a reference (exposure modes, config paths, install commands, caveats with numbers). Weakness: mostly a list of facts. The table names the cache features without explaining why they matter, so I would know what Pi has, but not why.
- **B.** Strength: gives the best single thesis, and explains the MCP reversal well: MCP is allowed in because Codemode means it no longer costs context. Weakness: thin on what Pi is day to day (no harness definition, no extensions or sessions model). It also spends a paragraph on the Cloudflare and Ronacher history and hedges its own attribution.
- **C.** Strength: explains the "why" at every layer: Zechner's rationale, why there are no permission prompts, the cache economics, and why Durable is a separate package. Weakness: the longest answer (about 1,700 words). The reception, caveats and table partly repeat earlier sections.

**Flags**
- A: the "What 1.0 changed" table and the "Pi Durable" bullets are facts without explanation. Install commands for three platforms, release counts ("11 releases since 1.0.0") and GitHub star and npm figures are reference padding for someone trying to understand the tool.
- B: the paragraph on Cloudflare Code Mode and Ronacher's 2025 post is mostly about other things and ends in a hedge ("treat the Cloudflare link as a strong resemblance"). The paragraph saying "I did not find the maintainers' stated reason" for the fullscreen default adds little.
- C: the "What 1.0 added" table repeats material the next two sections explain properly. The Databricks benchmark bullet is a stray fact.

## 2. June McDoom, *Follow the Light*

**Ranking:** C > A > B. C is clearly ahead of A.

**Main reason:** C is organized around explanation. It shows how the songs are built, then why they sound that way, and each fact is linked to what you hear. The key example: "McDoom sings each part she wants, including the basslines... So the bass carries tunes of its own, and it sits forward in the mix the way it does on a dub record." That one link explains the album's sound. A has most of the same facts and a good track table, but presents the family, the production and the reviews as bullets and tables. It also states the "which is why the arrangements feel so melodic" link only in passing.

- **A.** Strength: the broadest coverage. It has a clear "what it is about" section (the title's meaning, the "many selves" idea) and a useful track table with a listening order. Weakness: much of it is in list form (family bullets, production bullets, a six-row review-score table), so it reads as a dossier rather than an explanation.
- **B.** Strength: short and focused on why the record sounds as it does. The point that dub treats the bass and drums as the foreground and the mixing desk as an instrument is the best explanation of the genre fusion in any of the three answers. Weakness: drifts into other people's histories and its own guesses, and is thin on the songs, the themes and the reception.
- **C.** Strength: explains the method, the origin and the meaning in a logical order, with a track table that adds listening notes rather than repeating facts. Weakness: the longest answer; the reception section and the evidence note add length for modest value.

**Flags**
- A: the review table (Written in Music "Scored 4 (scale not shown)", The 13th Floor "Unscored") is a list of facts with little meaning. The naming detail (born Alyssa, named after grandmother Joan) and the NTS influences source are padding.
- B: about the wrong things: the paragraphs on Victor Axelrod's resume (Antibalas, Dap-Kings, *Dub Side of the Moon*, the Frightnrs), Popol Vuh's 1972 instrumentation, and the Jamaican Folk Singers discography conflict. Several self-flagged inferences ("that is my inference", "That is my reading") take up space. The disclaimer "I'm working from interviews..." is fair but also adds length.
- C: "A note on the evidence" (Jeff Ziegler and Noel Summerville with no roles) is padding for the reader.

## 3. Rust's borrow checker

**Ranking:** A > B. A is clearly ahead.

**Main reason:** A explains why the rules exist and where they come from, not just what they are. It frames every `&` as a loan, so the rules hang together as one idea. Using the same `push` example as B, it goes further. It explains that the real reason is mutation changing the shape of data (not just data races), it links the rule to C++ iterator invalidation, and it shows the same rule enforced at runtime by `RefCell` and across threads by `RwLock`. It also says how the checker works (on MIR, using control flow, NLL) and why lifetimes are written like generics (Cyclone's regions). B is a clear, practical beginner tutorial and is shorter, but I would come away knowing the rules more than understanding them.

- **A.** Strength: a deep, connected explanation of what, how and why: the loan model, the reader-writer-lock analogy, the Cyclone origin, MIR and NLL, and the conservative cases with reasons. Weakness: largely skips ownership and moves (mentioned only in one sentence), which a newcomer needs. The Polonius status paragraph is current news rather than understanding.
- **B.** Strength: efficient and hands-on. It has three rules, each with a failing example and its fix, and a good ordered list of ways out, including the useful "shared" and "exclusive" reading of `&` and `&mut`. Weakness: explains little about why beyond the `push` example, and nothing about how the checker decides or where it came from.

**Flags**
- A: the Matsakis 2012 attribution and the Polonius nightly or stable status ("I could not find confirmation...") lean towards history and news rather than explanation. Both are short.
- B: the closing offer ("paste the code and the message...") is chat filler in a written explanation. Otherwise lean.
