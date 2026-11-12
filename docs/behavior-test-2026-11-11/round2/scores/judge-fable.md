pi: B > A (clear)
mcdoom: B > A (slight)
rust: A > B (clear)

# Blind judgment, round 2

Read as the asker: a capable adult who does not know the subject. I read B before A for each question, used no web access, and could not check any factual claim, so this judges explanation and not accuracy.

## 1. Rust's borrow checker

**Preference: A over B, clear.**

A teaches the subject in the order a newcomer needs it: ownership with a move example, then the one rule, then lifetimes, then why safe-looking code is rejected, then the ways out. Each step says why before moving on. B covers more ground, but about a third of it is material a first-time reader cannot use yet, and it compresses ownership into a single bullet.

Example: A turns the rule into something you can reason with. "Exclusivity is the guarantee; the permission to write follows from it," and later, of `RefCell` and `Mutex`, "The rule never goes away; only when it is checked changes." B makes the same points but follows them with Stacked Borrows, Tree Borrows, RustBelt, view types and place-based lifetimes.

- **A.** Strength: one continuous line of reasoning from ownership to the aliasing rule to the friction it causes, with a reason at every step. Weakness: the conditional-return limitation is described only in prose, where B's code example makes it much easier to see.
- **B.** Strength: the "why" material is the richest of the two (aliasing plus mutation as the root of the bugs, per-function checking as a deliberate trade-off, the lexical to NLL to Polonius history with a worked example). Weakness: it is about half as long again and drifts into a reference survey, with terms such as "flow-insensitive", "autoref" and "origin" used without explanation.

**Flags**

- B, "What it does not cover: `unsafe`": the second paragraph (Stacked Borrows, Tree Borrows, Miri flags, RustBelt) is about research on unsafe code, not about the borrow checker a learner meets.
- B, "What's coming": a list of roadmap items (view types, place-based lifetimes, self-referential structs) with almost no explanation.
- B, "How it works inside the compiler" and the bullet on early Rust pointer kinds (`@T`, `~T`): accurate-sounding detail that adds little understanding at this level.
- B, "The short version": restates the opening at the end of an already long answer.
- B, the error table: dense, but it is the one list that earns its place, because each row maps a message to a cause and a fix.
- A, "Tools for when ownership doesn't fit": a list, but each item carries its reason. The Cyclone aside in the `Rc` bullet is a small digression.
- A: no real padding found.

## 2. June McDoom, *Follow the Light*

**Preference: B over A, slight.**

B gets the organizing idea across faster and makes it stick: two layers, folk on top and Jamaican bass underneath, and nearly everything else follows from how they meet. A leaves me knowing somewhat more (the inheritance theme, a guess at the title, why critics split), but it takes roughly half as much reading again, and a good part of the extra is description of other artists' records.

Example: B's picture of her father's bass coming "up through her bedroom floor while she listened to folk records upstairs," followed by "The album recreates that arrangement: folk on top, Jamaican bass underneath." A has the same facts (he "ran sound systems at home") but never delivers the image, so its account is more complete and less memorable.

- **B.** Strength: a single clear model of the record, each feature tied to a cause, and a concrete listening plan at the end. Weakness: almost nothing on what the album is about; it never addresses the theme or the title, and the jazz paragraph is thin.
- **A.** Strength: the deeper account, including the inheritance theme, the lyrics of the singles, and an actual explanation of the mixed reviews (stacked, perfected parts carry weight only when the song underneath is strong). Weakness: the third section spends much of its length on Bacharach, Spector, Riperton, *Victorialand* and *Hosianna Mantra*, and the repeated hedges ("though I haven't confirmed that") slow it down.

**Flags**

- A, section 3: closest thing in either answer to being about other things. Each reference is tied back to the album in a sentence, but the paragraph on *Victorialand* and Popul Vuh describes those records at more length than the songs they are meant to explain.
- A, Pentangle paragraph: a named reference point with a loose link to the album.
- A, the upfront "I haven't heard the record": not padding. It is useful for trust, and so are the hedges, though they leave the "Grandpa" point unresolved where B simply states it.
- B, "What it is": the biography sentence (EPs, tours, the Margo Guryan tribute) and the tracklist plus singles are facts listed without explanation. A also lists the tracklist.
- B, "As of mid-November 2026, Pitchfork, the Guardian and Paste had not reviewed it": filler.
- B, the Apple Music comparisons (Judee Sill, Nina Simone, Alton Ellis): names dropped with no explanation of the link.

## 3. Pi 1.0

**Preference: B over A, clear.**

B gives me a thesis I can hang everything on, that Pi is "a deliberate counter-design to Claude Code," and then shows each design choice following from it. A contains more facts, and its "Why it is this way" section is substantive, but that section arrives only after long feature lists, so I read the what before I had a reason to care, and then read parts of it again as the why.

Example: B explains Codemode by its effect. The demo pulls 167 Linear issues and returns "one summary (156 neutral, 11 mildly frustrated) instead of 167 tool results in context," and B adds when it helps: it "pays off most when a task chains many tool calls or filters a lot of data, and it saves little on a single lookup." A describes the same feature as a bullet of properties, ending in OAuth details.

- **B.** Strength: every feature and omission comes with its reason, and the MCP reversal is told as one story (objection, what changed, the fix). Weakness: it leans almost entirely on the makers' own framing, with little on the company, the criticism, or the package architecture.
- **A.** Strength: the more complete briefing, with the four-package layering, the caching argument against MCP, why JavaScript was chosen, upgrade notes, and outside concerns. Weakness: organized as an inventory, so the understanding is scattered and the detail level is often past what the question needs.

**Flags**

- A, "What 1.0 adds" and "Upgrade gotchas": lists of facts without explanation. Items such as "RFC 9207 `iss` checks" and credentials "keyed by server name plus URL" are changelog detail.
- A, "Pi Durable, briefly": four detailed bullets on a separate, experimental package. This is more about another thing than about Pi 1.0. B handles it in three sentences.
- A, "Context": investor names, Lefos, the Hacker News point count, and the unresolved surname ("check before citing it") read as padding. The hedging on dates and names is honest, but it puts research loose ends in front of the reader.
- A, the "Why" section repeats points already made in "How Pi works" (tiny prompt, omissions).
- B, "Smaller additions": a compressed fact list, including two breaking changes a newcomer does not need.
- B, the install line and the Emacs comparison: minor. The comparison is labelled as the writer's own, which is the right way to do it.
- B, the Cloudflare and Anthropic comparison for Codemode: slightly off-subject, but labelled as a resemblance and used to set expectations.
