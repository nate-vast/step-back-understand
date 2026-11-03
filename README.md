# Step Back Understand

**To understand a thing, learn the things that made it what it is.**

You can read about John Mayer and know John Mayer. Learn Stevie Ray Vaughan, Jimi Hendrix, B.B. King and Albert King as players in their own right, and you hear Mayer differently. This agent skill does that for anything: a person, a work, an idea, a product, a system, a company. It finds what shaped the subject, studies each of those sources as a subject in its own right, and returns with what you can now recognize in the original.

## The loop

1. Inspect the subject itself.
2. Identify what shaped it.
3. Learn each source as a subject in its own right, not merely its name.
4. Trace further back only where it improves understanding.
5. Return to the original subject and explain what the connections reveal.

Depth is flexible: follow a branch while it materially improves understanding, keep the original subject visible, and stop when the explanation is sufficient or evidence runs out. Deeper understanding can be the result; it does not have to justify an immediate action. Connections require evidence: resemblance alone does not prove influence, and every connection in the output is labelled `documented`, `composition`, `interpretive` or `unknown`, with a source.

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

The result leads with an explanation that teaches the shaping sources and shows what they reveal about the subject, with evidence and uncertainty woven in where they matter. It covers the question, what was inspected, what each source is like in its own right, the connections with their evidence, what they reveal, what remains distinctive, what you can now recognize, and what is unresolved. A table or template is used only when it makes the explanation clearer. Two abbreviated examples, one in prose and one in the template, are at the end of [`SKILL.md`](./step-back-understand/SKILL.md).

## Which step back?

- **Step Back Understand:** study what shaped a subject, even when nothing has gone wrong.
- **[Step Back Protocol](https://github.com/neonotics-png/step-back-protocol):** use `step-back-evaluate` to reframe stalled work and repeated failed approaches.

This skill stands alone; the recovery skill is not a dependency.

## Status

v2 procedure. Behavior-tested twice on 2026-11-02 with three subjects (a musician, a product, an idea), each run with and without the skill: [first test](./docs/behavior-test-2026-11-02.md) on the earlier revision, [second test](./docs/behavior-test-2026-11-02-v3.md) on the current "learn each source in its own right" procedure. In the second test all three skill runs studied the sources from their own material and went a layer further back where it helped. Nine blind graders preferred the skill answer 8 times out of 9, scoring it about 27% higher on teaching the sources, revealing the subject, distinctiveness and support, and about 35% lower on readability. Cost: roughly a third to a half more tokens and time than answering without the skill, almost all of it fetching source material. One run per cell, one reader; initial evidence, not a guarantee. Publishing or cloning this repository does not activate it in an agent runtime.

## License

[MIT](./LICENSE)
