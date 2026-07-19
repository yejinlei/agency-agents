# Gemini CLI Integration

Packages all Agency agents as Gemini CLI subagents. These agents
install to `~/.gemini/agents/`.

## Install

```bash
# Generate the Gemini CLI agent files first
./scripts/convert.sh --tool gemini-cli

# 然后安装它们 to ~/.gemini/agents/
./scripts/install.sh --tool gemini-cli
```

## Use an Agent

In Gemini CLI, reference an agent by name in your prompt:

```
使用 frontend-developer 代理来 help me build this UI.
```

Or invoke the agent directly if your version of Gemini CLI supports it:

```bash
gemini --agent frontend-developer "How should I structure this React component?"
```

## Structure

```
~/.gemini/agents/
  frontend-developer.md
  backend-architect.md
  reality-checker.md
  ...
```

## Regenerate

```bash
./scripts/convert.sh --tool gemini-cli
```
