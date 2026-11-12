---
name: step-back-understand
description: "Understand a person, work, idea, product, system or anything else, including why it is the way it is and the context around it, by studying the things that shaped it and then explaining the subject through them. Strongest on subjects you do not already know well: new releases, niche people and works, unfamiliar codebases, internal systems. Use when invoked by name or when the user explicitly asks for this kind of understanding."
---

# Step Back Understand

You can read about John Mayer and know some facts about John Mayer. Learn Albert King, Stevie Ray Vaughan and Jimi Hendrix as players in their own right, and Mayer's playing starts to make sense: you know whose bends those are, why he plays the way he does, and what is his alone. That is the goal: a better understanding of the subject itself, how it works, why it is that way, and where it sits among the things around it.

The influences are how you get there. They are your research, not your answer. The person asking wanted to understand Mayer, not to read an essay about Albert King.

**The whole skill in two sentences:** research the subject thoroughly, including the things that shaped it. Then explain the subject itself (what it is, how it works, why it is this way, its context), bringing in an influence only where it explains a specific feature. The rest of this file is detail on doing that well.

## When it earns its cost

- **Strong:** subjects you do not already know well (anything recent, niche, internal or new to you). Recognizing what something descends from lets you carry over everything you know about the ancestor: "this is built like Cargo" tells you how a new tool will behave before you have read its docs.
- **Strong:** questions about why: why it was designed this way, why it sounds this way, why people reacted to it as they did.
- **Weak:** a famous subject where a plain explanation is what is wanted. You already absorbed its lineage in training. If you are invoked on one anyway, run a short pass: write the complete plain explanation, and trace back only the features it leaves unexplained.

## 1. Look at the subject first

Read, inspect or examine the subject itself (its docs, code, the work, its own statements) before tracing anything backward. Write down what it is, its main parts, how it works, and what about it you cannot yet explain. The unexplained features are what the step back is for. Everything else on that list is what the answer still has to cover.

If you cannot examine the subject directly (an album you cannot hear, a product you cannot run), work from its makers' statements and from people who did examine it, and say so in one line of the answer.

## 2. Find what shaped it

For each unexplained feature, ask what it came from:

| Subject | Where to look |
| --- | --- |
| Person | teachers, heroes, scenes, collaborators, formative jobs, tools they grew up with |
| Work | earlier works it answers or imitates, genre conventions, the maker's prior work, how it was made |
| Product or system | predecessors, the ideas and papers it inherits, its dependencies, the constraints it was built under, what it was built to replace |
| Concept or method | the problem it answered, the field it came from, the idea it reacted against |
| Organization | founders' previous companies, the gap it filled, what it copied or rejected |

Prefer influences the subject or its makers name. An influence nobody names can still be used when it clearly explains a feature; call it a resemblance. Pick for explanatory value, not fame. Look sideways as well as back: what the subject competes with and how it was received are part of its context.

## 3. Learn the important influences in their own right

A name on a list teaches nothing. For the two to five influences that explain the most, learn what each is actually like: its signature traits, how it works, what it did differently from what came before. Then ask which of those traits show up in the subject, and what the subject changed. A subject with several separate parts (a release with many features) may need one or two influences per part.

What you already know about an influence counts, but check the specific traits you plan to rely on against a reference. Memory of a famous thing is often a caricature of it.

Keep notes for yourself (they do not go in the answer) of what you checked and how solid each link is: stated by the maker, an observable part or dependency, or only a resemblance. Check that each reference supports the specific claim, not just the topic. Never claim to have heard, watched or run something you did not. Where references disagree on a fact the answer depends on, say so in a clause; where the fact is a side detail, leave it out.

Go a layer deeper only when an influence is itself best understood through its own influences (Vaughan through Albert King). Stop when the subject's features are explained.

## 4. Turn the lineage into understanding of the subject

Write down, for yourself:

- **What it is and how it works**, now explained rather than listed.
- **Why it is this way**: which features came from where, and what the subject did differently.
- **What to expect**: predictions the lineage gives you about things you have not checked. "It descends from X, so it probably also does Y." Verify the important ones; a verified prediction is then a plain fact. An unverified one goes in the answer only if it helps the reader, marked as an expectation.
- **Context**: what came before and around it, what it reacts against, how it was received and why.
- **What is its own**: what the influences do not explain.

## 5. Answer about the subject

The answer explains the subject. The person should finish it understanding the subject better, not knowing more about its ancestors.

- **Cover the whole subject:** what it is, its main parts, how it works, why it is this way, and its context. A newcomer should not be missing a basic piece because the lineage had nothing to say about it.
- **Explain, do not assert.** Every main point carries its reason or mechanism: what causes it, or what it follows from. A point stated without its reason is a fact sheet entry.
- **Use an influence only where it makes a specific feature click,** in a sentence or two at that point: "his bends overshoot the note and come back down the way Albert King's did, which is why they sound vocal rather than precise." Give only the trait that explains the feature. No biography or track record of the influence, no section per influence, no family tree.
- **Teach each point once.**
- **Keep uncertainty in plain words, in a clause, where it matters** ("the maker hasn't said this; it's a resemblance"). No evidence-class labels. Do not narrate the research: what you could not find, or which pages disagreed on a side detail.
- **End with a short reference list:** the handful of pages you relied on most. Your notes stay out of the answer unless asked for.
- **Length follows the question.** A broad "help me understand X" needs room to cover the points above with their reasons, commonly 1,000 to 1,500 words. A narrow question gets a short answer. Do not cut explanation to be brief, and do not add facts that explain nothing.

## Check before sending

Send it back for another pass if any of these is true:

- A reader would learn more about the influences than about the subject, or a sentence about an influence explains no feature of the subject.
- It is organized by influence rather than by feature of the subject.
- A basic part of the subject is missing: what it is, its main parts, how it is used or experienced.
- A main point is stated without its reason.
- A claim is more certain than its evidence.
- It contains nothing a plain explanation of the subject would not have said. If the step back found nothing, say so briefly rather than padding.

## Which step back

Use this skill for understanding. For stalled work and repeated failed approaches, use `step-back-evaluate` from the separate Step Back Protocol skill, if it is installed; if that exposes a missing understanding of the subject, run this skill and return to the recovery.

## Example: what the answer looks like

Request: "Help me understand John Mayer's lead guitar playing." (Abbreviated.)

> Mayer's lead playing is blues vocabulary played with a pop songwriter's restraint. Three things carry it.
>
> **The bends.** His signature move is a wide bend, often past a whole step, that lands on the target note and sometimes catches a second string on the way. That is Albert King's move, which reached Mayer through Stevie Ray Vaughan; Mayer has said Vaughan was the first player he heard who was "not just strumming chords." Knowing this tells you what to listen for: a King-style bend pulls past the note for tension, where a B.B. King bend is a smaller, finger-vibrato phrase.
>
> **Space.** Where Vaughan fills every bar at full volume, Mayer leaves gaps and plays under the vocal. ...
>
> **Rhythm as lead.** ... (critics compare this to Hendrix; Mayer hasn't described it that way himself, so treat it as a resemblance.)
>
> References: ...

The research behind this answer covered Albert King's upside-down Flying V and pull-down bends, Vaughan's adoption of them, and Mayer's own statements. The answer uses that research only where it explains Mayer.
