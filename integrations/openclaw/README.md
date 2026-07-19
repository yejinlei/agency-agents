# OpenClaw Integration

OpenClaw agents are installed as workspaces 包含 `SOUL.md`, `AGENTS.md`,
and `IDENTITY.md` files. The installer copies each workspace into
`~/.openclaw/agency-agents/` and registers it when the `openclaw` CLI is
available.

安装前，生成 OpenClaw 工作区:

```bash
./scripts/convert.sh --tool openclaw
```

## Install

```bash
./scripts/install.sh --tool openclaw
```

## Activate an Agent

After installation, agents are available by `agentId` in OpenClaw sessions.

If the OpenClaw gateway is already 运行ning, 安装后重启它:

```bash
openclaw gateway restart
```

## Regenerate

```bash
./scripts/convert.sh --tool openclaw
```
