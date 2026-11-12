# Pi 1.0 comprehension quiz: answer key

Scoring: 2 / 1 / 0 points per question, 16 points total. Facts checked on 2026-11-11 against the sources listed under each question. Docs links point at the `v1.0.0` tag, so they describe 1.0 as released (GitHub release `v1.0.0`, published 2026-10-01).

Question types: 1-3 how it works, 4-5 why it is designed this way, 6-7 context, 8 application.

---

## 1. One turn of the agent loop (how it works)

**Model answer.** Pi adds the message to the active branch of the session, builds a model request from the system prompt, the active branch, the available tools and the model settings, and sends it through the selected provider. The provider streams back an assistant response that can contain text and tool calls; Pi records the response, executes each tool call and records the results, which completes one turn. The history comes from the active branch of the session tree (sessions are JSONL files whose entries each point at a parent). Another turn starts only if tool results or queued messages require another model request; otherwise the run ends.

**Rubric.**
- 2: Describes the cycle (build request, model response with tool calls, Pi executes the tools and records results), says the history comes from the session's active branch, and says the loop continues only while tool results or queued messages need another model request.
- 1: Gets the request / tool call / result cycle right but leaves out either where history comes from or the stopping condition, or is vague on one of them.
- 0: Describes a single request and response with no tool execution, or says the model itself runs the tools, or is otherwise wrong.

**Sources.**
- https://github.com/earendil-works/pi/blob/v1.0.0/packages/coding-agent/docs/how-pi-works.md (sections "Agent loop", "Context", "Sessions")

---

## 2. What Codemode is (how it works)

**Model answer.** Codemode is a tool that lets the model write a JavaScript script which calls Pi's other tools (and non-LLM models such as classifiers and image models) instead of issuing each call as a separate model turn. The script runs on the harness side, in a QuickJS sandbox with no Node APIs, file system, network or timers, so it can reach the outside world only through `tools.<name>()` and `models`. Only the script's output goes back to the model, so the script can run calls in parallel and filter or aggregate large results before the model sees them. Tool calls made by a script are real and are not undone if the script later fails.

**Rubric.**
- 2: Says it is model-written JavaScript that orchestrates tool calls, that it runs in a restricted sandbox (QuickJS, or "no file system / network, only tool calls") in the harness, and that only the script's output reaches the model's context.
- 1: Has the general idea (a script that batches or composes tool calls) but misses either the sandbox limits or the "only the output reaches the model" point.
- 0: Describes it as a coding mode, a plan mode, a way to run arbitrary Node or shell code, or anything else that is not tool orchestration.

**Sources.**
- https://github.com/earendil-works/pi/blob/v1.0.0/packages/coding-agent/docs/codemode.md
- https://lucumr.pocoo.org/2026/10/6/codemode/ (Armin Ronacher, "What is Codemode": runs in the harness, QuickJS within a WASM runtime, "no network, no file system, no timers, limited RAM")
- https://earendil.com/posts/you-said-no-mcp/ (section "What Is Codemode?")

---

## 3. How MCP tools reach the model (how it works)

**Model answer.** By default an MCP server has `codemode` exposure: its tools are registered as `mcp__<server>__<tool>` and are callable from Codemode scripts, but they are not declared to the model and not listed in the Codemode tool description. Pi turns Codemode on automatically when such a server connects, lists the server in the system prompt, and scripts discover its tools with `searchTools()`, `describeTool()` or `ALL_TOOLS`. The other options are `deferred` (not declared until the `tool_search` tool loads a match for the next model call), `direct` (declared to the model like a built-in tool) and `hidden` (registered but unreachable); `toolExposure` can override the setting per tool.

**Rubric.**
- 2: Says the default is that tools are not put into the model's tool list but are reached and discovered through Codemode scripts, and names or correctly describes at least two of the other options (deferred via tool search, direct, hidden).
- 1: Knows the tools are not all dumped into context by default, or knows they go through Codemode, but cannot describe the alternatives; or describes the alternatives but gets the default wrong.
- 0: Says every MCP tool definition is loaded into the context up front, or that Pi 1.0 has no MCP support.

**Sources.**
- https://github.com/earendil-works/pi/blob/v1.0.0/packages/coding-agent/docs/mcp.md (section "Control tool exposure")
- https://github.com/earendil-works/pi/blob/v1.0.0/packages/coding-agent/docs/cli.md (section "Tools": `codemode` and `tool_search` are off by default and turned on by the MCP extension when a server needs them)

---

## 4. Why Pi reversed on MCP (why)

**Model answer.** The original objection was that MCP servers dump all their tool descriptions into the context on every session (Mario Zechner cited 13.7k to 18k tokens for popular servers) and compose poorly, while CLI tools with a README are read only when needed and compose through bash. The makers say MCP itself has changed, and that what MCP needs is what Pi needed anyway: a sandboxed interpreter (Codemode), which also makes non-LLM models such as Jev usable. It went into the core because an MCP extension did not have enough metadata from Pi's tool loadout to mark tools as deferred or Codemode-only, and because they would rather help shape MCP ("the best way to positively influence something is to embrace it") than stand on the sidelines. On Hacker News both maintainers added that they follow what models are trained on, and that GPT-family models now rely on Codemode for parallel tool calls.

**Rubric.**
- 2: States the original objection (context/token overhead and/or poor composability compared with CLI tools) and gives at least two of the stated reasons for the change: MCP has improved; Codemode solves the context/composition problem and was needed anyway (for example for Jev or because models are trained on it); an extension lacked the tool-loadout metadata; wanting to influence MCP by embracing it.
- 1: Gives the original objection plus one reason, or two reasons without the original objection.
- 0: Says only "users asked for it" or "to catch up with competitors", or gets the original stance wrong.

**Sources.**
- https://earendil.com/posts/you-said-no-mcp/ (Earendil Engineering, 2026-09-29)
- https://mariozechner.at/posts/2025-11-30-pi-coding-agent/ (section "No MCP support": "pi does not and will not support MCP", token figures, CLI-plus-README alternative)
- https://news.ycombinator.com/item?id=49926377 (Armin Ronacher: "we look at what the models are doing ... codemode was a given")
- https://news.ycombinator.com/item?id=49926840 (Mario Zechner: GPT models trained on Codemode for parallel tool calls; MCP spec update)

---

## 5. Why Pi Durable is a separate package (why)

**Model answer.** The Pi coding agent is built to run on your machine, in a terminal, driven by one person; if the process dies, you look at what happened and tell it to continue, and Earendil says that focus is not changing. Reaching Pi from other surfaces, running very long conversations, surviving crashes and letting several people steer the same agent did not fit that shape, so rather than "stray from our minimal roots" they put that work into a new experimental package. Keeping it separate also lets them explore designs without disrupting the coding agent, with lessons flowing back into Pi once they have proven themselves. Pi Durable does not replace the coding agent; it is a framework for building agentic applications.

**Rubric.**
- 2: Explains that the coding agent is deliberately scoped to one person in a terminal and kept minimal, that durable / multi-surface / multi-user needs did not fit that scope, and that a separate experimental package lets them explore without disrupting or bloating Pi (or notes it does not replace Pi).
- 1: Says "to keep Pi minimal" without explaining what did not fit, or describes what Pi Durable does without the reason for separating it.
- 0: Says Pi Durable replaces Pi, is a paid product, or is the same thing as Pi 1.0.

**Sources.**
- https://earendil.com/posts/pi-1-0/ (Earendil, 2026-10-01)
- https://earendil.com/posts/pi-durable/ (section "Why Pi Durable?")

---

## 6. Where Pi came from (context)

**Model answer.** Pi was created by Mario Zechner (also the creator of libGDX), who described it in November 2025 as an opinionated, minimal coding agent: four tools (read, write, edit, bash), a system prompt and tool definitions under 1,000 tokens together, "YOLO by default" with no permission prompts, and no built-in to-dos, plan mode, MCP, background bash or sub-agents. It grew out of his frustration with Claude Code becoming a "spaceship" whose prompt and tools changed on every release, and it is also the minimal agent inside OpenClaw. On 2026-04-08 Earendil, the public benefit corporation founded by Armin Ronacher and Colin Daymond Hanna, announced it had acquired the Pi open source project, with Zechner joining as a major stakeholder and team member.

**Rubric.**
- 2: Names Mario Zechner as the creator, describes the minimal stance with at least two concrete features (for example four tools, tiny system prompt, no permission prompts, no MCP / plan mode / sub-agents), and says Earendil acquired the project (spring / April 2026) with Zechner joining.
- 1: Gets two of the three parts (creator, design stance, move to Earendil).
- 0: Says Earendil or Armin Ronacher created Pi from scratch, or confuses it with another product.

**Sources.**
- https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
- https://mariozechner.at/posts/2026-04-08-ive-sold-out/
- https://earendil.com/posts/announcing-pi-and-lefos/ (2026-04-08)
- https://lucumr.pocoo.org/2026/4/8/mario-and-earendil/

---

## 7. How 1.0 was received (context)

**Model answer.** The announcement reached the top of Hacker News (1,689 points and 610 comments as of 2026-11-11), and many commenters praised Pi's consistency, simplicity and small system prompt. Criticisms included that the bar for a "proven" idea looked uneven (MCP had been growing for nearly two years, while Jev had taken off less than a month earlier), that Pi's days as a minimal agent were numbered, that fullscreen by default goes against the minimalist theme, and doubt about the "hundreds of thousands" of weekly users, a figure Trending Topics noted cannot be independently verified. Armin Ronacher answered that they follow what models are trained to do and that Codemode "was a given"; Mario Zechner answered that the new features are optional and the only added weight is a few megabytes of QuickJS WASM.

**Rubric.**
- 2: Says the reception was strongly positive / high-profile (for example top of Hacker News) and gives at least two specific criticisms or doubts from: uneven "proven" criteria or the MCP reversal; fear of losing minimalism; fullscreen by default; the unverified user-count claim; choice of JavaScript; trust in a plugin ecosystem. Also reports one maker reply.
- 1: Gives the positive headline and one specific criticism, or two criticisms without the makers' reply.
- 0: Claims it was ignored or panned, or gives only invented criticisms.

**Sources.**
- https://news.ycombinator.com/item?id=49926069 (thread; points and comment count read from the HN Algolia API on 2026-11-11)
- https://news.ycombinator.com/item?id=49926262 (uneven "proven" criteria) and https://news.ycombinator.com/item?id=49926377 (Ronacher's reply)
- https://news.ycombinator.com/item?id=49926549 (minimal days "numbered") and https://news.ycombinator.com/item?id=49926840 (Zechner's reply)
- https://news.ycombinator.com/item?id=49926760 (doubt about the user count)
- https://www.trendingtopics.eu/pi-1-0-earendil-en/ (topped Hacker News; "The user figure cannot be independently verified")

---

## 8. Untrusted repository in CI (application)

**Model answer.** Print mode cannot show the trust prompt, and with the default `defaultProjectTrust: "ask"` and no saved decision or `--approve` flag, Pi skips the trust-protected project resources, so `.pi/extensions/` and `.pi/mcp.json` are not loaded. `AGENTS.md` is a context file and loads regardless of project trust, so the repository's instructions (and any file or command output the agent reads) can still steer the model. The run is not safe on that basis: Pi has no built-in permission system, does not ask before tool calls, and its tools run with the operating-system permissions of the CI user, so project trust is not a sandbox. Run the whole Pi process in a container, VM or sandbox that exposes only the needed files and narrowly scoped, short-lived credentials (optionally pass `--no-approve` to make the trust decision explicit and `--no-context-files` to skip `AGENTS.md`).

**Rubric.**
- 2: Predicts that the `.pi` extensions and MCP config are skipped while `AGENTS.md` still loads, says this does not make the run safe because tools run unprompted with the process's full OS permissions (prompt injection remains possible), and proposes isolation (container / VM / sandbox, scoped credentials).
- 1: Gets the safety conclusion and the fix right but is wrong or silent on what loads, or gets what loads right but concludes that skipping trust makes it safe enough.
- 0: Says Pi will prompt for approval before each command, that declining trust sandboxes the agent, or that the extensions load automatically.

**Sources.**
- https://github.com/earendil-works/pi/blob/v1.0.0/packages/coding-agent/docs/security.md (sections "Understand project trust", "Project trust without an interactive prompt", "Choose how to run Pi")
- https://github.com/earendil-works/pi/blob/v1.0.0/README.md (section "Permissions & Containerization")
- https://github.com/earendil-works/pi/blob/v1.0.0/packages/coding-agent/docs/cli.md (`-p`/`--print`, `-a`/`--approve`, `-na`/`--no-approve`, `-nc`/`--no-context-files`)
