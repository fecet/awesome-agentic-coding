# Awesome Agentic Coding [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of frameworks, tools, and sandboxes for building AI agents that automate software engineering tasks — from code generation to automated bug fixes.

## Contents

- [Autonomous Coding Agents](#autonomous-coding-agents)
- [Interactive Code Assistants](#interactive-code-assistants)
- [Agent Development Frameworks](#agent-development-frameworks)
- [MCP Servers & Execution Sandboxes](#mcp-servers--execution-sandboxes)
- [Headless CI/CD & GitHub Actions](#headless-cicd--github-actions)
- [PydanticAI-based Projects](#pydanticai-based-projects)
- [Related](#related)
  - [Benchmarks & Evaluation](#benchmarks--evaluation)
  - [Integration Resources](#integration-resources)
  - [Similar Lists](#similar-lists)

---

## Autonomous Coding Agents

Headless agents for automated code modification, testing, and repository operations.

- [OpenHands](https://github.com/All-Hands-AI/OpenHands) ![Last Commit](https://img.shields.io/github/last-commit/All-Hands-AI/OpenHands) — Code agent with file editor, shell & browser tools; supports **headless** mode and GH Actions.
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) ![Last Commit](https://img.shields.io/github/last-commit/princeton-nlp/SWE-agent) — Issue→patch workflow; strong results on SWE-bench; YAML-configurable batch runs.
- [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) ![Last Commit](https://img.shields.io/github/last-commit/QwenLM/Qwen-Agent) — General agent framework often used as coding agent; code-interpreter, function-calling & MCP.
- [Trae-Agent](https://github.com/bytedance/trae-agent) ![Last Commit](https://img.shields.io/github/last-commit/bytedance/trae-agent) — General-purpose SWE agent with CLI, modular tools, multi-model support.
- [Plandex](https://github.com/plandex-ai/plandex) ![Last Commit](https://img.shields.io/github/last-commit/plandex-ai/plandex) — Terminal-first coding agent for multi-file, multi-step tasks.
- [TraceRoot AI](https://github.com/traceroot-ai/traceroot) ![Last Commit](https://img.shields.io/github/last-commit/traceroot-ai/traceroot) — Agents that help triage/fix production bugs from traces/logs to PRs.
- [DeepCode](https://github.com/HKUDS/DeepCode) ![Last Commit](https://img.shields.io/github/last-commit/HKUDS/DeepCode) — Multi-agent Paper2Code / Text2Web / Text2Backend (research → implementation).

---

## Interactive Code Assistants

Terminal/IDE assistants for pair programming or semi-autonomous development.

- [Claude Code](https://github.com/anthropics/claude-code) ![Last Commit](https://img.shields.io/github/last-commit/anthropics/claude-code) — Terminal TUI, plan mode, MCP tools; also works via GitHub mentions & IDEs.
- [OpenAI Codex CLI](https://github.com/openai/codex) ![Last Commit](https://img.shields.io/github/last-commit/openai/codex) — Local coding agent CLI (`npm i -g @openai/codex` / `brew install codex`), plus Actions.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) ![Last Commit](https://img.shields.io/github/last-commit/google-gemini/gemini-cli) — Google’s open-source terminal AI agent; ReAct loop + built-in tools + MCP.
- [GitHub Copilot CLI](https://github.com/github/copilot-cli) ![Last Commit](https://img.shields.io/github/last-commit/github/copilot-cli) — Agentic CLI for build/edit/debug/PR flows; integrates GitHub context & MCP.
- [OpenCode](https://github.com/sst/opencode) ![Last Commit](https://img.shields.io/github/last-commit/sst/opencode) — Provider-agnostic terminal coding agent with LSP; great for Neovim users.
- [Aider](https://github.com/paul-gauthier/aider) ![Last Commit](https://img.shields.io/github/last-commit/paul-gauthier/aider) — Git-integrated chat to edit code across multiple files.
- [Open Interpreter](https://github.com/openinterpreter/open-interpreter) ![Last Commit](https://img.shields.io/github/last-commit/openinterpreter/open-interpreter) — Local agent that runs Python/JS/Shell; terminal chat.
- [Roo Code (VS Code)](https://github.com/RooVetGit/Roo-Code) ![Last Commit](https://img.shields.io/github/last-commit/RooVetGit/Roo-Code) — VS Code autonomous agent with strong MCP ecosystem.
- [Cline](https://github.com/cline/cline) ![Last Commit](https://img.shields.io/github/last-commit/cline/cline) — VS Code agent to create/edit files, run commands, browse.
- [Cursor](https://www.cursor.sh/) — AI-first editor with inline edits & chat.
- [Windsurf](https://windsurf.com/) — Editor focused on agentic workflows.
- [Continue](https://github.com/continuedev/continue) ![Last Commit](https://img.shields.io/github/last-commit/continuedev/continue) — Open-source autopilot for VS Code/JetBrains/CLI; custom agents, MCP.
- [Potpie](https://github.com/potpie-ai/potpie) ![Last Commit](https://img.shields.io/github/last-commit/potpie-ai/potpie) — Context-aware assistant with codebase understanding.
- [Kode](https://github.com/shareAI-lab/Kode) ![Last Commit](https://img.shields.io/github/last-commit/shareAI-lab/Kode) — Community-driven Claude Code–style assistant。
- [Factory.ai](https://factory.ai/) — Enterprise agent platform; “Droids” automate refactors/migrations/incidents。

---

## Agent Development Frameworks

SDKs and frameworks for building code-aware agents with composable tools.

- [OpenAI Agents SDK (Python)](https://github.com/openai/openai-agents-python) ![Last Commit](https://img.shields.io/github/last-commit/openai/openai-agents-python) — Primitives: Agent, Tools, **Handoffs**, **Guardrails**, **Sessions**; tracing.
- [OpenAI Agents SDK (JS/TS)](https://github.com/openai/openai-agents-js) ![Last Commit](https://img.shields.io/github/last-commit/openai/openai-agents-js)
- [PydanticAI](https://github.com/pydantic/pydantic-ai) ![Last Commit](https://img.shields.io/github/last-commit/pydantic/pydantic-ai) — Type-safe agents, structured outputs, schema validation & observability。
- [AutoGen](https://github.com/microsoft/autogen) ![Last Commit](https://img.shields.io/github/last-commit/microsoft/autogen) — Multi-agent conversations + Docker-based code executors.
- [LangGraph](https://github.com/langchain-ai/langgraph) ![Last Commit](https://img.shields.io/github/last-commit/langchain-ai/langgraph) — Controllable agent graphs with state & persistence。
- [CrewAI](https://github.com/crewAIInc/crewAI) ![Last Commit](https://img.shields.io/github/last-commit/crewAIInc/crewAI) — Role-based, task/flow oriented multi-agent framework。
- [AgentScope](https://github.com/agentscope-ai/agentscope) ![Last Commit](https://img.shields.io/github/last-commit/agentscope-ai/agentscope) — Developer-centric AOP; runtime, studio, sandboxed tools。
- [Griptape](https://github.com/griptape-ai/griptape) ![Last Commit](https://img.shields.io/github/last-commit/griptape-ai/griptape) — Modular agents, tools, memory; good production ergonomics。
- [Haystack Agents](https://github.com/deepset-ai/haystack) ![Last Commit](https://img.shields.io/github/last-commit/deepset-ai/haystack) — GitHub tools for PRs/edits; solid integrations。
- [smolagents](https://github.com/huggingface/smolagents) ![Last Commit](https://img.shields.io/github/last-commit/huggingface/smolagents) — “Agents that think in code”, supports E2B/Modal/Docker.

---

## MCP Servers & Execution Sandboxes

Tooling to safely give agents capabilities (files, Python, browser, etc.) or isolated code execution.

- [Model Context Protocol — Python SDK](https://github.com/modelcontextprotocol/python-sdk) ![Last Commit](https://img.shields.io/github/last-commit/modelcontextprotocol/python-sdk)
- [Reference MCP Servers](https://github.com/modelcontextprotocol/servers) ![Last Commit](https://img.shields.io/github/last-commit/modelcontextprotocol/servers) — e.g. Filesystem server.
- [pydantic/mcp-run-python](https://github.com/pydantic/mcp-run-python) ![Last Commit](https://img.shields.io/github/last-commit/pydantic/mcp-run-python) — Run Python in a sandbox via MCP.
- [FastMCP](https://github.com/jlowin/fastmcp) ![Last Commit](https://img.shields.io/github/last-commit/jlowin/fastmcp) — Decorator-first way to ship MCP servers in Python.
- [E2B sandboxes](https://e2b.dev/) — Managed, isolated cloud sandboxes for code execution（有 LangGraph 集成见下文）。
- [AutoGen DockerCommandLineCodeExecutor](https://microsoft.github.io/autogen/0.2/docs/reference/coding/docker_commandline_code_executor/) — Run model-generated code in Docker.
- [OpenHands Local Runtime](https://docs.all-hands.dev/openhands/usage/runtimes/local) — Local (unsandboxed) runtime; also supports headless/CLI.

---

## Headless CI/CD & GitHub Actions

Run agents automatically on issues/PRs or scheduled tasks.

- [OpenAI **Codex Action**](https://github.com/openai/codex-action) — Securely run `codex exec` in Actions.
- [Anthropic **Claude Code Action**](https://github.com/anthropics/claude-code-action) / [base action](https://github.com/anthropics/claude-code-base-action) — Trigger by @claude in PRs/issues, or as pure automation.
- [OpenHands GitHub Action (docs)](https://docs.all-hands.dev/openhands/usage/run-openhands/github-action) — Label/mention driven issue resolution。
- [Gemini CLI Actions (beta)](https://github.com/google-github-actions/run-gemini-cli) — Use Gemini CLI in CI for triage/review。

---

## PydanticAI-based Projects

- **rune-code** — Terminal-first coding agent built on PydanticAI（PyPI: `rune-code`）。
- **mcp-run-python** — 见上文（Pydantic 维护），将 Python 执行暴露为 MCP 服务器，便于与任意客户端对接。
- 组合建议：**PydanticAI Agent** + **mcp-run-python** + **E2B/AutoGen Docker** → “无界面/可编排的编码代理”。

---

## Related

### Benchmarks & Evaluation
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) — Real-world issue→patch benchmark。
- SWE-bench 家族：**Verified / Lite / Multimodal / Live**（参见官网与榜单）。
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) / **mini-SWE-agent** 等参考实现与工具。

### Integration Resources
- [E2B + LangGraph](https://e2b.dev/docs/hello-world/langgraph)
- [OpenHands Headless Mode](https://docs.all-hands.dev/openhands/usage/run-openhands/headless-mode)
- [ToolHive](https://github.com/stacklok/toolhive) ![Last Commit](https://img.shields.io/github/last-commit/stacklok/toolhive) — 一键发现/部署常用 MCP 服务器。

### Similar Lists
- [sourcegraph/awesome-code-ai](https://github.com/sourcegraph/awesome-code-ai)
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)
- [jamesmurdza/awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools)
