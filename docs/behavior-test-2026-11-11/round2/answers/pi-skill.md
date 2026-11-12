# Understanding Pi 1.0

Pi is an open-source (MIT) coding agent that runs in your terminal. You give it a model, it reads and edits your code and runs commands, and you talk to it the way you would talk to Claude Code or Codex. What sets it apart is that it is built to stay small and be rewritten by its user. Earendil's own description is "a hardened, minimal, extensible agent harness that you can make your own." Pi 1.0 shipped on 1 October 2026. Earendil says it has hundreds of thousands of weekly users.

The quickest way to understand Pi is to read it as a deliberate counter-design to Claude Code. Most of its choices, including the late arrival of MCP, follow from that.

(I haven't run Pi myself. This is based on Earendil's release posts, the changelog, the docs and the creator's own writing.)

## Where it came from

Mario Zechner, known for the libGDX game framework, built Pi in 2025 under the name pi-mono. He had been a heavy Claude Code user and wrote down why he stopped: it had become "a spaceship with 80% of functionality I have no use for." Its system prompt and tools changed with every release, which "breaks my workflows and changes model behavior." Worst of all, harnesses like it inject context "behind your back that isn't even surfaced in the UI." His rule for Pi was blunt: "if I don't need it, it won't be built."

In April 2026, Zechner joined Earendil, the public benefit company co-founded by Armin Ronacher (creator of Flask) and Colin Daymond Hanna, and Pi came with him. Coverage says he remains a major stakeholder and still leads Pi's technical direction. The repository moved from `badlogic/pi-mono` to `earendil-works/pi`, and the license stayed MIT. Ronacher framed the move as stewardship, not a pivot: the goal is for Pi "to continue to exist as a high-quality, open, extensible piece of software."

So 1.0 is the first release under a company, but it carries one person's year-old design philosophy. That explains why the release is so restrained.

## How it works: a small core you can see all of

**Four tools and a tiny prompt.** By default the model gets `read`, `write`, `edit` (exact text replacement) and `bash`. Read-only `grep`, `find` and `ls` exist but start disabled. Zechner measured the system prompt plus tool definitions at under 1,000 tokens. His reasoning is that frontier models have been trained so heavily on agentic coding that they "inherently understand what a coding agent is," so a long prompt mostly costs context and adds behavior you didn't ask for. The tool set is close to Codex's minimal one, which he noted himself. It differs sharply from Claude Code's, where the prompt is long and changes between releases.

**You control the context.** Project instructions come from `AGENTS.md` files, loaded from `~/.pi/agent/`, parent directories and the current directory. A `SYSTEM.md` can replace or extend the default prompt for a project. When the context window fills, compaction summarizes older messages, and extensions can override it. Nothing else is injected silently. That is the core promise, and it answers the hidden-injection complaint above.

**No permission prompts.** Pi runs with your user's full permissions. Zechner calls most agents' approval dialogs "security theater": an agent that can read private data, execute code and reach the network can't be made safe by clicking "allow." His answer is to isolate it properly, and the docs describe container setups. If you want approvals anyway, you build or install an extension for them.

**Sessions are trees.** Each session is one file holding a branching history. `/tree` jumps to an earlier point and branches from there, and you can label entries as bookmarks. `/export` writes HTML, and `/share` posts to a gist. This follows from Zechner's wish for a "cleanly documented session format" he could inspect and post-process.

**Steering while it works.** Pressing Enter mid-run sends a steering message. It is delivered after the current tool call, and the remaining tool calls are skipped. Alt+Enter queues a follow-up that waits until the agent finishes.

**Any model, switchable mid-session.** Pi sits on `pi-ai`, its own multi-provider LLM layer. Zechner built directly on the provider SDKs instead of the Vercel AI SDK because tool calling with self-hosted models kept breaking. The docs list 15+ providers, including Anthropic, OpenAI, Google, Bedrock, Mistral, Groq, Ollama and OpenRouter. You can change models partway through a conversation, and Pi converts the history between providers' formats as well as it can.

**Four ways to run it.** Interactive TUI, print/JSON mode for scripts, an RPC protocol over stdin/stdout, and a TypeScript SDK. The SDK is why Pi matters beyond its own users: OpenClaw, the popular personal-assistant agent, uses Pi as its engine.

## What it leaves out, and what you do instead

Pi skips features its rivals advertise. The reasons are specific:

- **Sub-agents:** Zechner calls Claude Code's sub-agents "a black box within a black box." Pi can start another Pi through bash or tmux, and then you can see its output.
- **Plan mode:** write the plan to a `PLAN.md` you can read, edit and commit.
- **To-do lists:** built-in to-dos "confuse models more than they help." Use a `TODO.md` instead.
- **Background bash:** use tmux, which you can attach to and watch.

Each of these can be added back as an extension. Pi's example list includes sub-agents, plan mode, permission gates and sandboxing. The point is that you choose to add them, and you can read the code that does.

## Extensions: the agent edits itself

Customization is the main feature, not a side one. Extensions are TypeScript modules with access to tools, commands, keybindings, events and the TUI. Skills are instruction packages loaded on demand. Prompt templates are Markdown files you call with `/name`. Themes complete the set. Any of these can be bundled into a Pi package and installed from npm or git (`pi install npm:...`). The intended loop is to ask Pi to write the tool or command you want, run `/reload`, and keep going. Pi "will customize itself on the fly." This resembles Emacs, where the editor is mostly user code. The makers don't make that comparison; it's mine.

## What 1.0 actually adds

**MCP, through Codemode.** This is the headline change, and a reversal. In November 2025, Zechner wrote that Pi would not support MCP. His reason was cost: MCP servers put every tool description into context on every turn, about 13.7k tokens for Playwright's and 18k for Chrome DevTools'. His alternative was CLI tools with READMEs the agent reads only when needed. Earendil's 29 September post ("You Said No MCP!") explains the change of mind. MCP itself had changed. The real problem was that tools didn't compose, and the work needed to fix that was useful anyway.

Codemode is that fix. Instead of calling tools one at a time through the conversation, the model writes a short JavaScript script that calls them, in any order or in parallel. The script runs in a sandbox on the harness side, and only its final result enters the context. Intermediate tool output never reaches the model, and tools can be marked deferred so they are discovered only when needed. Earendil's demo pulled 167 open Linear issues through Linear's MCP server and ran each through Jev, a non-LLM classifier model. The result came back as one summary (156 neutral, 11 mildly frustrated) instead of 167 tool results in context.

The idea isn't unique to Pi. Earendil names OpenAI Codex's JavaScript tool sandbox as precedent. The design also closely matches Cloudflare's "Code Mode" and Anthropic's "code execution with MCP" posts from 2025. Both turn MCP tools into a code API and keep intermediate results inside the execution environment. Earendil doesn't cite those two, so treat that link as a resemblance. The comparison still tells you what to expect: Codemode pays off most when a task chains many tool calls or filters a lot of data, and it saves little on a single lookup.

MCP servers are configured in a global or per-project `mcp.json` (project config only after you trust the project), or by extensions. They are managed with `/mcp` and `pi mcp add|list|login`. Both stdio and HTTP transports with OAuth are supported. The changelog reports that Codemode now uses about 40% fewer prompt tokens: one GPT-5.6 request went from about 5,300 to 3,300 tokens. That is Earendil's own figure, not an independent benchmark.

**Smaller additions.** Extensions can define virtual models, such as a `router/auto` model that plans with Claude Opus and implements with GPT. Tool loading can be deferred. There is cache warming for Anthropic models, and the prompt and tools can change mid-conversation. The TUI now runs fullscreen by default (`tuiMode: "regular"` brings back normal scrollback) and has a new theme. Breaking changes are minor: scripts must test `"name" in tools` instead of `typeof tools.name`, and `--provider` without `--model` is now an error.

**Pi Durable (experimental, separate).** People wanted to reach Pi from other surfaces and run long tasks. Rather than add that to the coding agent, Earendil shipped a separate npm package, `@earendil-works/pi-durable`. It is a runtime for long-running conversations, tasks and documents that survives crashes. It is explicitly not a replacement for the coding agent, so expect its API to change.

## How to think about it

Pi isn't trying to beat Claude Code on features. It is a small, readable, model-agnostic base that you shape yourself. The 1.0 release shows how it grows: an idea gets added only after it has proven itself elsewhere, in a form that keeps the context lean. MCP got in only once Codemode stopped it from flooding the context. The trade-off is that the safety, planning and orchestration other agents ship with are yours to set up, through containers, files, tmux or extensions. Pi suits you if you want to see and control everything the model sees. If you want those features ready out of the box, it's the wrong tool.

Install: `curl -fsSL https://pi.dev/install.sh | sh` (or npm `@earendil-works/pi-coding-agent`, Node 22.19+), then `/login` inside Pi.

## References

- Earendil, "Pi 1.0" (1 Oct 2026): https://earendil.com/posts/pi-1-0/
- Earendil, "You Said No MCP!" (29 Sep 2026): https://earendil.com/posts/you-said-no-mcp/
- Pi 1.0.0 changelog: https://pi.dev/changelog/releases/1.0.0
- Pi homepage and docs: https://pi.dev and https://github.com/earendil-works/pi
- Mario Zechner, "What I learned building an opinionated and minimal coding agent" (30 Nov 2025): https://www.mariozechner.at/posts/2025-11-30-pi-coding-agent/
- Armin Ronacher, "Mario and Earendil" (8 Apr 2026): https://lucumr.pocoo.org/2026/4/8/mario-and-earendil/
- Anthropic, "Code execution with MCP": https://www.anthropic.com/engineering/code-execution-with-mcp
