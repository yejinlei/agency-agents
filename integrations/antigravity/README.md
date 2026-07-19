# Antigravity Integration

Installs the full Agency roster as Antigravity skills. 每个代理都是 prefixed
with `agency-` to avoid conflicts with existing skills.

## Install

```bash
./scripts/install.sh --tool antigravity
```

This copies files from `integrations/antigravity/` to
`~/.gemini/config/skills/` (global). For project-scoped skills, Antigravity
also reads `<project>/.agents/skills/`.

## Activate a Skill

In Antigravity, activate an agent by its slug:

```
使用 agency-frontend-developer skill to 审查这个组件.
```

Available slugs follow the pattern `agency-<agent-name>`, e.g.:
- `agency-frontend-developer`
- `agency-backend-architect`
- `agency-reality-checker`
- `agency-growth-hacker`

## Regenerate

After modifying agents, regenerate the skill files:

```bash
./scripts/convert.sh --tool antigravity
```

## File Format

Each skill is a `SKILL.md` file with Antigravity-compatible frontmatter:

```yaml
---
name: agency-frontend-developer
description: Expert frontend developer ，专攻...
risk: low
source: community
date_added: '2026-03-08'
---
```
