---
name: step-back-understand
description: "Understand a person, work, idea, product, system or anything else by learning the things that shaped it: find its influences, foundations and ingredients, study each of those as a subject in its own right, then see the original through them. Use when invoked by name or when the user explicitly asks to understand a subject through what shaped it."
---

# Step Back Understand

To understand a thing, learn the things that made it what it is.

You can read about John Mayer and know John Mayer. Learn Stevie Ray Vaughan, Jimi Hendrix, B.B. King and Albert King as players in their own right, and you hear Mayer differently: you recognize whose bends those are, where the chord-melody rhythm playing comes from, and what is his alone. The deliverable is that richer understanding. Explanation, sources and evidence labels serve it; they are not the goal. The subject can be anything: a person, a song, a product, a codebase, a concept, a company, a recipe.

## What to look for, by kind of subject

| Subject | Shaping sources to look for |
| --- | --- |
| Person | teachers, heroes, scenes and places, collaborators, formative jobs or hardships, the tools they grew up with |
| Work (album, book, film, paper) | earlier works, genre conventions, the tools and constraints of its making, the maker's own prior work |
| Product or system | predecessor products, papers and design ideas it inherits, dependencies, the constraints it was built under, the team's earlier work |
| Concept or method | the problem it answered, the field it came from, the earlier idea it replaced or reacted against, its first practitioners |
| Organization | founders' previous companies, the gap in the market, the culture it copied or rejected |

The loop is the same for all of them.

## 1. Anchor the subject

- **Do:** name the subject and the aspect to understand. Inspect the subject itself, or one representative work, before tracing backward.
- **Do:** if a useful starting scope is apparent, state it and begin. Ask first only when the ambiguity would materially change the inquiry. Never silently substitute a different goal for the user's.
- **Avoid:** a generic request to learn an entire field.
- **Done when:** you have a concrete subject and one open question about it.

## 2. Map what shaped it

- **Do:** list candidate shaping sources using the table above. For each, write what it might explain about the subject.
- **Do:** treat names the user supplies as leads, not as proof of influence.
- **Avoid:** picking sources for fame or proximity. Pick them for explanatory value.
- **Done when:** you have a short map: subject, shaping source, what that source may explain.

## 3. Learn each source as a subject in its own right

This step is the heart of the skill. A name on a list teaches nothing.

- **Profile each source.** For every shaping source, learn what makes it what it is: its three to five signature traits, where it came from, what it is known for, what it did differently from what came before it. Engage with its actual material as far as your tools allow: texts, interviews, autobiographies, liner notes, scores, transcriptions, code, docs, papers, commit history, published analyses.
- **Map the traits forward.** For each trait, ask whether it shows up in the subject, and how the subject changed it. Stevie Ray Vaughan's thing is Albert King's bends on top of a Texas shuffle at full volume; Mayer keeps the bends and the Stratocaster but drops the aggression. That kind of sentence is the output of this step.
- **Be honest about inspection.** When the primary work cannot be inspected directly (audio, video, a physical object), say so and rely on first-person accounts and credible documented analyses. Never claim to have listened to, watched or handled something you did not.
- **Tag each connection** with one evidence class, so a plausible link is never presented as established history:
  - `documented`: the subject or a credible primary source states the influence.
  - `composition`: the source is an observable part or dependency of the subject (a sample, a library, a cited paper, a shared collaborator on the record).
  - `interpretive`: a comparison you or a critic draws; similarity alone, not proof.
  - `unknown`: plausible but no evidence found.
- **Cite** a source for each connection: URL, title, or document and date. Check that the source supports the exact claim you attach it to, not just the general topic. Do not cite from memory without checking.
- **Avoid:** a biography summary or an influence list standing in for the study.
- **Done when:** each source has a profile, and each connection names the specific trait carried forward, how it was transformed, an evidence class, and a source that supports it.

## 4. Go deeper where it improves understanding

- **Do:** follow a branch while it materially improves understanding of the subject. There is no fixed generation count.
- **When a second layer is worth it:** when a first-layer source is itself best understood through its own sources. Stevie Ray Vaughan is best understood through Albert King, so learning Albert King is part of learning Mayer.
- **Do:** keep the original subject visible while exploring, and respect the scope the user set. Deeper understanding can be the deliverable even without an immediate practical payoff.
- **Stop when:** the explanation is sufficient for the open question, or evidence or scope limits are reached. Disclose the unresolved branches instead of researching to fill them.

## 5. Return to the subject

- **Do:** explain how the subject absorbed, combined, changed or rejected those inputs, and what remains distinctive about it. Tie each point to a concrete feature of the subject.
- **Do:** say what the user can now recognize in the subject that they could not before. This line is required; it is the point of the exercise.
- **Do:** if there is a current task, say what this understanding changes about it.
- **Avoid:** reducing a person or work to a sum of influences.

## Report

Lead with a coherent explanation that teaches the shaping sources and shows what they reveal about the subject. Integrate evidence and uncertainty where they matter, in the sentence that makes the claim. Use a table or the template below only when it makes the explanation clearer; do not fill out a form.

Whatever the form, the report must cover:

- the subject and the open question;
- what you inspected directly, and what you could not;
- what each shaping source studied is like in its own right;
- the concrete connections, each with the trait carried forward, how it was transformed, its evidence class, and a source;
- what those connections reveal about the subject;
- what remains distinctive about the subject, or that this pass could not establish it;
- what the user can now recognize that they could not before;
- unresolved branches and consequential uncertainty;
- what changes for the current task, if there is one.

Apply the same evidence standard to the concluding prose as to the connections. A summary sentence may not claim more than the evidence above it showed. If a conclusion is interpretation, say so and give its basis; labelling a claim interpretive does not supply the basis.

Template, for when a structured form helps:

```md
STEP-BACK UNDERSTANDING

Subject and question:
- ...

Inspected directly:
- ...

Sources studied (what each is like in its own right):
- ...

Connections:
| Shaping source | Trait carried forward, and how it changed | Evidence | Source |
| --- | --- | --- | --- |
| ... | ... | documented / composition / interpretive / unknown | ... |

What this reveals about the subject:
- ...

What remains distinctive:
- ...

What you can now recognize:
- ...

Unresolved branches:
- ...

What changes for the current task (if any):
- ...
```

## Check the result

A useful result leaves the user able to recognize something in the subject they could not before. Send it back for another pass if it is any of these:

- a famous-name list with no study of the sources;
- a generic first-principles essay;
- a family tree where connections lack an evidence class or source;
- a chain that never returns to the subject.

## Which step back

Use this skill for understanding, including when nothing has failed. Use `step-back-evaluate` (Step Back Protocol) for stalled work and repeated failed approaches. If that recovery exposes a missing understanding of the subject's foundations, run this skill, then return the findings to the recovery decision.

## Example 1: a musician (abbreviated, in prose)

Sources checked 2026-11-02. No audio was inspected; every claim about how someone plays comes from a named written source, and the final section says what the reader can now check for themselves.

**Subject and question.** John Mayer's lead guitar playing: where do the wide blues bends come from, and what would a listener now be able to hear in them?

**Inspected directly.** Mayer's own statements in interviews, his Rolling Stone writing (via a fan archive, the original is paywalled) and his 2013 Rock and Roll Hall of Fame induction of Albert King. Not inspected: any recording.

**The source learned: Albert King.** King was left-handed and played a right-handed Gibson Flying V flipped over, so the strings ran upside down, high strings nearest the ceiling. He detuned the guitar; Premier Guitar gives C–F–C–F–A–D, Guitar World's account is C# standard, and the exact tuning is disputed. Because the high strings sat on top, he bent by pulling them down toward the floor, which gave him leverage for compound bends wider than a whole step. He plucked with his thumb rather than a pick. Over the V chord he would move the standard blues box up two frets rather than change scale. One signature move is a ghost bend that catches the second and third strings together before striking. All of that is from Jeff Jacobson's lesson in Premier Guitar (2024-01-20); the stringing and pull-down bends are also described in other lessons, the tuning is where sources disagree. Mayer's own description of King at the 2013 induction is a description of exactly this: King is "the reason guitar players break high E strings" (rockhall.com inductee page). Evidence class for the profile: documented analysis by a guitarist-author, not inspection.

**King to Stevie Ray Vaughan.** Alan Paul's book Texas Flood calls King "the number one influence on Stevie Ray Vaughan" and says King's style "was at the very heart of his playing"; Jimmie Vaughan recalls his brother playing "really good Albert King licks" (excerpt on alanpaul.substack.com, 2021-04-25). Jacobson's lesson names a specific trait that crossed over: the two-string ghost bend was "an Albert favorite that SRV later adopted". Evidence: documented.

**Vaughan to Mayer.** Mayer says Vaughan was the first thing he heard that was "not just strumming chords", at 13, on a neighbour's mixtape with Vaughan on one side and Robert Cray on the other (Far Out Magazine, original interview not named), and that on stage Vaughan is "my reference" (KTCZ-FM, 2002-04-16, via johnmayer.info). Mayer "discovered Hendrix by way of Stevie Ray Vaughan" (Rolling Stone, 2010-12-03, via johnmayer.info). Evidence: documented. A Rock Hall interview is reported to have Mayer saying King's playing reached him twice, through Vaughan and then through King's own records; the page returned 404 today, so that line is unverified and not relied on.

**What this reveals.** The chain King to Vaughan to Mayer is documented at every link, and at the King to Vaughan link it is documented at the level of a specific technique. Mayer's own words about King describe King's bending, not his songs or tone, so the thing he names as King's contribution is the bends.

**What remains distinctive.** Not established by this pass. The sources show what Mayer took; what is his own would need his recordings or transcriptions, which were not inspected.

**What you can now recognize.** You know what an Albert King bend is: a pull that goes past a whole step, often on the top string, often two strings caught together, played over a box that moves up for the V chord. When you next hear a Mayer solo you can listen for those specific things instead of a general blues feel, and you can tell a King-style compound bend from a B.B. King-style single-finger bend, which Jacobson describes as the contrasting approach. Whether Mayer's bends in a given song are King's is for your ears to check; this pass did not listen.

**Unresolved.** The Rock Hall "twice" quote. King's actual tuning. Anything about Mayer's chord-melody rhythm playing and Hendrix: critics compare them, no first-person statement was found, and the comparison stays an open question rather than a conclusion.

## Example 2: a product (abbreviated, in the template)

Sources checked 2026-11-02.

```md
STEP-BACK UNDERSTANDING

Subject and question:
- SQLite: why is it a single-file, serverless database when its contemporaries were client-server?

Inspected directly:
- sqlite.org "About SQLite" (https://www.sqlite.org/about.html): "serverless", "does not have a separate server process", "contained in a single disk file", "stable, enduring file format". Not inspected: the early 2000 source tree.

Sources studied:
- D. Richard Hipp's contract work for Bath Iron Works on the DDG-79 Oscar Austin: shipboard software where a database server was one more thing that could fail.
- Tcl: the scripting language SQLite was first an extension of; its test suite is still Tcl.

Connections:
| Shaping source | Trait carried forward, and how it changed | Evidence | Source |
| --- | --- | --- | --- |
| The destroyer software job | "why do we even need a server?"; the aim of no dependencies that can fail | documented | Corecursive #066 transcript, https://corecursive.com/066-sqlite-with-richard-hipp/ |
| Tcl | SQLite "began as a Tcl extension"; the test suite is still Tcl | documented | https://www.sqlite.org/tclsqlite.html; Changelog #201, https://changelog.com/podcast/201 |
| PostgreSQL | used as the reference for how SQL should behave | documented, thin: Hipp answers "Yes" to the interviewer's framing, no first-person elaboration | Changelog #201, https://changelog.com/podcast/201 |

What this reveals about the subject:
- The serverless design answers a deployment constraint (software on a ship with no admin), not a performance idea.

What remains distinctive:
- Treating the database as a file format with a public, stable on-disk spec, now a US Library of Congress recommended storage format.

What you can now recognize:
- Every "zero-configuration" claim in the docs is the ship talking.

Unresolved branches:
- Which earlier embedded databases (Berkeley DB, gdbm) Hipp looked at; nothing found in the sources above.
```
