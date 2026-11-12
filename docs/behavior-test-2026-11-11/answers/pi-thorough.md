# Pi 1.0, explained

Pi 1.0 is the first stable release of Pi, an open-source terminal coding agent that ships with very little built in and expects you to extend it. Earendil released it on 1 October 2026 under the MIT license. The headline change is that Pi, which spent a year saying it would never support MCP, now has MCP in its core, reached through a new scripting sandbox called Codemode. A separate experimental package, Pi Durable, launched the same day.

## What Pi is

Pi is a "harness": the program that wraps a language model with a loop, tools and a terminal interface. It works with models from many providers, including local ones, and you can switch models mid-session.

- **Origin:** Mario Zechner (creator of libGDX) started it in August 2025 because he wanted a small, predictable agent whose context he controlled.
- **Owner:** Earendil, a public benefit corporation founded in 2025 by Armin Ronacher (creator of Flask) and Colin Daymond Hanna, acquired Pi in April 2026. Zechner joined and still leads its technical direction.
- **Core design:** Four default tools (`read`, `write`, `edit`, `bash`) and a system prompt that, with tool definitions, comes in under 1,000 tokens.
- **Left out on purpose:** Sub-agents, plan mode, permission prompts, to-do lists and background bash. You add these with extensions (TypeScript files), skills, prompt templates or packages from the Pi catalog, or you ask Pi to write them for you.
- **Ways to run it:** Interactive terminal, print/JSON mode for scripts and CI (`pi -p`), RPC over stdin/stdout, or embedded through the TypeScript SDK.

## What 1.0 changed

Most of the headline features landed in versions 0.86 to 0.99 over the preceding two weeks. The 1.0.0 release itself mainly made fullscreen the default and trimmed Codemode, so "Pi 1.0" in most coverage means the whole set.

| Feature | What it does |
|---|---|
| Codemode | The model writes a JavaScript script that calls tools, in parallel if it wants, and only the script's output returns to the model. |
| Native MCP | MCP servers are configured in `mcp.json` and reached mainly through Codemode. |
| Deferred tool loading | Tools stay out of the prompt until a `tool_search` call loads them. |
| Virtual models | An extension registers a "model" that is really a router picking a physical model per request. Marked experimental. |
| Cache warming | Pi refreshes a provider's prompt cache when it estimates the refresh is cheaper than a cache miss. |
| Mid-conversation system messages | Prompt and tool changes are appended to the conversation, not rewritten into earlier messages, so the prompt cache survives. |
| Fullscreen TUI by default | Set `tuiMode` to `"regular"` or pass `--tui-mode regular` to keep normal terminal scrollback. |

### Codemode and MCP

Codemode scripts run in a QuickJS sandbox with no file system, network, Node APIs or timers. A script reaches the outside world only by calling Pi's tools (`tools.<name>(...)`) and non-chat models such as classifiers and image generators. The point is context economy. In Earendil's own demo, a script rated the tone of 167 open issues from a Linear MCP server, and none of the intermediate results entered the conversation.

Codemode turns on automatically when you configure an MCP server. Without MCP, add it with `"defaultTools": ["+codemode"]`.

Each MCP server gets an exposure mode:

- **`codemode` (default):** tools are callable only from scripts and add nothing to the prompt.
- **`deferred`:** tools are declared to the model only after `tool_search` finds them.
- **`direct`:** tools are declared like built-in tools.
- **`hidden`:** tools are registered but unreachable.

Servers connect over stdio or streamable HTTP, with OAuth. Config lives in `~/.pi/agent/mcp.json` (user) and `.pi/mcp.json` (project, read only after you trust the folder). `--no-mcp` turns MCP off for one run.

Earendil's explanation for the reversal is that the MCP spec changed, and that models are now trained to orchestrate tools through code, so the harness should follow. Ronacher put it this way on Hacker News: "the answer is pretty disappointing: we look at what the models are doing."

## Pi Durable

Pi Durable is a separate TypeScript library for building long-running agent applications, such as a Slack bot or a shared assistant. It is not a replacement for the coding agent, and Earendil says its API may still change.

- **Crash survival:** Every model call and tool call is checkpointed, so an agent resumes after a crash, a sleeping laptop or a container restart.
- **Many conversations:** One harness runs many conversations in parallel, and forks share history without copying it.
- **Multiplayer:** Several clients can watch and steer the same conversation.
- **Storage and runtime:** Memory, SQLite or JSONL storage, on Node, Bun or Cloudflare Durable Objects. One process owns a storage at a time.
- **Size:** About 15,000 lines without tests, kept small so an agent can read and modify it.

## Trying it

```sh
# macOS / Linux
curl -fsSL https://pi.dev/install.sh | sh

# Windows
powershell -c "irm https://pi.dev/install.ps1 | iex"

# npm (needs Node.js 22.19+)
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
```

Then `cd` into a project, run `pi`, use `/login` to connect a subscription or API key, and give it a task. Pi itself is free; you pay for the model.

## What to know before relying on it

- **No guardrails by default.** Pi runs with your account's permissions and does not ask before tool calls. Its own docs say project trust and diff review are not security boundaries, and recommend a container or VM for untrusted or unattended work. The Codemode sandbox confines only the script; any tool the script calls keeps its full reach.
- **It still moves fast.** There have been 11 releases since 1.0.0, reaching 1.5.2 on 10 November, and 1.5.0 and 1.5.1 both contained breaking changes.
- **The efficiency numbers are mostly the vendor's.** Earendil reports Codemode's own prompt cost fell about 40% in 1.0. The one outside test I found (single runs, by a company selling an MCP server) measured 66,200 tokens with Codemode against 324,426 with direct tool calls on the same task. It also found the Codemode script silently dropped three deleted items, and that Codemode adds roughly 4,300 tokens of fixed overhead, so it does not pay off for one or two small calls.
- **The adoption claim is unverified.** Earendil says "hundreds of thousands" use Pi weekly. What can be checked: about 121,000 GitHub stars and about 6.3 million npm downloads in the past week, a figure that includes CI runs and embedded SDK use.
- **Licensing has an asterisk.** Earendil says the core "remains MIT licensed and that will not change", but that some add-ons may be Fair Source or proprietary.

## How it was received

The launch post reached 1,689 points and 610 comments on Hacker News. Users praised the small prompt, especially for local models, and the fact that Pi is vendor-neutral. The main objections were:

- **Minimalism drift:** MCP, Codemode and a fullscreen default contradict the things Pi originally refused to build. Zechner replied that every addition is optional and that scrollback mode "is definitely not going away."
- **Uneven bar for "proven":** MCP waited almost two years, while support for Jev, a classifier model released in September, arrived within weeks.
- **Footprint:** Commenters questioned calling a large Node.js codebase with an npm dependency tree "minimal."

## Sources

- [Pi 1.0 announcement](https://earendil.com/posts/pi-1-0/), [You Said No MCP!](https://earendil.com/posts/you-said-no-mcp/), [Pi Durable](https://earendil.com/posts/pi-durable/), [Pi Durable on Cloudflare](https://earendil.com/posts/pi-durable-on-cloudflare/) (Earendil)
- [Pi changelog](https://pi.dev/changelog), [1.0.0 release notes](https://pi.dev/changelog/releases/1.0.0), [0.99.0 release notes](https://pi.dev/changelog/releases/0.99.0)
- Pi docs: [Codemode](https://pi.dev/docs/latest/codemode), [MCP](https://pi.dev/docs/latest/mcp), [Virtual models](https://pi.dev/docs/latest/virtual-models), [Security](https://pi.dev/docs/latest/security), [Settings](https://pi.dev/docs/latest/settings), [Quickstart](https://pi.dev/docs/latest/quickstart)
- [Pi licensing, RFC 0015](https://rfc.earendil.com/0015) and [acquisition announcement](https://earendil.com/posts/announcing-pi-and-lefos/)
- [Mario Zechner's original design post](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [Hacker News: Pi 1.0](https://news.ycombinator.com/item?id=49926069) and [Pi Durable](https://news.ycombinator.com/item?id=49925969)
- [GitHub repository](https://github.com/earendil-works/pi)
- Coverage: [Trending Topics](https://www.trendingtopics.eu/pi-1-0-earendil-en/), [Techzine](https://www.techzine.eu/news/devops/144715/pi-1-0-will-include-mcp-and-a-dedicated-layer-for-long-running-ai-agents/), [eesel](https://www.eesel.ai/blog/pi-coding-agent), [Developers Digest](https://www.developersdigest.tech/blog/pi-1-0-release-guide-mcp-codemode-pi-durable), [One's Codemode measurement](https://www.withone.ai/blog/pi-codemode-one-mcp-server/md)
