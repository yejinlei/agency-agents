# GitHub Copilot Integration

The Agency works with GitHub Copilot out of the box. No conversion needed —
agents use the existing `.md` + YAML frontmatter format.

## Install

```bash
# Copy all agents to your GitHub Copilot agents directories
./scripts/install.sh --tool copilot

# 或者手动复制一个分类
cp engineering/*.md ~/.github/agents/
cp engineering/*.md ~/.copilot/agents/
```

## Activate an Agent

In any GitHub Copilot session, reference an agent by name:

```
Activate Frontend Developer and help me build a React component.
```

```
使用 Reality Checker 代理来 verify this feature is production-ready.
```

## Agent Directory

Agents are organized into divisions. 参见 the [main README](../../README.md) for
the full current roster.
