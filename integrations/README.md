# 🔌 Integrations

此目录包含 Agency 集成 and converted formats for
supported agentic coding tools.

## 支持的工具

- **[Claude Code](#claude-code)** — `.md` agents, use the repo directly
- **[GitHub Copilot](#github-copilot)** — `.md` agents, use the repo directly
- **[Antigravity](#antigravity)** — `SKILL.md` per agent in `antigravity/`
- **[Gemini CLI](#gemini-cli)** — `.md` agent files in `gemini-cli/agents/`
- **[OpenCode](#opencode)** — `.md` agent files in `opencode/`
- **[OpenClaw](#openclaw)** — `SOUL.md` + `AGENTS.md` + `IDENTITY.md` workspaces
- **[Cursor](#cursor)** — `.mdc` rule files in `cursor/`
- **[Aider](#aider)** — `CONVENTIONS.md` in `aider/`
- **[Windsurf](#windsurf)** — `.windsurfrules` in `windsurf/`
- **[Kimi Code](#kimi-code)** — YAML agent specs in `kimi/`
- **[Qwen Code](#qwen-code)** — project-scoped `.md` SubAgents in `.qwen/agents/`
- **[Codex](#codex)** — `.toml` custom agents in `codex/`
- **[Mistral Vibe](vibe/README.md)** — `.toml` agents + prompt files generated in `vibe/`
- **Osaurus** -- `SKILL.md` skills generated in `osaurus/`
- **[Hermes](hermes/README.md)** -- lazy-router plugin generated in `hermes/`

## 快速安装

```bash
# 为所有检测到的工具自动安装
./scripts/install.sh

# 安装特定的家庭范围工具
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool copilot
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool claude-code
./scripts/install.sh --tool codex
./scripts/install.sh --tool osaurus
./scripts/install.sh --tool hermes

# Gemini CLI needs generated integration files on a fresh clone
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli

# Qwen Code also needs generated SubAgent files on a fresh clone
./scripts/convert.sh --tool qwen
./scripts/install.sh --tool qwen
```

如果你安装了 OpenClaw 且网关已在运行, 安装后重启它:

```bash
openclaw gateway restart
```

对于项目范围的工具 such as OpenCode, Cursor, Aider, Windsurf, and Qwen
Code, 运行
the installer from your target project root as shown in the tool-specific
sections below.

## 重新生成集成文件

If you add or modify agents, 重新生成所有 integration files:

```bash
./scripts/convert.sh
```

---

## Claude Code

Agency 最初为 Claude Code 设计. Agents work natively
无需转换.

```bash
cp -r <category>/*.md ~/.claude/agents/
# or install everything at once:
./scripts/install.sh --tool claude-code
```

参见 [claude-code/README.md](claude-code/README.md) 了解更多详情.

---

## GitHub Copilot

Agency 也与 GitHub Copilot 原生工作. Agents can be copied
directly into `~/.github/agents/` and `~/.copilot/agents/` 无需转换.

```bash
./scripts/install.sh --tool copilot
```

参见 [github-copilot/README.md](github-copilot/README.md) 了解更多详情.

---

## Antigravity

技能安装到 `~/.gemini/config/skills/`. Each agent becomes
a separate skill 前缀为 `agency-` 以避免命名冲突.

```bash
./scripts/install.sh --tool antigravity
```

参见 [antigravity/README.md](antigravity/README.md) 了解更多详情.

---

## Gemini CLI

代理打包为 Gemini CLI 子代理.
子代理安装到 `~/.gemini/agents/`.
因为代理文件是生成的产物, 运行
`./scripts/convert.sh --tool gemini-cli` 从新克隆安装前.

```bash
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli
```

参见 [gemini-cli/README.md](gemini-cli/README.md) 了解更多详情.

---

## OpenCode

每个代理成为一个项目范围的 `.md` 文件在 `.opencode/agents/`.

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool opencode
```

参见 [opencode/README.md](opencode/README.md) 了解更多详情.

---

## OpenClaw

每个代理成为一个 OpenClaw 工作区 包含 `SOUL.md`, `AGENTS.md`,
and `IDENTITY.md`.

安装前，生成 OpenClaw 工作区:

```bash
./scripts/convert.sh --tool openclaw
```

然后安装它们:

```bash
./scripts/install.sh --tool openclaw
```

参见 [openclaw/README.md](openclaw/README.md) 了解更多详情.

---

## Cursor

Each agent becomes a `.mdc` rule file. 规则是项目范围的 — 运行 the
installer from your project root.

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool cursor
```

参见 [cursor/README.md](cursor/README.md) 了解更多详情.

---

## Aider

所有代理合并为一个 `CONVENTIONS.md` file that Aider
reads automatically 当它存在于你的项目根目录时.

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool aider
```

参见 [aider/README.md](aider/README.md) 了解更多详情.

---

## Windsurf

所有代理合并为一个 `.windsurfrules` file for your
project root.

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool windsurf
```

参见 [windsurf/README.md](windsurf/README.md) 了解更多详情.

---

## Kimi Code

每个代理都是 converted to a Kimi Code CLI 代理规范 (YAML format with
separate system prompt files). 代理安装到 `~/.config/kimi/agents/`.

因为 Kimi 代理文件从源 Markdown 生成, 运行
`./scripts/convert.sh --tool kimi` 从新克隆安装前.

```bash
./scripts/convert.sh --tool kimi
./scripts/install.sh --tool kimi
```

### Usage

After installation, use an agent with the `--agent-file` flag:

```bash
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml
```

Or in a specific project:

```bash
cd /your/project
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml \
     --work-dir /your/project
```

参见 [kimi/README.md](kimi/README.md) 了解更多详情.

---

## Qwen Code

每个代理成为一个项目范围的 `.md` SubAgent 文件在 `.qwen/agents/`.

从新克隆，首先生成 Qwen 文件:

```bash
./scripts/convert.sh --tool qwen
```

然后安装它们 from your project root:

```bash
cd /your/project && /path/to/agency-agents/scripts/install.sh --tool qwen
```

参见 [qwen/README.md](qwen/README.md) 了解更多详情.

---

## Codex

每个代理都是 converted into 一个独立的 Codex 自定义代理 TOML 文件 and
安装到 `~/.codex/agents/`.

Because Codex uses generated TOML 文件s rather than the source Markdown
directly, 运行 the converter 从新克隆安装前:

```bash
./scripts/convert.sh --tool codex
./scripts/install.sh --tool codex
```

参见 [codex/README.md](codex/README.md) 了解更多详情.
