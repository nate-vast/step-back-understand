---
name: step-back-understand
description: "Explain a person, work, idea, product or system through what shaped it: trace its influences, foundations and ingredients, study those sources, and return with evidenced connections. Use when explicitly invoked or when asked to understand a subject through its influences or origins."
---

# Step Back Understand

To understand a thing, study the things that made it what it is. Run the five steps below, then report what you found.

## 1. Anchor the subject

- **Do:** name the subject (person, work, idea, product, system) and the aspect the user wants to understand. Inspect the subject itself, or one representative work, before tracing backward.
- **Do:** if a useful starting scope is apparent, state it and begin. Ask a question first only when the ambiguity would materially change the inquiry. Never silently substitute a different goal for the user's.
- **Avoid:** a generic request to learn an entire field.
- **Done when:** you have a concrete subject and one open question about it.

## 2. Map what shaped it

- **Do:** list candidate influences: teachers, earlier works, disciplines, components, dependencies, collaborators, experiences, constraints. For each, write what it might explain about the subject.
- **Do:** treat names the user supplies as leads, not as proof of influence.
- **Avoid:** picking connections for fame or proximity. Pick them for explanatory value.
- **Done when:** you have a short map of subject, shaping source, what that source may explain.

## 3. Study the sources, not their names

- **Do:** engage with the shaping source's actual material as far as your tools allow: texts, interviews, autobiographies, liner notes, scores, transcriptions, code, docs, papers, commit history, published analyses.
- **Do:** when the primary work cannot be inspected directly (audio, video, a physical object), say so, and rely on first-person accounts and credible documented analyses instead. Never claim to have listened to, watched or handled something you did not.
- **Do:** classify every connection you keep with one evidence class:
  - `documented`: the subject or a credible primary source states the influence.
  - `composition`: the source is an observable part or dependency of the subject (a sample, a library, a cited paper, a shared collaborator on the record).
  - `interpretive`: a comparison you or a critic draws; similarity alone, not proof.
  - `unknown`: plausible but no evidence found.
- **Do:** cite a source for each connection: URL, title, or document and date. Check that the source supports the exact claim you attach it to, not just the general topic. Do not cite from memory without checking.
- **Avoid:** a biography summary or an influence list standing in for the study.
- **Done when:** each connection has the specific thing carried forward, an evidence class, and a source that supports it.

## 4. Go deeper where it improves understanding

- **Do:** follow a branch while it materially improves understanding of the subject. If a shaping source remains opaque, repeat the inquiry for what shaped that source. There is no fixed generation count.
- **Do:** keep the original subject visible while exploring, and respect the scope the user set. Deeper understanding can be the deliverable even without an immediate practical payoff.
- **Stop when:** the explanation is sufficient for the open question, or evidence or scope limits are reached. Disclose the unresolved branches instead of researching to fill them.

## 5. Return to the subject

- **Do:** explain how the subject absorbed, combined, changed or rejected those inputs, and what remains distinctive about it. Tie each point to a concrete feature of the subject.
- **Do:** if there is a current task, say what this understanding changes about it. If the purpose is learning, say what the user can now recognize.
- **Avoid:** reducing a person or work to a sum of influences.

## Report

Whatever the form, the report must cover:

- the subject and the open question;
- what you inspected directly, and what you could not;
- the concrete shaping connections, each with what carried forward, its evidence class, and a source;
- what those connections reveal about the subject;
- what remains distinctive about the subject;
- unresolved branches and consequential uncertainty;
- what changes for the current task, if there is one.

Choose the form that explains the subject best: a short narrative, a table, a diagram, or the template below. The template is a default, not a requirement.

```md
STEP-BACK UNDERSTANDING

Subject and question:
- ...

Inspected directly:
- ...

Connections:
| Shaping source | What carried forward | Evidence | Source |
| --- | --- | --- | --- |
| ... | ... | documented / composition / interpretive / unknown | ... |

What this reveals about the subject:
- ...

What remains distinctive:
- ...

Unresolved branches:
- ...

What changes for the current task (if any):
- ...
```

## Check the result

A useful result explains at least one connection that changes how the subject is understood. Send it back for another pass if it is any of these:

- a famous-name list with no study of the sources;
- a generic first-principles essay;
- a family tree where connections lack an evidence class or source;
- a chain that never returns to the subject.

For a musician, study the candidate shaping artists' relevant work and the evidence of connection before attributing influence. For a product or system, inspect the constituent mechanisms and inherited design ideas before explaining the visible behavior. The loop is the same in both domains.

## Which step back

Use this skill for understanding, including when nothing has failed. Use `step-back-evaluate` (Step Back Protocol) for stalled work and repeated failed approaches. If that recovery exposes a missing understanding of the subject's foundations, run this skill, then return the findings to the recovery decision.

## Example (abbreviated)

Sources checked 2026-11-02. Each row's source was read and supports the wording of that row.

```md
STEP-BACK UNDERSTANDING

Subject and question:
- SQLite: why is it a single-file, serverless database when its contemporaries were client-server?

Inspected directly:
- sqlite.org "About SQLite" (https://www.sqlite.org/about.html): "serverless", "does not have a separate server process", "contained in a single disk file", "stable, enduring file format".
- Not inspected: the early 2000 source tree.

Connections:
| Shaping source | What carried forward | Evidence | Source |
| --- | --- | --- | --- |
| Hipp's contract work for Bath Iron Works on software for the DDG-79 Oscar Austin | the question "why do we even need a server?", and the aim of having no dependencies that can fail | documented | Corecursive #066 transcript, https://corecursive.com/066-sqlite-with-richard-hipp/ |
| Tcl | SQLite "began as a Tcl extension"; the test suite is still Tcl | documented | https://www.sqlite.org/tclsqlite.html; Changelog #201, https://changelog.com/podcast/201 |
| PostgreSQL | used as the reference for how SQL should behave | documented, thin: Hipp answers "Yes" to the interviewer's framing, no first-person elaboration | Changelog #201, https://changelog.com/podcast/201 |

What this reveals about the subject:
- The serverless design answers a deployment constraint (software on a ship with no admin), not a performance idea.

What remains distinctive:
- Treating the database as a file format with a public, stable on-disk spec, now a US Library of Congress recommended storage format.

Unresolved branches:
- Which earlier embedded databases (Berkeley DB, gdbm) Hipp looked at; nothing found in the sources above.
```
