pi: C > B > A (clear)
mcdoom: C > A > B (slight)
rust: A > B (slight)

# Judge 2: blind ranking notes

## pi: C > B > A (clear)

**Main reason.** C explains the reasoning behind each feature, not just what it does. It is the only answer that makes the cache features make sense: it explains that providers bill a cached prefix cheaply "but only if that prefix is identical", so adding a tool at the top "changes the prefix and forces the whole conversation to be reprocessed". After that, deferred loading, mid-conversation system messages and cache warming read as one idea rather than three features. B has the same unifying idea ("keep what the model sees small, cheap and under your control") but mostly states it rather than showing how it works. A is closer to a reference sheet.

- **C.** Strength: a clear "why it is built this way" section (Claude Code as a "spaceship", permission prompts as "security theater", models already trained to act as agents) and a real explanation of the caching mechanism. Weakness: the longest of the three. The "What 1.0 added" table repeats material that the following sections cover again.
- **B.** Strength: the tightest of the three. Its opening thesis organises every feature, and it is honest about what it could not find, such as the reason for making fullscreen the default. Weakness: the Cloudflare/Ronacher lineage paragraph is about other things more than about Pi, and the cache section asserts that the prompt cache "survives" without explaining why that matters.
- **A.** Strength: the most practical. It gives install commands, config paths, exposure modes and a good "what to know before relying on it" list of caveats, including an outside measurement that found Codemode silently dropped items. Weakness: it is mostly lists of facts with little explanation of why Pi is minimal or why the cache features exist.

**Flags.**
- A: the "What Pi is" bullets (Origin, Owner, libGDX, Flask) are a fact list. The Windows/npm install block, the `mcp.json` paths and `--no-mcp` are reference detail rather than understanding. The Pi Durable section is a run of bullets.
- B: the Cloudflare Code Mode history paragraph drifts away from the subject.
- C: the table and the prose sections overlap. The single-source figures in the Reception section lean toward a list.

## mcdoom: C > A > B (slight)

**Main reason.** C connects how the album was made to what it sounds like. Its line "The method explains most of what you hear" is followed by the explanation: because McDoom sings every part, bassline included, "the bass carries tunes of its own, and it sits forward in the mix the way it does on a dub record." A covers almost the same ground and adds more biography and a reception table, but more of it is facts in sequence than cause and effect. B is the thinnest on the album itself and spends its space on side figures.

- **C.** Strength: the clearest account of how the album works (sung parts, drums from Ticklah, minimal-versus-lavish contrast) and why it sounds that way (the father's sound systems coming through the floor, the mento grandfather). The track table is informative. Weakness: the "A note on the evidence" section and a long source list add length for little gain to understanding.
- **A.** Strength: the most complete picture: background, themes (the FLOOD quote about the title, "Future You is an ancestor"), track table, reception table and a useful "where to start". Weakness: list-heavy. The reference-points sentence (Warwick, Riperton, Pentangle, Victorialand, Popol Vuh) is name-dropping with no explanation, and the reception table repeats praise without adding understanding.
- **B.** Strength: good explanation of why folk sits on top of dub ("the mixing desk is played like an instrument"), and it is clear about which statements are its own inference. Weakness: no track overview, and large parts are about other people and records rather than this album.

**Flags.**
- B: the Victor Axelrod CV (Antibalas, Dap-Kings, *Dub Side of the Moon*, the Frightnrs), the Popol Vuh album description and the Jamaican Folk Singers discography aside are about other things more than the subject. The disclaimer "I'm working from interviews… not from listening" is useful once, but the repeated "that is my inference/reading" hedges add bulk.
- A: the reference-points list and the reception table are lists of facts. The birth name and the origin of the nickname are biographical padding.
- C: the "evidence" note naming studio crew whose roles are unknown is padding.

## rust: A > B (slight)

**Main reason.** A leaves you understanding why the rules exist and where the borrow checker sits among other ideas, not only what the rules are. It frames shared/exclusive access as "a reader-writer lock that is checked at compile time and then erased", ties that to `RefCell` and `RwLock`, and explains that non-lexical lifetimes are why the `println!` example compiles once the line is removed. B is excellent, faster to read and more practical, so the margin is small.

- **A.** Strength: real depth on why and how. It explains the mutation-changes-shape reasoning, links the problem to C++ iterator invalidation, covers Cyclone regions as the origin of lifetimes, and describes how the checker runs on MIR. Weakness: it barely covers ownership and moves, which a newcomer needs. The Cyclone, Niko 2012 and Polonius-status passages add history and a hedged news item at some cost in reading time.
- **B.** Strength: compact and concrete. It gives three rules, a failing example with its error code for each, and a well-ordered list of fixes, including ownership/move, which A skips. Weakness: it stays at the level of "what the rules are and how to get unstuck" and says little about why the design is this way or how the checker reasons.

**Flags.**
- A: the Polonius Alpha nightly and stabilisation timeline is news detail rather than understanding. The Niko Matsakis 2012 attribution is history that is not needed to understand the checker.
- B: no padding of note. The closing offer to walk through a pasted error is a conversational extra, not padding.
