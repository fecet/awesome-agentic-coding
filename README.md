# Awesome Agentic Coding [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of frameworks, tools, and sandboxes for building AI agents that automate software engineering tasks - from code generation to automated bug fixes.

## Contents

- [Autonomous Coding Agents](#autonomous-coding-agents)
- [Interactive Code Assistants](#interactive-code-assistants)
- [Agent Development Frameworks](#agent-development-frameworks)
- [Related](#related)

## Autonomous Coding Agents

Headless agents for automated code modification, testing, and repository operations.

- [OpenHands](https://github.com/All-Hands-AI/OpenHands) ![Last Commit](https://img.shields.io/github/last-commit/All-Hands-AI/OpenHands) - Code agent with built-in tools for file editing, shell, and browser. Supports headless mode and GitHub Actions for automated workflows.
- [SWE-agent](https://github.com/princeton-nlp/SWE-agent) ![Last Commit](https://img.shields.io/github/last-commit/princeton-nlp/SWE-agent) - Agent specialized in GitHub issue-to-patch workflow. Achieves SOTA on SWE-bench with customizable YAML configs and batch processing.
- [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) ![Last Commit](https://img.shields.io/github/last-commit/QwenLM/Qwen-Agent) - Integrated agent framework with Code Interpreter, Function Calling, and MCP support. Chinese ecosystem friendly.
- [Trae-Agent](https://github.com/bytedance/trae-agent) ![Last Commit](https://img.shields.io/github/last-commit/bytedance/trae-agent) - General-purpose software engineering agent with CLI, modular tools, and multi-model support (OpenAI/Anthropic).
- [Plandex](https://github.com/plandex-ai/plandex) ![Last Commit](https://img.shields.io/github/last-commit/plandex-ai/plandex) - Terminal-based AI coding agent for complex tasks spanning multiple files and steps.
- [TraceRoot AI](https://github.com/traceroot-ai/traceroot) ![Last Commit](https://img.shields.io/github/last-commit/traceroot-ai/traceroot) - AI agents that automatically fix production bugs.
- [DeepCode](https://github.com/HKUDS/DeepCode) ![Last Commit](https://img.shields.io/github/last-commit/HKUDS/DeepCode) - Multi-agent system for Paper2Code (research to implementation), Text2Web (frontend generation), and Text2Backend (server-side development).

## Interactive Code Assistants

Terminal and IDE-based assistants with conversational interfaces for pair programming.

- [Claude Code](https://github.com/anthropics/claude-code) ![Last Commit](https://img.shields.io/github/last-commit/anthropics/claude-code) - Anthropic's official CLI with interactive TUI for coding tasks, plan mode, and MCP tool integration.
- [Aider](https://github.com/paul-gauthier/aider) ![Last Commit](https://img.shields.io/github/last-commit/paul-gauthier/aider) - AI pair programming in your terminal. Git-integrated chat interface for editing code across multiple files.
- [OpenAI Codex CLI](https://github.com/openai/codex) ![Last Commit](https://img.shields.io/github/last-commit/openai/codex) - Lightweight coding agent built in Rust that runs locally, with support for GPT-5-Codex and agentic workflows.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) ![Last Commit](https://img.shields.io/github/last-commit/google-gemini/gemini-cli) - Google's terminal AI agent with 1M token context, multimodal capabilities, and MCP extensibility. Free tier with 60 req/min.
- [OpenCode](https://github.com/sst/opencode) ![Last Commit](https://img.shields.io/github/last-commit/sst/opencode) - Open-source terminal coding agent with LSP support, provider-agnostic (Anthropic/OpenAI/Google/local models), built by Neovim users.
- [Cursor](https://www.cursor.sh/) - AI-first code editor with built-in chat and inline editing capabilities.
- [Cline](https://github.com/cline/cline) ![Last Commit](https://img.shields.io/github/last-commit/cline/cline) - Autonomous coding agent that can create/edit files, execute commands, and use browser within VS Code.
- [Windsurf](https://windsurf.com/) - AI code editor focused on building autonomous agents with minimal human intervention.
- [Continue](https://github.com/continuedev/continue) ![Last Commit](https://img.shields.io/github/last-commit/continuedev/continue) - Open-source autopilot for VS Code and JetBrains with customizable AI models.
- [Potpie](https://github.com/potpie-ai/potpie) ![Last Commit](https://img.shields.io/github/last-commit/potpie-ai/potpie) - AI coding assistant with codebase understanding and context-aware suggestions.
- [GitHub Copilot CLI](https://github.com/github/copilot-cli) ![Last Commit](https://img.shields.io/github/last-commit/github/copilot-cli) - AI pair programmer that suggests code completions and entire functions.
- [Factory.ai](https://factory.ai/) - Enterprise agent platform with "Droids" that automate refactors, migrations, and incident response across IDE, terminal, and project management tools.

## Agent Development Frameworks

SDKs and frameworks for building custom code-aware agents with composable tools.

- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) ![Last Commit](https://img.shields.io/github/last-commit/openai/openai-agents-python) - Official SDK with primitives: Agent, Tools, Handoffs, Guardrails, and Sessions. Python-first with lightweight orchestration.
- [PydanticAI](https://github.com/pydantic/pydantic-ai) ![Last Commit](https://img.shields.io/github/last-commit/pydantic/pydantic-ai) - Type-safe agent framework emphasizing structured outputs and schema validation. Strong observability support.
- [AutoGen](https://github.com/microsoft/autogen) ![Last Commit](https://img.shields.io/github/last-commit/microsoft/autogen) - Multi-agent conversations with `DockerCommandLineCodeExecutor` for safe code execution.
- [LangGraph](https://github.com/langchain-ai/langgraph) ![Last Commit](https://img.shields.io/github/last-commit/langchain-ai/langgraph) - Build controllable agent workflows as directed graphs with state management.
- [CrewAI](https://github.com/crewAIInc/crewAI) ![Last Commit](https://img.shields.io/github/last-commit/crewAIInc/crewAI) - Role-based multi-agent framework organized by tasks and flows. Backend automation friendly.
- [AgentScope](https://github.com/agentscope-ai/agentscope) ![Last Commit](https://img.shields.io/github/last-commit/agentscope-ai/agentscope) - Developer-centric async multi-agent framework with MCP, parallel tools, planning, and tracing.
- [Griptape](https://github.com/griptape-ai/griptape) ![Last Commit](https://img.shields.io/github/last-commit/griptape-ai/griptape) - Modular framework with chain-of-thought reasoning, tools, and memory for production workflows.
- [Haystack Agents](https://github.com/deepset-ai/haystack) ![Last Commit](https://img.shields.io/github/last-commit/deepset-ai/haystack) - Built-in GitHub editing/PR tools for CI/CD integration. Strong tool ecosystem.
- [smolagents](https://github.com/huggingface/smolagents) ![Last Commit](https://img.shields.io/github/last-commit/huggingface/smolagents) - Minimalist agent library where agents "think in code". Native support for E2B/Docker/Modal sandboxes.

## Related

### Benchmarks & Evaluation

- [SWE-bench](https://github.com/SWE-bench/SWE-bench) ![Last Commit](https://img.shields.io/github/last-commit/SWE-bench/SWE-bench) - Benchmark for evaluating agents on real-world GitHub issues.

### Integration Resources

- [E2B + LangGraph](https://e2b.dev/docs/hello-world/langgraph) - Integrate code execution with graph-based agents.
- [OpenHands Headless Mode](https://docs.all-hands.dev/usage/how-to/headless-mode) - Run OpenHands without UI for CI/CD pipelines.
- [ToolHive](https://github.com/stacklok/toolhive) ![Last Commit](https://img.shields.io/github/last-commit/stacklok/toolhive) - Find and deploy the right MCP server for your task with one click.

### Similar Lists

- [awesome-code-ai](https://github.com/sourcegraph/awesome-code-ai) ![Last Commit](https://img.shields.io/github/last-commit/sourcegraph/awesome-code-ai) - Comprehensive list of AI coding tools including completion, refactoring, and review.
- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) ![Last Commit](https://img.shields.io/github/last-commit/e2b-dev/awesome-ai-agents) - List of AI autonomous agents across domains.
- [awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools) ![Last Commit](https://img.shields.io/github/last-commit/jamesmurdza/awesome-ai-devtools) - Curated list of AI-powered developer tools.

---
