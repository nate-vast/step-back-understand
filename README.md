# Step Back Understand

**To understand a thing, study the things that made it what it is.**

An agent skill for understanding a person, work, idea, product, or system through the influences, foundations, ingredients, and conditions that shaped it.

## The loop

1. Inspect the subject itself.
2. Identify what shaped it.
3. Study those sources, not merely their names.
4. Trace further back only where it improves understanding.
5. Return to the original subject and explain what the connections reveal.

Depth is flexible: one layer back by default, a second only for sources that stay opaque. Deeper understanding can be the result; it does not have to justify an immediate action. Connections require evidence: resemblance alone does not prove influence, and every connection in the output is labelled `documented`, `composition`, `interpretive` or `unknown`, with a source.

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

In Claude Code, `/step-back-understand` works once installed. In any runtime:

```text
Use step-back-understand to explore what shaped [subject].
```

For example:

```text
Use step-back-understand on SQLite. Why is it a single-file, serverless
database when its contemporaries were client-server?
```

The skill returns a fixed block: the subject and question, what was inspected directly, a table of connections (shaping source, what carried forward, evidence class, source), what the connections reveal, what remains distinctive, unanswered branches, and what changes for the current task. An abbreviated example is at the end of [`SKILL.md`](./step-back-understand/SKILL.md).

## Which step back?

- **Step Back Understand:** study what shaped a subject, even when nothing has gone wrong.
- **[Step Back Protocol](https://github.com/neonotics-png/step-back-protocol):** use `step-back-evaluate` to reframe stalled work and repeated failed approaches.

This skill stands alone; the recovery skill is not a dependency.

## Status

v1 procedure. Not yet behavior-tested across agent runtimes. Publishing or cloning this repository does not activate it in an agent runtime.

## License

[MIT](./LICENSE)
