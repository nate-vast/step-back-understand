# Pi 1.0 comprehension quiz

Answer each question in 2-4 sentences.

1. You type a message into Pi and press Enter. Describe what happens in one turn of the agent loop, where the conversation history for the model request comes from, and what decides whether another turn starts.

2. What is Codemode in Pi 1.0? Say where a Codemode script runs, what it can and cannot touch, and what ends up in the model's context when it finishes.

3. You add an MCP server to Pi 1.0 and change nothing else. How do that server's tools reach the model by default, and what other exposure options does Pi offer?

4. Pi's original author wrote that Pi "does not and will not support MCP", yet Pi 1.0 ships MCP in the core. What was the original objection, and what reasons did the makers give for changing course and for building it into the core instead of leaving it as an extension?

5. Alongside Pi 1.0, Earendil released Pi Durable as a separate, experimental package. Why did they keep long-running, crash-surviving, multi-user agents out of the Pi coding agent itself?

6. Where did Pi come from before Earendil? Name who created it, the design stance it started with, and how it ended up at Earendil.

7. How was the Pi 1.0 release received? Give the headline reaction and at least two specific criticisms or doubts that were raised, and say how the makers answered one of them.

8. A CI job clones a third-party repository that contains `.pi/extensions/`, `.pi/mcp.json` and an `AGENTS.md`, then runs `pi --print "fix the failing test"` with default settings and no saved trust decision. Predict what Pi loads and what it skips, and say whether that makes the run safe. If not, what would you change?
