# step-back-understand: skill vs a two-sentence instruction (2026-11-11)

Question: the 2026-11-03 tests showed the skill's answers beat a plain thorough answer. Does the skill file add anything over two sentences that state its idea?

The two-sentence instruction: "Research it thoroughly, including the things that shaped it. Then explain the subject itself (what it is, how it works, why it is this way, its context), bringing in an influence only where it explains a specific feature."

## Subjects

- Pi 1.0, a terminal coding agent released October 2026 (past the writers' training data).
- June McDoom's album *Follow the Light*, released October 2026 (past the writers' training data).
- Rust's borrow checker (famous; the case where an early revision lost to a plain answer on 2026-11-03).

## Design

- Same request for every arm: "Help me understand X." Web access allowed. One run per arm per round.
- Independent quiz writers for the two new subjects (never told a skill exists): 8 questions with a sourced key and a 0/1/2 rubric. Rust reuses the 2026-11-03 quiz.
- Measures:
  - **Judges:** blind, shuffled labels, asked which answer they would rather receive as the asker, weighing understanding against reading time. Two judges per round, reading in opposite orders.
  - **Coverage:** a blind scorer marks, per quiz question, whether a reader with only the answer text could answer it (0/1/2, 16 max).
  - **Agent quiz (round 1 only):** the agent that did the research answers the quiz afterwards with no further lookups.
- Models: round 1 writers Claude Fable 5.2, scorers and judges Claude Opus 5.5. Rounds 2 to 4 writers Claude Opus 5.5, judges one Opus 5.5 and one Fable 5.2, scorer Opus 5.5.
- The skill file used in each round is in `behavior-test-2026-11-11/skill-revisions/`.

## Round 1: the 2026-11-03 revision (674cfe5)

| Subject | Arm | Words | Lookups (searches + pages) | Agent quiz /16 | Coverage /16 | Judge 1 rank | Judge 2 rank |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Pi 1.0 | skill | 890 | 9 + 17 | 15 | 11 | 2 | 2 |
| Pi 1.0 | two sentences | 1,669 | 7 + 33 | 16 | 13 | 1 | 1 |
| Pi 1.0 | plain, "research thoroughly" | 1,303 | 14 + 44 | 16 | 11 | 3 | 3 |
| Album | skill | 827 | 7 + 18 | 14 | 10 | 3 | 3 |
| Album | two sentences | 1,331 | 12 + 22 | 14 | 13 | 1 | 1 |
| Album | plain, "research thoroughly" | 1,234 | 17 + 37 | 15 | 13 | 2 | 2 |
| Rust | skill | 1,000 | 5 + 13 | n/a | 9 | 1 | 1 |
| Rust | plain (no research instruction) | 648 | 0 | n/a | 7 | 2 | 2 |

- Skill against the two sentences on the new subjects: 0 of 4 judge calls.
- Skill against a plain answer on Rust: 2 of 2 judge calls. The plain run did no research, so effort differs.
- What the judges said about the skill's answers: short, with points stated but not explained; a paragraph each on influences' own histories (a drum engineer's track record, another band's 1972 album, a prior-art blog post); space spent on the writer's own hedges and on what could not be found; thin on basic parts of the subject.
- What the agents running the skill reported as unclear: no instruction for the weak (famous-subject) case; "sources" used for both influences and citations; whether prior knowledge counts as learning an influence; whether "two to five" is per subject or per feature; whether predictions belong in the answer; what to do with conflicting facts, unnamed but obvious influences, and a subject that cannot be examined; no length guidance.

## What changed in the skill after round 1

- The two-sentence core is stated near the top.
- Answer rules added: open with the organizing idea; cover the whole subject and define terms the explanation rests on; give every main point its reason; give only the trait of an influence that explains a feature, with a counter-example; no closing recap or bare lists; do not narrate the research; a length guide for broad questions.
- Research rules clarified: the weak case gets a short pass; "influences" and "references" are separate words; prior knowledge counts but specific traits get checked; search summaries are not references; side-detail conflicts are left out; unnamed influences are called resemblances.
- The check list gained three items (missing basic part, missing reason, missing organizing idea).

## Rounds 2 to 4: revised skill against the two sentences

The two-sentence answers were written once in round 2 and reused as the comparison in rounds 3 and 4.

| Round | Subject | Skill words | Two-sentence words | Judge (Opus 5.5) | Judge (Fable 5.2) | Coverage skill / two sentences |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | Pi 1.0 | 1,744 | 1,953 | skill, clear | skill, clear | 8 / 11 |
| 2 | Album | 1,625 | 1,157 | two sentences, slight | two sentences, slight | 10 / 11 |
| 2 | Rust | 1,546 | 2,411 | skill, slight | skill, clear | 9 / 9 |
| 3 | Album | 1,632 | 1,157 | two sentences, slight | two sentences, slight | not scored |
| 4 (final file) | Pi 1.0 | 1,484 | 1,953 | skill, clear | skill, clear | 9 / 11 |
| 4 (final file) | Album | 1,450 | 1,157 | two sentences, slight | skill, slight | 10 / 11 |
| 4 (final file) | Rust | 1,464 | 2,411 | skill, clear | skill, clear | 10 / 9 |

- Round 2: skill preferred in 4 of 6 judge calls. On the album it still spent a section on other artists' records.
- Round 3 (album only, after tightening the influence rule): no change in the verdict.
- Round 4 (the file now in the repository): skill preferred in 5 of 6 judge calls; the album split.

## Reading the result

- The idea carries most of the value. In round 1 the two sentences beat both the 2026-11-03 skill file and a plain thorough answer on both new subjects, with both judges.
- The revised file is preferred to the two sentences on two of three subjects by both judges, and ties on the third. What it adds is discipline in the answer (one organizing idea, reasons, shorter than an unconstrained answer on a famous subject), not more research and not more learning.
- Coverage of quiz content goes slightly the other way on the two new subjects: the two-sentence answers contain a little more of what the quiz asked.
- Music is the weak spot: in every round the skill's album answer spent more words on influences than judges wanted.

## Caveats

- One run per arm per round. Run-to-run variation is not measured, and the round 2 two-sentence answers are reused in rounds 3 and 4.
- The skill was revised between rounds using the judges' reasons on these same three subjects, so round 4 is not an independent test of the final file. A fresh set of subjects is the next check.
- Round 1 and rounds 2 to 4 used different writer models, so the before-and-after comparison mixes a skill change with a model change.
- Writers, scorers and judges are all models. No human reader yet.
- Factual accuracy was checked only against the quiz keys. One skill answer on Rust (round 4) has a code example that fails with a different error than the text describes.

Raw data: `behavior-test-2026-11-11/` (quizzes and keys, every answer, quiz sheets, scores, judge notes, label keys, the skill file used in each round).
