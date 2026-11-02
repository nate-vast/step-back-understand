---
name: step-back-understand
description: "Explain a person, work, idea, product or system through what shaped it: trace its influences, foundations and ingredients, study those sources, and return with evidenced connections. Use when explicitly invoked or when asked to understand a subject through its influences or origins."
---

# Step Back Understand

To understand a thing, study the things that made it what it is. Run the five steps below, then report in the required output format.

## 1. Anchor the subject

- **Do:** name the subject (person, work, idea, product, system) and the aspect the user wants to understand. Inspect the subject itself, or one representative work, before tracing backward.
- **Do:** if the aspect is unclear, ask one question before researching. Do not invent the question for the user.
- **Avoid:** a generic request to learn an entire field.
- **Done when:** you have a concrete subject and one open question about it.

## 2. Map what shaped it

- **Do:** list candidate influences: teachers, earlier works, disciplines, components, dependencies, collaborators, experiences, constraints. For each, write what it might explain about the subject.
- **Do:** treat names the user supplies as leads, not as proof of influence.
- **Avoid:** picking connections for fame or proximity. Pick them for explanatory value.
- **Done when:** you have a short map of subject, shaping source, what that source may explain. Three to six sources is a normal size.

## 3. Study the sources, not their names

- **Do:** engage with the shaping source's actual material as far as your tools allow: texts, interviews, autobiographies, liner notes, scores, transcriptions, code, docs, papers, commit history, published analyses.
- **Do:** when the primary work cannot be inspected directly (audio, video, a physical object), say so, and rely on first-person accounts and credible documented analyses instead. Never claim to have listened to, watched or handled something you did not.
- **Do:** classify every connection you keep with one evidence class:
  - `documented`: the subject or a credible primary source states the influence.
  - `composition`: the source is an observable part or dependency of the subject (a sample, a library, a cited paper, a shared collaborator on the record).
  - `interpretive`: a comparison you or a critic draws; similarity alone, not proof.
  - `unknown`: plausible but no evidence found.
- **Do:** cite a source for each connection: URL, title, or document and date. Do not cite from memory without checking.
- **Avoid:** a biography summary or an influence list standing in for the study.
- **Done when:** each connection has the specific thing carried forward, an evidence class, and a source.

## 4. Go deeper only where it helps

- **Default depth:** one layer back. Go a second layer only for one or two sources that remain opaque and matter to the open question.
- **Do:** keep the original subject visible while exploring. Deeper understanding can be the deliverable even without an immediate practical payoff.
- **Stop when:** you can explain the meaningful connections, or when evidence or scope runs out. In that case state the unanswered branches explicitly and stop. Do not keep researching to fill them.

## 5. Return to the subject

- **Do:** explain how the subject absorbed, combined, changed or rejected those inputs, and what remains distinctive about it. Tie each point to a concrete feature of the subject.
- **Do:** if there is a current task, say what this understanding changes about it. If the purpose is learning, say what the user can now recognize.
- **Avoid:** reducing a person or work to a sum of influences.

## Required output

```md
STEP-BACK UNDERSTANDING

Subject and question:
- ...

Inspected directly:
- what you examined of the subject itself, and what you could not

Connections:
| Shaping source | What carried forward | Evidence | Source |
| --- | --- | --- | --- |
| ... | ... | documented / composition / interpretive / unknown | ... |

What this reveals about the subject:
- ...

What remains distinctive:
- ...

Unanswered branches:
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

```md
STEP-BACK UNDERSTANDING

Subject and question:
- SQLite: why is it a single-file, serverless database when its contemporaries were client-server?

Inspected directly:
- SQLite's own "About" and "Appropriate Uses" pages, the file-format spec, the 2000-era release notes.

Connections:
| Shaping source | What carried forward | Evidence | Source |
| --- | --- | --- | --- |
| Hipp's work on a US Navy guided-missile destroyer program | need for a DB that runs with no admin when the server is down | documented | Hipp interviews (Changelog #201, 2016) |
| Tcl's extension model | SQLite began as a Tcl extension; its C API mirrors Tcl's simplicity | documented | sqlite.org "Tcl interface" history |
| PostgreSQL's SQL syntax | the grammar SQLite copied as its dialect | documented | sqlite.org "SQL As Understood By SQLite" |

What this reveals about the subject:
- The serverless design is a response to a deployment constraint, not a performance idea.

What remains distinctive:
- Treating the database as a file format, with a public, stable on-disk spec.

Unanswered branches:
- Which pre-2000 embedded databases (Berkeley DB, gdbm) Hipp looked at; not found in primary sources.
```
