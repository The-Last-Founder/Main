# Tools

A starter map of tools and practices we may use while building the Build community and the Johnny pilot.

## How to read this

**Scope**

- **General**: useful for builders across projects.
- **Johnny**: specifically relevant to the [Johnny pilot](https://github.com/The-Last-Founder/Johnny).
- **Both**: useful generally and also relevant to Johnny.

**Signal (as of June 2026)**

- For open-source tools: GitHub stars, activity, or similar visible traction.
- For commercial tools: product maturity, adoption, or strategic relevance.
- For concepts: source quality or relevance, not popularity.

**Bold tools** are primary candidates for early hands-on use or evaluation.

The table is sorted roughly by first-sprint usefulness, then by Johnny MVP relevance.

## Tool map

| Tool | Scope | Category | What it does | Why for us | Released / maturity | Signal (June 2026) |
|---|---:|---|---|---|---|---|
| [**Cofounder.co**](https://cofounder.co/) | Both | Company agent OS | AI company OS across engineering, sales, marketing, design, finance, and ops. | Main harness for starting the project, coordinating agents, and testing AI-native startup workflows. | Active commercial product. | Primary starting harness. |
| [**Claude Code**](https://github.com/anthropics/claude-code) | Both | Agentic coding | Coding agent for terminal, IDE, GitHub workflows, and repo changes. | Main implementation tool for coding, reviewing, debugging, docs, and PR workflows. | Mature Anthropic coding product with active releases. | Official Anthropic tool; high builder relevance. |
| [**Codex**](https://github.com/openai/codex) | Both | Agentic coding | OpenAI coding agent for CLI, IDE, app, and cloud workflows. | Second coding agent for parallel implementation, review, and comparison with Claude Code. | Active OpenAI coding product and OSS CLI. | Official OpenAI tool; high builder relevance. |
| [ctx](https://github.com/stevesolun/ctx) | Both | Agent context / tool routing | Graph-backed recommendation layer for skills, agents, MCP servers, and harnesses, with CLI and dashboard workflows. | Companion to Claude Code and Codex: helps builders load the right context bundle for the current task without bloating agent sessions. | Active MIT OSS Python package on PyPI. | Ships a large recommendation graph: 68k+ skills, 10k+ MCP servers, 467 agents, and 207 harnesses. |
| [GitHub Copilot](https://github.com/features/copilot) | Both | Coding assistant / agent | AI coding assistant inside GitHub, IDEs, CLI, and PR workflows. | Lowest-friction tool for builders already living inside GitHub. | Mature GitHub product. | Very broad adoption. |
| [OpenClaw](https://github.com/openclaw/openclaw) | Both | Personal agent runtime | Self-hosted personal AI assistant that runs across chat channels and devices. | Candidate reference/backend for chat-native agent architecture and task automation. | Active OSS. | Very high GitHub traction. |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Both | Persistent agent runtime | Self-improving agent with memory, skills, messaging gateways, and multi-platform execution. | Candidate backend/reference for persistent memory, agent skills, and long-running routines. | Active OSS, with June 2026 releases. | High relevance for persistent-agent patterns. |
| [**Claude Tag**](https://www.anthropic.com/news/introducing-claude-tag) | Both | Team agent in chat | Lets teams tag Claude inside Slack channels and delegate work. | Strong reference for Johnny’s “shared teammate in a group chat” behavior. | Released 2026-06-23, beta. | Anthropic Team/Enterprise beta. |
| [Loop Engineering](https://www.oreilly.com/radar/loop-engineering/) | General | Practice / workflow | Designing feedback loops around agents: plan, act, verify, adjust, repeat. | Core skill to teach builders: stop prompting once, start designing reliable loops. | Emerging 2026 practice. | High relevance, not a product. |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | General | Agent skill / ruleset | Makes coding agents prefer the smallest working solution and avoid overengineering. | Useful default skill/ruleset so agents ship less bloat and simpler code. | Active OSS. | Strong fit for builder discipline. |
| [Talk To My Agent](https://www.talktomyagent.io/) | General | Voice gateway | Gives an OpenClaw-style agent a real phone number. | Later-stage inspiration for voice access, support calls, or personal assistant workflows. | Active commercial product. | Niche but directly adjacent. |
| [**open-bsp-api**](https://github.com/matiasbattocchia/open-bsp-api) | Johnny | WhatsApp / Instagram infra | Self-hostable WhatsApp and Instagram Business API platform by Matías Battocchia. | Most directly relevant infrastructure candidate for Johnny’s WhatsApp-native MVP. | Active OSS. | Small repo, very high strategic relevance. |
| [Any.do](https://www.any.do/) | Johnny | Task management | Tasks, lists, calendar, reminders, WhatsApp task capture, AI assistant, and team boards. | Integration candidate and UX reference for Johnny’s tasks, reminders, and AI-assisted task capture. | Mature commercial product. | Mature product; WhatsApp support; 40M+ users claimed. |
| [monday.com](https://monday.com/) | Johnny | Work management | Work OS for teams, projects, workflows, CRM, dev, service, automations, and AI agents. | Integration candidate for teams that outgrow Markdown task files. | Mature commercial product. | Mature AI work platform. |

## Notes

- **Johnny-specific tools are marked in the Scope column.**
- **Bold tools** are the current primary candidates: Cofounder.co, Claude Code, Codex, Claude Tag, and open-bsp-api.
- **Loop Engineering is a practice, not a tool**, but it belongs here because it is central to how builders will use agents well.
- **Trello was intentionally removed** because it is not central enough to the AI-native Johnny workflow right now.
- **The task “Upload Tools.md to Johnny GitHub” is not a tool**, so it is intentionally not listed in the table.
- This file should stay concise. Add new tools only when someone actually plans to try them, teach them, or integrate them.
