# Understanding Pi 1.0

Pi 1.0 (October 1, 2026) is the first stable release of Pi, an MIT-licensed terminal coding agent that Earendil calls a "minimal agent harness." The core is four tools (read, write, edit, bash), a very short system prompt, and an extension system for everything else. Most of 1.0 is hardening. The new features look unrelated, but nearly all of them serve one goal: keep what the model sees small, cheap and under your control.

**The minimal core.** Mario Zechner built Pi in 2025 as a reaction to Claude Code, which he said had "turned into a spaceship with 80% of functionality I have no use for" and kept changing its prompt and tools under him. His rule was "if I don't need it, it won't be built." That is why the 1.0 site still has a "what we didn't build" list: no sub-agents, no plan mode, no to-dos, no background bash, no permission popups. The suggested replacements are tmux, plain files, a container, or an extension you write or install. If you come from Claude Code, expect those gaps to be deliberate, and expect Pi to run with full access unless you sandbox it yourself.

**Codemode, and the MCP reversal.** This is the headline. Pi refused MCP for a year because MCP servers load every tool definition into context (Zechner measured about 13.7k tokens for Playwright's server), where a command-line tool costs nothing until it is used. Pi 1.0 has MCP built in, but by default MCP tools are not shown to the model at all. Instead the model gets one tool, `codemode`, and writes a JavaScript script that searches for the tools it needs, calls them in parallel, filters the results, and returns only the final output. The script runs in a QuickJS sandbox with no file system or network. So the reversal keeps the original objection intact: MCP is allowed in because it no longer costs context.

The idea has a clear history. Cloudflare's "Code Mode" (September 2025) argued that models are better at writing code than at emitting tool calls, and that code lets them chain calls without passing every intermediate result back through the model. Earendil co-founder Armin Ronacher had argued a month earlier that an MCP server should be one tool that accepts code. Earendil's own post credits neither and mentions only that Codex does something similar, so treat the Cloudflare link as a strong resemblance. Earendil also says plainly that MCP is still "hard to compose" and that it adopted the protocol in order to influence it.

Each server or tool can be set to one of four exposures: `codemode` (the default), `deferred` (found through a `tool_search` tool and loaded on demand), `direct` (declared like a built-in) or `hidden`. If you configure no MCP servers, codemode stays off and Pi is still the four-tool agent.

**Models as parts.** Scripts and extensions can call non-chat models: image generators, and classifiers such as Jev, a model from TypeSafe launched in September 2026 that returns typed answers with probabilities instead of text. Extensions can also define "virtual models." Earendil's demo has Pi write itself a router that plans with Claude Opus, implements with a GPT model, and uses Jev to decide when to switch.

**Cache economics.** Two quieter features follow from the same concern with context. Prompt and tool changes are appended to the transcript as messages instead of rewriting the top of the prompt, so the provider's prompt cache survives. Cache warming keeps an Anthropic cache alive between runs, for up to 30 idle minutes, and only when Pi estimates it saves at least $0.05. Some Hacker News commenters thought this belonged in a plugin, not a minimal core.

**Fullscreen by default.** Pi originally wrote into your terminal's normal scrollback on purpose. Fullscreen arrived as an experiment in 0.84 and is now the default; `tuiMode: "regular"` restores the old behavior. I did not find the maintainers' stated reason. The docs show fullscreen lets Pi own scrolling and mouse input.

**Pi Durable.** People were already building other agents on Pi (OpenClaw is the one that made Pi widely known). Instead of growing the coding agent, Earendil shipped a separate experimental package for long-running agents: every model and tool call is a checkpointed task, state lives in SQLite or JSONL, a crashed process resumes where it stopped, and several clients can steer one conversation. It is about 15,000 lines of TypeScript and its API may change.

**Who is behind it, and how it landed.** Earendil acquired Pi in April 2026 and Zechner joined as a stakeholder. He has committed to the core staying MIT, with paid add-ons and enterprise features planned around it. The launch drew roughly 1,700 points and 600 comments on Hacker News. Praise centered on the small prompt, which helps local models. Criticism centered on Pi "abandoning the minimality philosophy," uneven extension quality, and the fullscreen change. The "hundreds of thousands" of weekly users is Earendil's own figure.

**Sources**

- [Pi 1.0 announcement, Earendil](https://earendil.com/posts/pi-1-0/)
- ["You Said No MCP!", Earendil](https://earendil.com/posts/you-said-no-mcp/)
- [Pi Durable announcement, Earendil](https://earendil.com/posts/pi-durable/)
- Pi docs: [releases](https://pi.dev/news/releases), [codemode](https://pi.dev/docs/latest/codemode), [MCP](https://pi.dev/docs/latest/mcp), [settings](https://pi.dev/docs/latest/settings), [homepage](https://pi.dev/)
- [Mario Zechner on building Pi (2025)](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) and [on joining Earendil (2026)](https://mariozechner.at/posts/2026-04-08-ive-sold-out/)
- [Cloudflare, "Code Mode: the better way to use MCP"](https://blog.cloudflare.com/code-mode/)
- [Armin Ronacher, "Your MCP Doesn't Need 30 Tools: It Needs Code"](https://lucumr.pocoo.org/2025/8/18/code-mcps/)
- [Hacker News discussion](https://news.ycombinator.com/item?id=49926069)
