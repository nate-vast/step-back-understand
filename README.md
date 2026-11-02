# Step Back Understand

**To understand a thing, study the things that made it what it is.**

An explicitly invoked agent skill for understanding a person, work, idea, product, or system through the influences, foundations, ingredients, and conditions that shaped it.

## The loop

1. Inspect the subject itself.
2. Identify what shaped it.
3. Study those sources—not merely their names.
4. Trace further back where it improves understanding.
5. Return to the original subject and explain what the connections reveal.

Depth is flexible. Deeper understanding can be the result; it does not have to justify an immediate action. Connections require evidence: resemblance alone does not prove influence.

## Install

Clone this repository:

```sh
git clone https://github.com/neonotics-png/step-back-understand.git
```

Copy the included [`step-back-understand`](./step-back-understand) directory into your agent's skill directory. Discovery paths differ by runtime. The portable entry point is [`SKILL.md`](./step-back-understand/SKILL.md).

## Invoke

```text
Use step-back-understand to explore what shaped [subject].
```

For example:

```text
Use step-back-understand to understand a musician's style through
the artists, traditions, collaborators, and experiences that shaped it.
Study their relevant work and establish evidence for the connections.
```

The result should explain the subject through concrete shaping connections, with sources attached to claims and uncertainty made explicit.

## Which step back?

- **Step Back Understand:** study what shaped a subject, even when nothing has gone wrong.
- **[Step Back Protocol](https://github.com/neonotics-png/step-back-protocol):** use `step-back-evaluate` to reframe stalled work and repeated failed approaches.

This skill stands alone; the recovery skill is not a dependency.

## Status

Initial v1 procedure. Not yet behavior-tested across agent runtimes. Publishing or cloning this repository does not activate it in an agent runtime.
