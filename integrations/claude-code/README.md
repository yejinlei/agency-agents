# Claude Code Integration

The Agency was built for Claude Code. No conversion needed — agents work
natively with the existing `.md` + YAML frontmatter format.

## Install

```bash
# Copy all agents to your Claude Code agents directory
./scripts/install.sh --tool claude-code

# 或者手动复制一个分类
cp engineering/*.md ~/.claude/agents/
```

## Activate an Agent

In any Claude Code session, reference an agent by name:

```
Activate Frontend Developer and help me build a React component.
```

```
使用 Reality Checker 代理来 verify this feature is production-ready.
```

## Agent Directory

Agents are organized into divisions. 参见 the [main README](../../README.md) for
the full Agency roster.
