# Pi 1.0

Pi 1.0 is the first stable release of Pi, an open-source (MIT) coding agent for the terminal, shipped by Earendil on October 1, 2026. Its defining idea is a very small core that you, or the agent itself, extend. The release is best known for reversing Pi's most famous refusal: it now supports MCP, through a new mechanism called Codemode.

## What Pi is

Pi is an agent harness: the program that sends a language model your request plus a set of tools, runs the tools the model asks for, and loops until the work is done. It works with models from more than 15 providers, including local ones, and you can switch models mid-session.

By default the model gets four tools: `read`, `bash`, `edit` and `write`. Earendil says the system prompt and tool definitions together come to under 1,000 tokens. There is no plan mode, no sub-agents, no to-do list, no background shell and no permission prompts. For each of those the project's answer is a file, tmux, or an extension.

Three choices make that small core workable:

- **Extensions.** TypeScript modules loaded into the Pi process can register tools, commands, model providers, event hooks and UI. Pi can read its own documentation and write an extension for you, and `/reload` picks it up. Earendil counts more than 5,000 shared extensions.
- **Sessions as trees.** A session is a JSONL file in which every entry points to its parent, so you can rewind to any message and branch from it with `/tree`. Compaction adds a summary entry and leaves the original messages in the file.
- **One engine, four front ends.** The interactive terminal UI, a print/JSON mode for scripts, an RPC mode over stdin/stdout, and a TypeScript SDK all drive the same loop. The SDK is how OpenClaw embeds Pi.

## Why it is built this way

Mario Zechner wrote Pi in 2025 because Claude Code, which he liked when it was simple, had in his words "turned into a spaceship with 80% of functionality I have no use for," with prompts and tools that changed on every release and context injected where he could not see it. His rule was "if I don't need it, it won't be built." The bet behind it is that frontier models are already trained to behave as coding agents, so long prompts and many tools mostly cost tokens and hide what the model actually sees.

The missing permission prompts come from the same reasoning. Once an agent can write and run code, Zechner argued, per-command approval is security theater, so you should isolate the whole process instead. The 1.0 documentation still says this: tools run with your user's permissions, "project trust" only decides whether a folder's settings and extensions are loaded, and the recommended protection is a container or VM.

Earendil, a public benefit corporation founded by Armin Ronacher and Colin Daymond Hanna, acquired Pi in April 2026, and Zechner joined as a major stakeholder. Earendil's addition to the rationale is neutrality: a harness you own, that runs locally and talks to any model, keeps leverage with the user and away from the model vendor.

## What 1.0 added

| Addition | What it does |
|---|---|
| Codemode | The model writes a JavaScript script that calls Pi's tools and returns only the result |
| Native MCP | Connects to MCP servers over stdio or streamable HTTP, with OAuth sign-in |
| Classifier and image models | Scripts can run non-chat models such as TypeSafe's Jev |
| Virtual models | An extension registers a selectable "model" that routes each request to a real one |
| Deferred tool loading | Tools are declared to the model only after a search finds them |
| Mid-conversation system messages | Prompt and tool changes are appended to the transcript |
| Cache warming | Keeps a provider's prompt cache alive during long tool runs |
| Terminal UI | Fullscreen by default, with a theme built from your terminal's own colors |

Most of this landed in version 0.99.0 on September 29, when the version number jumped from 0.87. The 1.0.0 release itself made fullscreen the default and cut Codemode's prompt overhead by about 40%.

MCP and Codemode ship as built-in extensions that stay off until you configure an MCP server or enable them. With nothing configured, Pi 1.0 still starts with four tools.

## Codemode and the MCP reversal

Zechner's 2025 objections to MCP were specific. Servers put every tool description into the context on every session (he measured Playwright MCP at 21 tools and 13.7k tokens), and their results could not be piped into each other the way shell commands can. Command-line tools with a README had neither problem.

Codemode is Pi's answer to both. With the default setting, an MCP server's tools are not declared to the model at all. The system prompt gets a short section naming the server, and the model writes a script that finds tools with `searchTools()` and calls them as `tools.mcp__server__tool(args)`. The script can run calls in parallel, filter a large result, and return a few lines, so intermediate data never enters the context. Each server or tool can instead be set to `deferred`, `direct` (declared like a built-in tool) or `hidden`.

The script runs in a QuickJS sandbox inside the Pi process, with no file system, network or timers, and 256 MB of memory. Earendil chose the harness side deliberately: it is the trusted side, and values a script saves with `store()` live in the session transcript, so they follow branches and resumes. The sandbox contains the script and not the tools. A script that calls `tools.bash` has the full power of bash.

Earendil's post "You Said No MCP!" gives the reasons for the change. MCP has improved; Codemode removes the composition and context-cost objections; Pi needed the same sandbox anyway to run classifier models like Jev, which answer typed questions with probabilities and generate no text; and the team would sooner shape how MCP works in small harnesses than watch from outside. The post credits Codex with the same approach of exposing tools to a JavaScript sandbox.

## The cache features

Three of the additions exist because of how prompt caching is billed. Providers charge much less for a prompt prefix they have already processed, but only if that prefix is identical, and Anthropic's default cache expires after five minutes.

- **Deferred tool loading.** Adding a tool to the list at the top of a request changes the prefix and forces the whole conversation to be reprocessed. Newer Anthropic and OpenAI APIs let a tool be introduced at a point inside the transcript. Pi's `tool_search` uses those, and on other models falls back to resending the full list, which works but misses the cache.
- **Mid-conversation system messages.** The same idea applied to instructions. Pi records the initial prompt and tool set as the first system message and appends later changes, so they survive resume and branching and the cached prefix stays valid.
- **Cache warming.** If a test suite runs for seven minutes, the cache expires and the next request pays full price for the whole history. Pi sends a refresh during long tool runs when it estimates at least $0.05 in savings. Warming while idle is opt-in.

Virtual models follow the same discipline. A router can plan on an expensive model and implement on a cheap one, and the documentation recommends staying on one model within a turn because every switch costs a cache miss.

## Pi Durable

Pi Durable shipped the same day as a separate, experimental package. Pi the coding agent assumes one person, one terminal, and a process you restart by hand. Pi Durable is a framework for agents that must outlive their process: every model request and tool call is a checkpointed task, a new process resumes unfinished tasks from storage (memory, SQLite or JSONL), and several clients can watch and steer the same conversation. Earendil kept it separate so the coding agent stays small.

## Reception and caveats

The announcement reached the top of Hacker News with 1,689 points and 610 comments. The main criticisms were:

- **An uneven bar for "proven."** Jev had existed for about two weeks when Pi added support, while MCP waited nearly two years.
- **Eroding minimalism.** Critics pointed at cache warming and a fullscreen default in a "minimal" agent. The 2025 design had rejected fullscreen as well as MCP.
- **The TypeScript and Node footprint.**

Supporters said the small prompt is why Pi works well with local models, and that MCP removes a blocker for company use.

Some of the figures above have a single source:

- "Hundreds of thousands" of weekly users is Earendil's number, and commenters questioned it.
- The evidence that minimalism pays is a Databricks benchmark as quoted by Earendil: the same model cost more than twice as much in some harnesses, and Pi sent about a third of the context per turn.
- One MCP vendor measured a single task at 66K tokens through Codemode against 324K with tools declared directly.

## Trying it

```sh
curl -fsSL https://pi.dev/install.sh | sh
cd /path/to/project && pi
```

Run `/login` to connect a subscription or API key. The npm package `@earendil-works/pi-coding-agent` needs Node.js 22.19 or newer. Releases have been roughly weekly since 1.0, and the current version is 1.5.2 (November 10, 2026).

## Sources

- [Pi 1.0 announcement](https://earendil.com/posts/pi-1-0/), ["You Said No MCP!"](https://earendil.com/posts/you-said-no-mcp/), [Pi Durable](https://earendil.com/posts/pi-durable/), [Prompt Caching In Agents](https://earendil.com/posts/prompt-caching/), [Pi, Minimal and Performant](https://earendil.com/posts/pi-autoresearch-and-databricks/), [What is a Harness?](https://earendil.com/posts/what-is-a-harness/), [Announcing Pi & Lefos](https://earendil.com/posts/announcing-pi-and-lefos/) (Earendil)
- [Repository, release notes and v1.0.0 documentation](https://github.com/earendil-works/pi) and [pi.dev](https://pi.dev)
- [What I learned building an opinionated and minimal coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) and [What if you don't need MCP at all?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/) (Mario Zechner)
- [Pi: The Minimal Agent Within OpenClaw](https://lucumr.pocoo.org/2026/1/31/pi/) and [Mario and Earendil](https://lucumr.pocoo.org/2026/4/8/mario-and-earendil/) (Armin Ronacher)
- [Hacker News discussion of Pi 1.0](https://news.ycombinator.com/item?id=49926069)
- [Pi Codemode vs direct tool calls](https://www.withone.ai/blog/pi-codemode-one-mcp-server/md) (One)
- [Models Built to Do One Thing Well](https://www.deeplearning.ai/the-batch/models-built-to-do-one-thing-well) (DeepLearning.AI, on Jev)
