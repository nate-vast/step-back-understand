# Step Back Understand

**To understand a thing, learn the things that made it what it is.**

You can read about John Mayer and know John Mayer. Learn Stevie Ray Vaughan, Jimi Hendrix, B.B. King and Albert King as players in their own right, and you hear Mayer differently. This agent skill does that for anything: a person, a work, an idea, a product, a system, a company. It finds what shaped the subject, studies the most important of those influences in their own right, and then explains the subject itself: how it works, why it is that way, and what is its own.

## The loop

1. Look at the subject itself and note what you cannot yet explain.
2. Find what shaped those features.
3. Learn the two to five influences that explain the most, as subjects in their own right, not merely their names.
4. Turn the lineage into understanding: why the subject is this way, what to expect from it, its context, and what is its own.
5. Answer about the subject. An influence appears only where it makes a specific feature click.

The influences are the agent's research, not the answer. The answer opens with the idea that organizes the subject, covers the whole subject, gives each main point its reason, and keeps uncertainty in plain words. Resemblance alone does not prove influence: a link the makers have not confirmed is called a resemblance.

The whole skill in two sentences: research the subject thoroughly, including the things that shaped it; then explain the subject itself (what it is, how it works, why it is this way, its context), bringing in an influence only where it explains a specific feature. Pasting those two sentences into a request gets most of the benefit. The skill file adds the detail that kept answers on the subject in testing (see Status).

## Install

Clone this repository:

```sh
git clone https://github.com/neonotics-png/step-back-understand.git
```

Copy the [`step-back-understand`](./step-back-understand) directory into your agent's skill directory. The portable entry point is [`SKILL.md`](./step-back-understand/SKILL.md).

| Runtime | Path |
| --- | --- |
| Claude Code (personal) | `~/.claude/skills/step-back-understand/SKILL.md` |
| Claude Code (one project) | `<project>/.claude/skills/step-back-understand/SKILL.md` |
| Codex | `~/.codex/skills/step-back-understand/SKILL.md` |
| Shared repo | `skills/step-back-understand/SKILL.md` |

Other runtimes differ; check where they discover `SKILL.md` files.

## Invoke

The skill runs when invoked by name, or when you explicitly ask to understand a subject through what shaped it. In Claude Code, `/step-back-understand` works once installed. In any runtime:

```text
Use step-back-understand to explore what shaped [subject].
```

For example:

```text
Use step-back-understand on John Mayer's guitar playing. Where do the
bends and the chord-melody rhythm style come from, and what is his own?
```

The answer is about the subject, organized by the subject's features and not by its influences, with a short reference list at the end. The agent's research notes stay out unless you ask for them. An abbreviated example is at the end of [`SKILL.md`](./step-back-understand/SKILL.md).

## Which step back?

- **Step Back Understand:** study what shaped a subject, even when nothing has gone wrong.
- **[Step Back Protocol](https://github.com/neonotics-png/step-back-protocol):** use `step-back-evaluate` to reframe stalled work and repeated failed approaches.

This skill stands alone; the recovery skill is not a dependency.

## Status

Current revision: 2026-11-11. The influences are the agent's research, and the answer explains the subject itself. Best on subjects the agent does not already know well.

What testing has shown so far (all writers, scorers and judges are models; samples are small):

- **The answer is better than a plain thorough answer.** 2026-11-03, three subjects past the model's training cutoff or niche, two runs per arm: blind judges ranked the skill's answers first and second in all three subjects, ahead of answers from a plain request told to research thoroughly, at about half the length ([test](./docs/behavior-test-2026-11-03-v5.md)).
- **The agent does not learn more than it would from researching thoroughly.** Same test, quiz answered by the agent after studying: skill 91/96, thorough plain 93/96, plain 72/96. On 2026-11-11 the three arms again scored within one or two points of each other.
- **Against the two-sentence instruction above.** 2026-11-11, three subjects (a coding agent released in October 2026, an album released in October 2026, and Rust's borrow checker), one run per arm, blind judges from two model families asked which answer they would rather receive ([test](./docs/behavior-test-2026-11-11.md)). The 2026-11-03 revision lost to the two sentences on both new subjects (0 of 4 judge calls): its answers were short, asserted points without their reasons, and drifted into the influences' own histories. This revision was preferred in 5 of 6 judge calls: both judges on the coding agent and on Rust, a split on the album. Its answers carried slightly less of an independent quiz's content on the two new subjects (9 and 10 of 16, against 11 and 11) and slightly more on Rust (10 against 9).
- **Famous subjects.** An early revision that made the influences the answer lost to a plain answer on six well-known subjects ([fair test](./docs/behavior-test-2026-11-03-fair.md)). On Rust's borrow checker the current approach was preferred to a plain answer and to the two-sentence instruction by both judges each time.

Not yet tested: a human reader, more than one run per arm in the latest round, and tasks that depend on the lineage's predictions. Cost: roughly the research of a thorough answer. Publishing or cloning this repository does not activate it in an agent runtime.

## License

[MIT](./LICENSE)
