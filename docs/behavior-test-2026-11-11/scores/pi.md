SHEETS
sheet-A: 2 2 2 2 2 2 2 2 = 16
sheet-B: 1 2 2 2 2 2 2 2 = 15
sheet-C: 2 2 2 2 2 2 2 2 = 16
WRITEUPS
answer-A: 0 2 2 1 1 2 2 1 = 11
answer-B: 0 2 2 2 1 2 1 1 = 11
answer-C: 1 2 2 2 2 2 1 1 = 13
CONTRADICTIONS
- sheet-B.md (q1): "Another turn starts only because the model called tools: the loop keeps going until the model answers without calling any". The key says queued (steering / follow-up) messages can also start another turn.
- No other statement in the sheets or write-ups contradicts the key. Extra details the key does not cover (256 MB memory limit, `store()`/`load()`, the 10,000-token output cap, release-version history, Cloudflare Code Mode lineage, cache-warming thresholds) were not counted as contradictions.
NOTES
- sheet-B q1 = 1: the request / tool-call / result cycle is right. The history source is vague ("session transcript", with branching only mentioned in passing, not "active branch"), and the stop condition is wrong, since it leaves out queued messages and says "only".
- sheet-B q7 and sheet-C q7 = 2 (borderline): both say they saw no direct maker replies in the HN thread, but each still gives a maker answer to a criticism it lists. B: MCP kept off-context through Codemode and adopted in order to influence it, plus `tuiMode` regular for fullscreen. C: the "You Said No MCP!" rebuttal for the MCP/"proven" criticism, plus `tuiMode: "regular"`. These count as "reports one maker reply". A stricter reading that accepts only HN-thread replies would make each of them 1.
- sheet-B q8 = 2 (borderline): it hedges on `.pi/extensions/` and `AGENTS.md`, but it still makes the correct prediction for all three files, reaches the right safety conclusion and gives the container fix. Its "I'm not sure" hedges were not penalised beyond what the content supports.
- sheet-A q1 = 2: it admits the stop condition comes from its own reading of other docs, but the content (tool calls or queued steering / follow-up messages) matches the key.
- Write-ups q1: answer-A and answer-B only say a harness "wraps a model with a loop", which scores 0. answer-C describes the request / run-tools / loop cycle and JSONL session trees with parent pointers, but gives no active-branch statement and only "loops until the work is done" as a stop condition, so 1.
- answer-A q4 = 1: it gives reasons (the spec changed, models are trained to orchestrate through code) but never states the original objection (token / context cost), only that Pi refused MCP.
- answer-A q5 = 1 and answer-B q5 = 1: both describe what Pi Durable does (and A says it is not a replacement), but neither explains why it was kept out of Pi beyond B's "instead of growing the coding agent". answer-C = 2: one person, one terminal, restart by hand, versus agents that outlive the process, kept separate so the coding agent stays small.
- Write-ups q7: answer-A = 2 because it names Zechner's reply on minimalism drift. answer-B and answer-C list criticisms but frame no maker reply to them, so 1 each. A reader could build one by inference from their MCP-rationale sections (that is how sheet-B and sheet-C got credit), but the write-ups do not present those sections as replies.
- Write-ups q8 = 1 for all three: each has the "not safe, tools run with full user permissions, use a container / VM" conclusion. None says that print mode skips trust-protected resources with no saved decision, or that `AGENTS.md` loads regardless of trust. answer-A covers only `.pi/mcp.json` being gated by trust, and answer-C only "trust decides whether settings and extensions load".
- answer-B and answer-C q3 = 2: both give the codemode default (not declared, found from scripts) and at least two other exposures. answer-A's "callable only from scripts and add nothing to the prompt" was accepted as the discovery-through-Codemode point.
- No credit was given for length. sheet-A and sheet-C are long but were scored only on the rubric elements.
