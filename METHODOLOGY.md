# Methodology

Build is a learn-by-shipping community for building real products with AI agents.

This file is the seed of a future methodology book: how to use AI across the whole startup-building process.

For now, this is intentionally small. We are starting by collecting practical tips, workflows, prompts, and patterns that help us ship better.

## Principles

- Prefer real shipping over theory.
- Make AI work visible, testable, and reviewable.
- Capture workflows as reusable methods.
- Improve this file through pull requests.

## 1. Specify Tests Before Implementation

When working with AI, one way to avoid endless debugging loops is to define the tests first.

Instead of starting with “build this,” start by asking the AI to create a full testing specification for the idea.

Then, preferably in a new session, ask the AI to implement the idea until it passes all the predefined tests.

For web systems, it is especially useful to give the AI access to a browser, such as Chrome or Playwright, so it can test the product end-to-end.

### Example prompt

```text
Before implementing this feature, write a complete testing specification.

Include:
- expected behavior
- edge cases
- failure cases
- unit tests
- integration tests
- end-to-end tests
- manual QA checklist

Do not implement yet.
```

Then, in a new session:

```text
Implement this feature until it passes the full testing specification below.

Do not consider the task done until all tests pass.
```

## 2. Keep the Source of Truth Outside the Chat

Important product decisions should not live only inside an AI chat.

Whenever a conversation produces something valuable, turn it into a durable artifact:

- `README.md`
- `SPEC.md`
- `methodology.md`
- GitHub issue
- pull request
- decision log

The AI chat is a workshop.  
The repo is the source of truth.

### Example prompt

```text
Turn this conversation into a clean SPEC.md file.

Keep only decisions, open questions, assumptions, and next actions.
Remove chat noise.
```

## 3. Use Separate AI Sessions for Separate Jobs

Do not overload one AI session with every role.

A useful pattern:

- one session for product/spec
- one session for implementation
- one session for testing
- one session for review/critique

This creates separation between “builder mode” and “reviewer mode,” and helps catch blind spots.

### Example workflow

```text
Session 1: Define the feature.
Session 2: Write the test plan.
Session 3: Implement.
Session 4: Review the diff and look for bugs.
```

## 4. Treat AI Output Like a Pull Request

AI output should not be treated as truth.

Treat it like a strong draft that needs review.

Ask for:

- diffs
- assumptions
- risks
- tests
- alternatives
- rollback plans
- open questions

### Example prompt

```text
Review your own work as if this were a pull request.

List:
- what changed
- what could break
- missing tests
- security/privacy risks
- anything that should be simplified
```

### Spec-improvement helper: tiny-pr-bot

[ripper234/tiny-pr-bot](https://github.com/ripper234/tiny-pr-bot) is an autonomous bot (powered by OpenClaw) that watches spec repositories and opens small, focused PRs to improve clarity, reduce ambiguity, and unblock decisions — with minimal decision overhead for the operator.

Typical PR size: 1–2 lines, 1 file. The bot avoids large refactors and multi-decision changes.

Usage pattern:

1. Point the bot at a spec repo via `config/clawbot.config.json`.
2. The bot polls continuously; when it identifies a high-value improvement, it opens a PR and notifies via Telegram.
3. Review the PR and respond with the feedback protocol: `APPROVE`, `CHANGES`, `NOPE`, `NOW`, `PAUSE`, or `RESUME`.
4. The bot waits for feedback before proposing the next PR, keeping decision load low.

## Specific Tools
### Claude

#### Lee Twito & Gal Peretz - 29.6.26

This episode is about practical workflows for coding agents: Codex, Claude Code, Cursor, Superpowers, visual planning, PR environments, terminal setup, browser auth, secrets, and overnight agent tasks.
Main thesis: agents work much better when you give them visual plans, explicit definitions of done, proof-of-work loops, isolated browser/auth profiles, and clear process skills.
Several tool names are noisy in the transcript, so I marked unclear names rather than guessing. Confidence: medium, because the source is a rough speech-to-text transcript.

[English translation](https://gist.github.com/ripper234/58606f3649dc5fb72955880ed0e6dfc2)

Hebrew Source (30 min)
https://www.linkedin.com/posts/lee-twito_70-our-claude-code-tips-share-7477210420131401728-yePc/


## Future Sections

Possible future chapters:

- Product discovery with AI
- MVP scoping
- Agentic coding workflows
- AI-assisted design
- Testing and QA
- Launch and marketing
- Community building
- Open-source governance
- Working with Cofounder.co
- Human roles vs AI roles

