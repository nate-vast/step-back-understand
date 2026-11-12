# Pi 1.0: what it is, how it works, and why it looks the way it does

## The short version

Pi is an open-source (MIT) coding agent for the terminal. It is also a set of libraries you can build your own agents on. Mario Zechner, the creator of libGDX, wrote it in 2025. In spring 2026 he and the project moved to Earendil, the company Armin Ronacher (creator of Flask) co-founded. Earendil shipped Pi 1.0 on **October 1, 2026**. The official changelog gives that date; some press reports say October 2 to 4. Earendil calls it a "hardened, minimal, extensible agent harness that you can make your own." It works with models from every major provider, plus any OpenAI-compatible endpoint.

The headline change in 1.0 is **Codemode**, a JavaScript sandbox inside the harness. With it, Pi gets **native MCP support**, which it had refused to add before. An experimental sibling package, **Pi Durable**, came out alongside it for long-running, crash-safe agent applications.

## How Pi works

**Four layered packages.** The original design splits Pi into:
- `pi-ai`, a single LLM API across providers that handles streaming, tool calls, reasoning, cost tracking and aborts;
- `pi-agent-core`, the agent loop: call the model, run the tools it asks for, repeat until it stops;
- `pi-tui`, a terminal UI framework;
- `pi-coding-agent`, the CLI that ties them together with sessions, themes and project context.

You can use the lower layers on their own. That is how OpenClaw, the viral personal-agent project, is built: it embeds Pi's SDK and swaps in its own versions of the core tools.

**A tiny core.** By default the model gets four tools: `read`, `write`, `edit` and `bash`. Read-only `grep`, `find` and `ls` exist but are off by default. The system prompt plus tool definitions originally came to under about 1,000 tokens. Pi appends only your `AGENTS.md` files (global and per-project), and you can replace the whole prompt. It runs "YOLO" by default: no permission prompts and full filesystem access. Zechner's argument is that once an agent can run code and reach the network, in-harness permission prompts are mostly security theater. If you want isolation, run Pi in a container.

**What it leaves out on purpose.** Zechner's original design post lists the omissions, each with a reason:
- No built-in to-do tool: models get confused tracking hidden state, so a `TODO.md` file does the job.
- No plan mode: you plan in conversation and keep the result in `PLAN.md`.
- No background bash: long processes go in tmux, where both you and the agent can watch them.
- No sub-agents: they are opaque and hand over context poorly. Pi can run itself through bash with `pi --print` instead.
- Until 1.0, no MCP.

**Sessions.** Sessions are saved in a documented format you can post-process. They can be continued, resumed, branched into a tree and exported to HTML. One session can hold messages from several providers. For example, Anthropic thinking traces become tagged text when you switch to an OpenAI model mid-session. Sessions can also store custom entries that the model never sees, and extensions use these to persist their state.

**Extensions.** This is how Pi grows. Extensions are TypeScript modules that can register tools the model can call, add slash commands, hook lifecycle events and draw custom TUI components. They hot-reload, and Pi ships docs and examples aimed at the agent. The intended workflow is to ask Pi to write the extension you need, then reload, test and iterate in the same session. Ronacher says none of his own extensions (`/review`, `/todos`, `/answer`, `/files` and others) were written by hand. By May 2026 there were reportedly over 2,000 third-party extensions and more than 45,000 GitHub stars. Those are third-party counts, not audited.

## What 1.0 adds

- **Codemode.** The model writes short JavaScript scripts that call tools in any order or in parallel and combine their results in code. Intermediate results stay out of the model's context. Codemode runs where the harness loop runs, not where `bash` runs. Its state lives in the session transcript, not on disk. It loads automatically when MCP is configured, or you can enable it as a default tool. Scripts can also call non-LLM models, such as Earendil's Jev decision model and image generators (`models.generateImages()`). The 1.0 changelog says Codemode's prompt overhead fell about 40%; in one GPT-5.6 example a request dropped from about 5,300 to about 3,300 tokens.
- **Native MCP.** Servers can run over stdio or streamable HTTP, with OAuth. You configure them in `mcp.json` (global, or per project once the project is trusted) or with `pi.registerMcpServer()`, and manage them with `/mcp` or `pi mcp add|remove|list|login|logout`. OAuth was hardened with per-server credentials, RFC 9207 `iss` checks, and step-up sign-in that keeps scopes you already granted.
- **Deferred tool loading.** A tool can be hidden from the model until it is needed and found through `tool_search`. It can also be exposed only inside Codemode.
- **Virtual models.** An extension can present a router as if it were a model. Earendil's demo builds `router/auto`: Claude Opus plans, GPT implements, and Jev decides when to switch. `/session` then shows cost and cache use per model.
- **Mid-conversation system messages**, so prompt and tool changes can take effect partway through a session.
- **Cache warming** for Anthropic models.
- **Fullscreen TUI by default**, with a new theme.

**Upgrade gotchas:**
- The fullscreen default replaces normal terminal scrollback. Set `tuiMode: "regular"` or pass `--tui-mode regular` to get it back.
- Codemode scripts that test for a tool with `typeof tools.x` must switch to `"x" in tools`.
- `--provider` without `--model` now errors instead of silently picking another provider's default model.
- Stored MCP credentials are now keyed by server name plus URL.

Install with `curl -fsSL https://pi.dev/install.sh | sh` on macOS and Linux, or `powershell -c "irm https://pi.dev/install.ps1 | iex"` on Windows.

## Why it is this way

Pi's shape comes mostly from one stance: **you should know exactly what goes into the model's context.** Earendil's version is that it adds a feature only "after it has proven itself," because many agent-tooling trends fade fast. Several specific features trace back to particular influences:

- **The tiny, stable prompt and the lack of hidden injection** react to Claude Code. Zechner moved to Claude Code in 2025 and grew frustrated with it. System prompts and tools changed under him from release to release, the harness injected context he couldn't see, and the terminal output flickered. That is why Pi publishes its prompt, keeps it small, lets you replace it, and builds its own differential-rendering TUI. Zechner also pointed to Terminus 2, a bare tmux-only agent that scores competitively on Terminal-Bench, as evidence that a small harness doesn't cost capability.
- **The fullscreen default reverses an early choice.** `pi-tui` originally wrote into the terminal's native scrollback to keep native scrolling and search. In 1.0, fullscreen is the default and the old behavior is the `regular` mode.
- **The long refusal of MCP, and then Codemode,** form one story. Zechner's 2025 post "What if you don't need MCP?" argued that MCP servers cost a lot of context; he cited Playwright MCP at about 13.7k tokens of tool definitions. CLIs with READMEs, which the agent reads only when needed, compose better. Ronacher added a caching point: providers load MCP tool definitions at session start, so reloading tools breaks the cache and confuses the model. Pi users reached MCP through adapters like mcporter instead. Earendil's 1.0 post, titled "You Said No MCP!", explains the reversal:
  - the protocol has changed ("the MCP of today is not the MCP of yesteryear");
  - Pi needed a sandboxed interpreter anyway for Jev and similar work;
  - a plain MCP extension didn't carry enough metadata to decide which tools the model sees directly and which only the sandbox sees.

  Codemode is how Pi answers its own objection. Tools are deferred or kept sandbox-only, so they stop flooding the context. The model chains them in JavaScript the way it chains CLIs with shell pipes, which Earendil compares to Codex's approach. Earendil chose JavaScript partly because small builds can ship as WASM binaries with reasonable isolation. The broader position is that MCP should be "much closer to OpenAPI with intelligent tool discovery": structured data, discoverable from descriptions. Earendil also says "the best way to positively influence something is to embrace it."
- **Deferred tools and mid-conversation system messages** exist because recent models support deferred loading, changing system messages mid-run and changing reasoning levels. Pi's tool setup hadn't caught up with those abilities until 1.0.
- **Extensions that the agent writes and hot-reloads, plus SDK layering,** come from the premise Pi shares with OpenClaw: LLMs are good at writing and running code, so let the agent build what it needs rather than install other people's plugins.
- **Pi Durable is a separate package** so the coding agent itself stays minimal.

## Pi Durable, briefly

Pi is built for one person in a terminal. Pi Durable is an experimental library (about 15k lines, MIT) for agent applications that run for a long time and may be steered by several people. It runs on any JavaScript runtime, including Bun and Cloudflare Durable Objects. It installs via `npm install @earendil-works/pi-durable @earendil-works/pi-ai @earendil-works/chord`.

- **Crash recovery.** Every step is checkpointed, so an agent survives crashes, a sleeping laptop or a restarted container. A tool call that was cut off reruns only if it is safe to; otherwise the model is told it was interrupted. Zechner describes it as an "intent, execution, result" pattern rather than event sourcing.
- **Conversations.** Many conversations can run in parallel, and compaction runs in the background. Pi's per-entry session tree is replaced by flat conversations that can fork from entries in other conversations.
- **State.** App state is stored as versioned JSON documents with an Immer-like draft API. `requestId` idempotency keys support exactly-once submission.
- **Sandboxes are pluggable**, one per conversation if you want; Earendil's VM-based Gondolin is one option.

Expect the API to change. Commenters on Hacker News questioned how external state, like a browser or a VM, stays consistent after a crash, and whether an ID alone gives true exactly-once behavior.

## Context

- **Earendil** was founded by Armin Ronacher and Colin, formerly of Balderton. Reports give his surname as either Sidoti or Daymond Hanna, so check before citing it. Backers reportedly include Accel and Balderton, plus founders of n8n, OpenClaw, Revolut, Sentry and Slack. Its stated mission is "software and open protocols that strengthen human agency."
- **The Pi deal.** Reports call it either an acquisition or Zechner joining as a shareholder. Zechner's own post is titled "I've sold out." Either way, he still leads Pi's technical direction. Earendil says the core stays open and that it will sell paid add-ons and cloud services. Its email-based agent platform, Lefos, sits alongside Pi.
- **Adoption.** Earendil claims "hundreds of thousands" of weekly users; this is not independently verified. Much of Pi's visibility comes from being the engine inside OpenClaw. The 1.0 post passed 1,000 points on Hacker News.
- **Concerns.** Some developers worry that venture backing, or a future acquirer, could erode Pi's provider neutrality. Others note that the project now ships features it once rejected on principle.

## Sources

- [Earendil: Pi 1.0 announcement](https://earendil.com/posts/pi-1-0/)
- [Earendil: "You Said No MCP!"](https://earendil.com/posts/you-said-no-mcp/)
- [Pi 1.0.0 changelog](https://pi.dev/changelog/releases/1.0.0)
- [Mario Zechner: What I learned building an opinionated and minimal coding agent (Nov 2025)](https://www.mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [Mario Zechner: What if you don't need MCP?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/)
- [Armin Ronacher: Pi (Jan 2026)](https://lucumr.pocoo.org/2026/1/31/pi/)
- [Armin Ronacher: Mario and Earendil (Apr 2026)](https://lucumr.pocoo.org/2026/4/8/mario-and-earendil/)
- [Trending Topics: Pi 1.0 coverage](https://www.trendingtopics.eu/pi-1-0-earendil-en/)
- [Developers Digest: Pi 1.0 release guide](https://www.developersdigest.tech/blog/pi-1-0-release-guide-mcp-codemode-pi-durable)
- [Hacker News discussion of Pi Durable / 1.0](https://news.ycombinator.com/item?id=49925969)
- [GitHub: earendil-works/pi](https://github.com/earendil-works/pi)
