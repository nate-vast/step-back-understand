# Understanding Pi 1.0

Pi is a coding agent built on a bet: give the model a tiny, stable core that it writes code against, and let everything else be code that you or the agent adds. Most of what Pi does, and nearly everything that changed in 1.0, follows from that. Earendil shipped 1.0 on October 1, 2026 (1.0.1 followed on October 3) and calls it "a hardened, minimal, extensible agent harness that you can make your own." The headline changes, native MCP through a feature called Codemode and a separate Pi Durable package, both look like reversals of the minimal approach. They are better read as ways to add capability without growing the core. (This is drawn from Earendil's and the original author's posts, the project site and coverage, not from running Pi myself.)

## Where it came from, and why that matters

Mario Zechner, best known for the libGDX game framework, wrote Pi in late 2025 because, in his words, Claude Code had "turned into a spaceship with 80% of functionality I have no use for." His other complaints shaped the design directly. The system prompt and tools changed with every release, which shifted model behavior under him. The harness injected context he couldn't see. The terminal flickered. Pi answers each of these. Its system prompt plus tool definitions come to under 1,000 tokens, so there is little hidden context to change. Its session format is documented so you can inspect every exchange. Its terminal UI redraws only what changed.

In April 2026 Zechner and Pi joined Earendil, the company of Armin Ronacher (creator of Flask). Ronacher had already written that Pi was the agent he used almost exclusively. Earendil's own stated aim is software that "strengthens human agency," which fits a tool built around user control rather than a vendor's choices.

## The core: four tools and a short prompt

By default the agent gets four tools: **read**, **write**, **edit** and **bash**. Grep, find and ls exist but are off by default, because the model can run them through bash anyway. The reasoning is that current models are already very good at using a shell and writing code. Every additional built-in tool costs context and becomes one more thing that can change under you.

The same reasoning explains what Pi deliberately leaves out, which its site lists openly:

- **No permission prompts.** Pi runs with full access. Zechner calls most agent permission systems "security theater," since an agent that can run code and reach the network can't be meaningfully fenced by pop-ups. If you want isolation, run Pi in a container, or build a confirmation step as an extension.
- **No plan mode or built-in to-dos.** Plans go in a PLAN.md or TODO.md that you and the model can both read and edit, so nothing lives in hidden harness state.
- **No built-in sub-agents.** You can have Pi launch other Pi instances (for example in tmux) or install an extension. Zechner's objection is that a sub-agent is a black box whose context you can't see.

## How you make it your own

The other half of the design is that Pi is meant to be changed. It has four layers:

- **Extensions** are TypeScript modules that can add tools, slash commands, keyboard shortcuts, event hooks and UI components, and can store state in the session.
- **Skills** are capability packages, mostly instructions plus scripts, loaded only when needed so they don't occupy context up front.
- **Prompt templates** are Markdown files you trigger with `/name`.
- **Packages** bundle all of the above and install from npm or git (`pi install npm:...`).

What sets Pi apart is that you usually don't download these: you ask the agent to write them. It edits an extension, you run `/reload`, and it's live in the same session. Ronacher's own setup is a handful of small commands he had Pi build for itself, such as `/review` (a fresh context for code review) and `/todos` (a shared to-do file). The four-tool core makes this practical, because a small, stable surface is easy for a model to build against.

Other features to know:

- **Session trees.** A session is stored as a tree in one file. `/tree` lets you go back to any point and branch, so a side quest, such as fixing a broken tool, doesn't clutter the main thread.
- **Many providers.** It supports 15+ providers (Anthropic, OpenAI, Google, Ollama and others) through Pi's own unified model library. You can switch models mid-session, and one session can mix providers.
- **Steering.** Enter sends a message that takes effect after the current tool call; Alt+Enter queues one for when the agent finishes.
- **Four ways to run it:** an interactive terminal UI; print/JSON mode for scripts (`pi -p "..."`); an RPC protocol over stdin/stdout; and an SDK for embedding.

The SDK point matters for context. Pi is built as separate layers (model access, agent loop, terminal UI, the CLI), and others build on the lower ones. The best-known example is OpenClaw, the personal agent that runs in chat apps, which embeds Pi rather than writing its own agent engine. Much of Pi's wider visibility came through that. Earendil says Pi now has "hundreds of thousands" of weekly users.

## What 1.0 changed

**MCP, through Codemode.** MCP (Model Context Protocol) is the standard for connecting agents to external tool servers. Pi's site used to state proudly that it had no MCP. The objection was about context. Zechner measured popular MCP servers taking roughly 7 to 9% of the context window before any work started. Ronacher added that MCP tools load at session start, which makes them hard to swap without breaking the prompt cache.

1.0 adds MCP as a core feature, but routes it through **Codemode**. Instead of putting every MCP tool's definition in front of the model, Codemode gives it one tool for writing a short JavaScript program, run by the harness, that calls the MCP tools. The model can then chain several calls, filter the results and return only the final output to its context. MCP servers can be set up so their tools are either *deferred* (loaded only when needed) or reachable only through Codemode. This addresses the context cost that kept MCP out, and it keeps the agent working the way Pi always assumed models work best: by writing code. Earendil also says MCP itself has matured. They want to influence its direction from inside, and they admit composability is still "the biggest issue."

**Virtual models.** Extensions can now define a "model" that is really a router. Earendil's example sends planning to Claude Opus, implementation to GPT, and lets Jev, a non-LLM model, decide when to switch. You select it like any model (`router/auto`). This builds on Pi's provider-neutral sessions.

**Smaller items:** full-screen terminal UI by default with a new theme; cache warming for Anthropic models; and mid-conversation system messages, so prompts and tools can change during a session based on what has happened in it. That last one bears on one of the original objections to dynamic tools: changing them used to mean disturbing the start of the session. Version 1.0.1 added per-project MCP config (`.pi/mcp.json`), MCP OAuth and a Nix flake.

Earendil frames "1.0" as months of hardening from user feedback into something "people and businesses can depend on." It hasn't published a formal stability or API guarantee, so don't assume extension APIs are frozen.

## Pi Durable is a different thing

Pi Durable shipped alongside 1.0. It is **not** a new version of the coding agent. It is an experimental TypeScript framework for building long-running agent applications, and it shares Pi's model library and design principles. The coding agent assumes one person in one terminal. Durable is for agents that run on a server, outlive crashes, handle very long conversations and accept input from several people at once. Each step saves a checkpoint to storage (SQLite, JSONL or memory), so a restarted process resumes where the last one stopped. Many conversations can run at once and fork from one another. Any number of clients can attach to a conversation and steer it. Earendil kept this separate precisely so the coding agent could stay minimal, and says lessons may flow back into Pi once proven. Its API may change.

## Getting started

Install with `curl -fsSL https://pi.dev/install.sh | sh` or `npm install -g @earendil-works/pi-coding-agent`. Both Pi and Pi Durable are MIT-licensed; code is at github.com/earendil-works/pi. Expect a bare tool at first. The intended path is to start with the four tools, notice what you keep wanting, and have Pi write that for you.

## References

- Earendil, "Pi 1.0": https://earendil.com/posts/pi-1-0/
- Earendil, "You said no MCP": https://earendil.com/posts/you-said-no-mcp/
- Earendil, "Pi Durable": https://earendil.com/posts/pi-durable/
- Mario Zechner, "What I learned building an opinionated and minimal coding agent": https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- Armin Ronacher, "Pi": https://lucumr.pocoo.org/2026/1/31/pi.md
- pi.dev, home page and 1.0.1 changelog: https://pi.dev/ , https://pi.dev/changelog/releases/1.0.1
