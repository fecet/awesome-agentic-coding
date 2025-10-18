# Awesome Agentic Coding [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of frameworks, tools, and sandboxes for building AI agents that automate software engineering tasks - from code generation to automated bug fixes.

## Contents

- [Autonomous Coding Agents](#autonomous-coding-agents)
- [Interactive Code Assistants](#interactive-code-assistants)
- [Agent Development Frameworks](#agent-development-frameworks)
- [Related](#related)

## Autonomous Coding Agents

Headless agents for automated code modification, testing, and repository operations.

- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Code agent with built-in tools for file editing, shell, and browser. Supports headless mode and GitHub Actions for automated workflows.
- [SWE-agent](https://swe-agent.com/latest/) - Agent specialized in GitHub issue-to-patch workflow. Achieves SOTA on SWE-bench with customizable YAML configs and batch processing.
- [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) - Integrated agent framework with Code Interpreter, Function Calling, and MCP support. Chinese ecosystem friendly.
- [Trae-Agent](https://github.com/bytedance/trae-agent) - General-purpose software engineering agent with CLI, modular tools, and multi-model support (OpenAI/Anthropic).
- [Plandex](https://github.com/plandex-ai/plandex) - Terminal-based AI coding agent for complex tasks spanning multiple files and steps.
- [Blinky](https://github.com/seahyinghang8/blinky) - Debugging agent that automatically identifies and fixes bugs in your code.
- [Pixee](https://pixee.ai) - Automated security and code quality bot that creates merge-ready pull requests with fixes.
- [TraceRoot AI](https://github.com/traceroot-ai/traceroot) - AI agents that automatically fix production bugs.
- [Factory.ai](https://factory.ai/) - Enterprise agent platform with "Droids" that automate refactors, migrations, and incident response across IDE, terminal, and project management tools.
- [DeepCode](https://github.com/HKUDS/DeepCode) - Multi-agent system for Paper2Code (research to implementation), Text2Web (frontend generation), and Text2Backend (server-side development).

## Interactive Code Assistants

Terminal and IDE-based assistants with conversational interfaces for pair programming.

- [Claude Code](https://docs.claude.com/en/docs/claude-code) - Anthropic's official CLI with interactive TUI for coding tasks, plan mode, and MCP tool integration.
- [Aider](https://github.com/paul-gauthier/aider) - AI pair programming in your terminal. Git-integrated chat interface for editing code across multiple files.
- [OpenAI Codex CLI](https://github.com/openai/codex) - Lightweight coding agent built in Rust that runs locally, with support for GPT-5-Codex and agentic workflows.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google's terminal AI agent with 1M token context, multimodal capabilities, and MCP extensibility. Free tier with 60 req/min.
- [OpenCode](https://github.com/sst/opencode) - Open-source terminal coding agent with LSP support, provider-agnostic (Anthropic/OpenAI/Google/local models), built by Neovim users.
- [Cursor](https://www.cursor.sh/) - AI-first code editor with built-in chat and inline editing capabilities.
- [Cline](https://cline.bot/) - Autonomous coding agent that can create/edit files, execute commands, and use browser within VS Code.
- [Windsurf](https://windsurf.com/) - AI code editor focused on building autonomous agents with minimal human intervention.
- [Continue](https://continue.dev/) - Open-source autopilot for VS Code and JetBrains with customizable AI models.
- [Potpie](https://potpie.ai) - AI coding assistant with codebase understanding and context-aware suggestions.
- [GitHub Copilot](https://github.com/features/copilot) - AI pair programmer that suggests code completions and entire functions.

## Agent Development Frameworks

SDKs and frameworks for building custom code-aware agents with composable tools.

- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) - Official SDK with primitives: Agent, Tools, Handoffs, Guardrails, and Sessions. Python-first with lightweight orchestration.
- [PydanticAI](https://ai.pydantic.dev/) - Type-safe agent framework emphasizing structured outputs and schema validation. Strong observability support.
- [AutoGen](https://microsoft.github.io/autogen/stable/) - Multi-agent conversations with `DockerCommandLineCodeExecutor` for safe code execution.
- [LangGraph](https://langchain-ai.github.io/langgraph/concepts/why-langgraph/) - Build controllable agent workflows as directed graphs with state management.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Role-based multi-agent framework organized by tasks and flows. Backend automation friendly.
- [AgentScope](https://github.com/agentscope-ai/agentscope) - Developer-centric async multi-agent framework with MCP, parallel tools, planning, and tracing.
- [Griptape](https://github.com/griptape-ai/griptape) - Modular framework with chain-of-thought reasoning, tools, and memory for production workflows.
- [Haystack Agents](https://docs.haystack.deepset.ai/docs/agent) - Built-in GitHub editing/PR tools for CI/CD integration. Strong tool ecosystem.
- [smolagents](https://github.com/huggingface/smolagents) - Minimalist agent library where agents "think in code". Native support for E2B/Docker/Modal sandboxes.

## Related

### Benchmarks & Evaluation

- [SWE-bench](https://www.swebench.com/) - Benchmark for evaluating agents on real-world GitHub issues.

### Integration Resources

- [E2B + LangGraph](https://e2b.dev/docs/hello-world/langgraph) - Integrate code execution with graph-based agents.
- [OpenHands Headless Mode](https://docs.all-hands.dev/usage/how-to/headless-mode) - Run OpenHands without UI for CI/CD pipelines.
- [ToolHive](https://github.com/stacklok/toolhive) - Find and deploy the right MCP server for your task with one click.

### Similar Lists

- [awesome-code-ai](https://github.com/sourcegraph/awesome-code-ai) - Comprehensive list of AI coding tools including completion, refactoring, and review.
- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - List of AI autonomous agents across domains.
- [awesome-ai-devtools](https://github.com/jamesmurdza/awesome-ai-devtools) - Curated list of AI-powered developer tools.

---

## Contributing

Contributions welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.
