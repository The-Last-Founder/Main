# SPEC: Contributor Onboarding GPT Experience

## Status

Proposed (Issue #13)

## Problem

People discover Build and want to help, but do not know where to start.

## Goal

Create a GPT-like onboarding flow that:

1. Explains Build in two short lines.
2. Asks 3–5 lightweight questions.
3. Produces concrete, bite-sized next steps for the person.

## Non-Goals (v0.1)

- No data collection by Build (no stored name/email).
- No account system.
- No guaranteed real-time issue matching.

## User Flow

1. User opens onboarding chat.
2. Assistant gives a 2-line explanation of Build and links for deeper reading.
3. Assistant asks brief onboarding questions.
4. Assistant returns:
   - a personalized onboarding summary,
   - a suggested starting area,
   - one starter task the user can do in ~30–90 minutes.

## Assistant Opening (Draft)

Build is an open-source learn-by-shipping community for building real products with AI agents.  
We collaborate in public, ship small, and learn what works.

Start here:
- README: https://github.com/The-Last-Founder/Build/blob/main/README.md
- Methodology: https://github.com/The-Last-Founder/Build/blob/main/METHODOLOGY.md
- Tools: https://github.com/The-Last-Founder/Build/blob/main/Tools.md

## Onboarding Questions (3–5)

Ask in this order, keeping everything optional except where noted:

1. **Name** (for personalization).
2. **Contact email** (collect in-chat for now; not persisted in v0.1).
3. **Experience with AI/agents** (none / beginner / intermediate / advanced + optional details).
4. **Needs, goals, or dreams** (what they want to build or learn).
5. **Project context (optional)**: idea, existing repo, doc, or “no project yet”.

## Required Output Format

After the questions, always produce:

1. **Your onboarding summary** (3–5 bullets).
2. **Best starting area** (one primary recommendation).
3. **Starter task (30–90 min)** with clear done criteria.
4. **Next 2 follow-up options** the user can pick from.

## Starting Areas (fallback routing)

If no clear project fit is found, route to one of:

- Marketing / storytelling / website messaging
- Community management
- Architecture / systems thinking
- Curation / documentation / content

## Version Plan

### v0.1 (MVP)

- Runs as a custom GPT-style experience.
- Collects context conversationally but stores nothing for Build.
- Prioritizes clear recommendations and quick first action.

### v0.2

- Move experience to Build-owned server or a suitable SaaS.
- Keep GPT-like conversational UX (not a static fixed form).
- Add consented persistence for onboarding fields (including email) and outputs.
- Preserve the same question flow and concrete-output contract.

## Acceptance Criteria

1. First response includes a two-line Build intro plus links.
2. Assistant asks the 3–5 onboarding questions above.
3. Assistant tolerates sparse answers and still returns concrete output.
4. Every completed onboarding ends with a starter task and done criteria.
5. If no project exists, assistant still routes to a valid fallback area.
6. v0.1 explicitly does not depend on backend data storage.

## Manual QA Checklist

- Simulate user with no AI background and no project.
- Simulate user with strong AI background and existing repo.
- Simulate user who skips email and gives minimal answers.
- Verify output is still concrete, short, and actionable in all cases.
- Verify fallback routing works when project context is empty.
