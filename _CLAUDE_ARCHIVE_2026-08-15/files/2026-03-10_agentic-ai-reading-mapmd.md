---
original_path: "/mnt/user-data/outputs/agentic-ai-reading-map.md"
source_conversation: "Systems design and conceptualization career path"
created: 2026-03-10
trunk: BLACK
kind: generated-file
---

# Agentic AI Systems Development
## Part 2: A Broad-Stroke Reading Map and Learning Curriculum

> **The Craft in One Sentence:** Designing, orchestrating, and deploying systems in which AI agents autonomously plan, reason, use tools, and collaborate to accomplish complex goals — without a human directing every step.

---

## Table of Contents

1. [What "Agentic AI" Actually Means](#1-what-agentic-ai-actually-means)
2. [The Field Map](#2-the-field-map)
3. [Tier 1 — Foundational AI Literacy](#3-tier-1--foundational-ai-literacy)
4. [Tier 2 — Large Language Models & Prompt Engineering](#4-tier-2--large-language-models--prompt-engineering)
5. [Tier 3 — Agentic Architecture & Orchestration](#5-tier-3--agentic-architecture--orchestration)
6. [Tier 4 — Memory, Tools & Multi-Agent Systems](#6-tier-4--memory-tools--multi-agent-systems)
7. [Tier 5 — Evaluation, Safety & Reliability](#7-tier-5--evaluation-safety--reliability)
8. [Tier 6 — Applied & Production Agentic Systems](#8-tier-6--applied--production-agentic-systems)
9. [Adjacent Disciplines Worth Knowing](#9-adjacent-disciplines-worth-knowing)
10. [Primary Resources: Papers, Repos & Living Docs](#10-primary-resources-papers-repos--living-docs)
11. [Suggested Learning Sequence](#11-suggested-learning-sequence)
12. [Key Vocabulary to Internalize](#12-key-vocabulary-to-internalize)

---

## 1. What "Agentic AI" Actually Means

Most people's exposure to AI is **reactive** — you prompt, it responds. Agentic AI is fundamentally different:

| Reactive AI | Agentic AI |
|---|---|
| Single turn — input → output | Multi-step — plan → act → observe → replan |
| Stateless between turns | Maintains memory across steps |
| Human directs every action | Agent decides its own next action |
| One model | Often multiple specialized agents |
| Tool use is optional | Tool use is structural |

An **agent** is any AI system that: perceives its environment, maintains some form of state or memory, selects actions, executes them through tools, and updates based on results — in a loop, toward a goal.

**Agentic AI development** is the discipline of designing, building, evaluating, and deploying these systems reliably. It sits at the intersection of:
- AI/ML engineering
- Distributed systems design
- Cognitive architecture
- Software engineering
- Reliability engineering

---

## 2. The Field Map

```
                    ┌─────────────────────────────┐
                    │     AGENTIC AI STACK         │
                    └─────────────────────────────┘

  Layer 5: EVALUATION & SAFETY      ← Is it doing what we intended? Safely?
  Layer 4: MULTI-AGENT SYSTEMS      ← Agents coordinating with agents
  Layer 3: SINGLE AGENT LOOP        ← Plan → Act → Observe → Reflect → Repeat
  Layer 2: TOOL USE & MEMORY        ← How agents reach outside themselves
  Layer 1: FOUNDATION MODELS        ← The reasoning engine underneath
  Layer 0: AI/ML FUNDAMENTALS       ← The math and concepts underneath that
```

You don't need to master Layer 0 to work at Layers 3–5. But you need *literacy* at every layer to design systems that don't fail mysteriously.

---

## 3. Tier 1 — Foundational AI Literacy

*The minimum viable knowledge base. Non-negotiable before moving up the stack.*

---

### **Artificial Intelligence: A Modern Approach** — Russell & Norvig
> The definitive AI textbook. Dense, comprehensive, and the standard reference for the entire field. You don't read this cover to cover — you use it as a map and reference.

- **Focus chapters:** Intelligent Agents (Ch. 2), Search (Ch. 3–4), Knowledge Representation (Ch. 7–9), Planning (Ch. 10–11), Learning (Ch. 19–21)
- **Why it matters:** The formal definition of an *agent*, a *percept*, an *action*, an *environment*, and a *goal* all come from here. This vocabulary is load-bearing.

---

### **The Alignment Problem** — Brian Christian
> A deeply readable examination of what happens when AI systems optimize for the wrong thing — and the researchers trying to fix it.

- **Why it matters:** Before you build agentic systems, you need to viscerally understand why specification (telling a system *exactly* what you want) is the hardest problem in the field. Every agentic system you build will face this.

---

### **Grokking Deep Learning** — Andrew Trask
> Hands-on, code-first introduction to neural networks without requiring a math PhD.

- **Why it matters:** You need a working mental model of *how* these models reason (or fail to). You're not becoming an ML researcher — but you need to know enough to diagnose when a model is the wrong tool.

---

### **Fast.ai Practical Deep Learning for Coders** *(free course, fast.ai)*
> The best practical entry point to modern ML. Top-down, code-first, zero fluff.

- **Why it matters:** Gets you to working intuition faster than any book. Treat this as the lab component of your Tier 1 reading.

---

## 4. Tier 2 — Large Language Models & Prompt Engineering

*LLMs are the reasoning engine of most agentic systems today. You must understand them deeply — not as magic boxes, but as probabilistic reasoning systems with specific failure modes.*

---

### **"Attention Is All You Need"** — Vaswani et al. (2017) *(paper)*
> The original transformer paper. The architecture that underlies GPT, Claude, Gemini, and every major LLM.

- **Why it matters:** Read it once. Not for the math — for the conceptual model. Understanding *attention* gives you intuition for why LLMs are good at some things and systematically bad at others.
- **Where:** arxiv.org/abs/1706.03762

---

### **"Language Models are Few-Shot Learners"** — Brown et al. / GPT-3 paper (2020) *(paper)*
> The paper that introduced in-context learning and demonstrated that scale produces emergent capabilities.

- **Why it matters:** Establishes why prompting works — and what its limits are. The conceptual ancestor of everything in prompt engineering.
- **Where:** arxiv.org/abs/2005.14165

---

### **Prompt Engineering Guide** — DAIR.AI *(free, promptingguide.ai)*
> The most comprehensive structured guide to prompt engineering techniques: zero-shot, few-shot, chain-of-thought, self-consistency, ReAct, and more.

- **Why it matters:** Prompt engineering is the lowest-level control surface for agentic systems. Mastery here directly improves every agent you build.

---

### **"Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"** — Wei et al. (2022) *(paper)*
> The paper that demonstrated that asking models to show their work dramatically improves performance on complex tasks.

- **Why it matters:** CoT is structural to how agents reason. Understanding *why* it works informs how you design agent prompts and task decomposition.
- **Where:** arxiv.org/abs/2201.11903

---

### **"ReAct: Synergizing Reasoning and Acting in Language Models"** — Yao et al. (2022) *(paper)*
> The foundational paper for the Reason + Act loop that underlies most modern agent architectures.

- **Why it matters:** ReAct is the direct ancestor of tool-using agents. This single paper explains why agents alternate between thinking and doing — the core loop.
- **Where:** arxiv.org/abs/2210.03629

---

## 5. Tier 3 — Agentic Architecture & Orchestration

*How to design the actual systems — the loops, the architectures, the orchestration patterns.*

---

### **"A Survey on Large Language Model based Autonomous Agents"** — Wang et al. (2023) *(paper)*
> The most comprehensive academic survey of the agentic AI landscape. Covers architecture patterns, memory types, tool use, planning methods, and evaluation.

- **Why it matters:** This is the field's map. Read it early, return to it often. Every pattern you'll encounter in practice is named and contextualized here.
- **Where:** arxiv.org/abs/2308.11432

---

### **LangChain Documentation & Conceptual Guides** *(langchain.com/docs)*
> LangChain is the dominant framework for building LLM-powered applications and agents. Its documentation doubles as a conceptual curriculum.

- **Focus sections:** LCEL (LangChain Expression Language), Agents, Tools, Memory, Retrieval
- **Why it matters:** Even if you don't use LangChain directly, its abstractions — chains, agents, tools, retrievers — have become the lingua franca of the field.

---

### **LlamaIndex Documentation** *(docs.llamaindex.ai)*
> The leading framework for building knowledge-augmented agents. Specializes in connecting LLMs to external data sources.

- **Why it matters:** Most real agentic systems need to reason over documents, databases, or knowledge graphs. LlamaIndex is where that architecture lives.

---

### **"Cognitive Architectures for Language Agents"** — Sumers et al. (2023) *(paper)*
> A framework paper that maps agentic AI onto classical cognitive architecture research (ACT-R, SOAR). Introduces memory taxonomy and action space design.

- **Why it matters:** Gives you a principled vocabulary for agent design — not just frameworks and libraries, but *why* agents are structured the way they are.
- **Where:** arxiv.org/abs/2309.02427

---

### **"HuggingGPT / TaskMatrix"** — Microsoft Research papers *(2023)*
> Early demonstrations of using LLMs as orchestrators that delegate to specialized models/tools.

- **Why it matters:** Establishes the **orchestrator pattern** — the most important architectural pattern in production agentic systems today.

---

## 6. Tier 4 — Memory, Tools & Multi-Agent Systems

*The advanced layer. Where single agents become systems, and where the hard engineering problems live.*

---

### **"MemGPT: Towards LLMs as Operating Systems"** — Packer et al. (2023) *(paper)*
> Proposes treating LLM context windows like OS memory — with paging, hierarchical storage, and self-directed memory management.

- **Why it matters:** Memory is the hardest unsolved problem in production agentic systems. MemGPT is the most principled treatment of it.
- **Where:** arxiv.org/abs/2310.08560

---

### **"Generative Agents: Interactive Simulacra of Human Behavior"** — Park et al. / Stanford (2023) *(paper)*
> The Stanford paper that simulated a town of 25 AI agents with persistent memory, daily planning, and emergent social behavior.

- **Why it matters:** The clearest demonstration of what multi-agent systems with memory can produce — and the architectural patterns that make it work. Directly relevant to any creative/IP system.
- **Where:** arxiv.org/abs/2304.03442

---

### **AutoGen Documentation & Papers** — Microsoft Research *(microsoft.github.io/autogen)*
> Microsoft's framework for multi-agent conversation systems. Introduces the **conversable agent** pattern and group chat orchestration.

- **Why it matters:** AutoGen is the leading framework for multi-agent systems. Its design patterns — agent roles, group chat, human-in-the-loop — are directly applicable to production systems.

---

### **"OpenAgents: An Open Platform for Language Agents in the Wild"** — Chen et al. (2023) *(paper)*
> Documents three production-grade agents (data analysis, web browsing, tool use) with real-world deployment lessons.

- **Why it matters:** The gap between research agents and production agents is enormous. This paper is honest about what breaks in the real world.

---

### **"Tool Learning with Foundation Models"** — Qin et al. (2023) *(paper)*
> Comprehensive survey of how LLMs learn to use tools — APIs, code interpreters, search engines, databases.

- **Why it matters:** Tool use is what gives agents reach. Understanding how it works — and fails — is structural to agent design.
- **Where:** arxiv.org/abs/2304.08354

---

## 7. Tier 5 — Evaluation, Safety & Reliability

*The most under-studied and most critical layer. Agentic systems that aren't evaluated rigorously will fail in production in ways that are hard to diagnose.*

---

### **"Evaluating Large Language Models: A Comprehensive Survey"** — Chang et al. (2023) *(paper)*
> Maps the landscape of LLM evaluation — benchmarks, methodologies, failure modes, and open problems.

- **Why it matters:** You cannot improve what you cannot measure. This survey teaches you how to think about evaluation as a design practice, not an afterthought.

---

### **"AgentBench: Evaluating LLMs as Agents"** — Liu et al. (2023) *(paper)*
> A benchmark specifically for evaluating agents across diverse environments: web, database, operating system, games.

- **Why it matters:** Establishes the standard evaluation framework for agentic systems. Your Case Study layer needs this vocabulary.
- **Where:** arxiv.org/abs/2308.03688

---

### **"Constitutional AI: Harmlessness from AI Feedback"** — Anthropic (2022) *(paper)*
> Anthropic's approach to training models to be helpful, harmless, and honest using AI-generated feedback.

- **Why it matters:** Safety is not optional in agentic systems. Agents that can take real-world actions (send emails, execute code, modify files) need principled safety design.
- **Where:** anthropic.com/research

---

### **"Failure Modes in Machine Learning"** — Microsoft *(security.microsoft.com)*
> A taxonomy of how ML systems fail — from data poisoning to model inversion to prompt injection.

- **Why it matters:** Agentic systems have a dramatically larger attack surface than reactive models. This taxonomy is the starting point for threat modeling your systems.

---

### **Reliable Machine Learning** — Cathy Chen et al.
> O'Reilly book on building ML systems that actually work in production — monitoring, testing, drift detection, incident response.

- **Why it matters:** The operational layer that most AI curricula skip entirely. Agents in production need observability, fallback logic, and incident runbooks.

---

## 8. Tier 6 — Applied & Production Agentic Systems

*Where the rubber meets the road. Real systems, real architecture decisions, real failure modes.*

---

### **"The Agent Protocol"** — AI Engineer Foundation *(agentprotocol.ai)*
> An emerging standard for agent-to-agent communication and tool interfaces. Think of it as the HTTP of agentic systems.

- **Why it matters:** As multi-agent systems mature, interoperability becomes critical. The Agent Protocol is the field's attempt to standardize how agents talk to each other and to tools.

---

### **Building LLM Powered Applications** — Valentina Alto
> A practical, code-forward book on production LLM application architecture — RAG systems, agent loops, memory, evaluation.

- **Why it matters:** Bridges the gap between reading papers and actually shipping systems. The most applied text in the stack.

---

### **"LLM Powered Autonomous Agents"** — Lilian Weng / OpenAI (2023) *(blog post)*
> One of the most cited technical blog posts in the field. Synthesizes planning, memory, and tool use into a unified agent architecture model.

- **Why it matters:** Short, dense, and precise. An essential reference that most practitioners have read multiple times.
- **Where:** lilianweng.github.io/posts/2023-06-23-agent/

---

### **Simon Willison's Blog** *(simonwillison.net)*
> The best practitioner blog in the LLM/agent space. Willison documents real experiments, failure modes, and architectural decisions with unusual clarity.

- **Why it matters:** The field moves faster than books. Willison's blog is the closest thing to a living textbook for applied LLM engineering.

---

### **Anthropic's Model Specification & Prompt Library** *(anthropic.com/research + docs.anthropic.com)*
> Anthropic's public documentation on how Claude is designed to behave, plus their prompt engineering guides.

- **Why it matters:** If you're building on Claude (relevant given your Bold Venture X context), understanding the model's design philosophy directly informs how you architect agents on top of it.

---

## 9. Adjacent Disciplines Worth Knowing

| Discipline | Entry Point | Why It Matters |
|---|---|---|
| **Retrieval-Augmented Generation (RAG)** | LlamaIndex docs + "RAG Survey" paper (2023) | How agents access external knowledge without fine-tuning |
| **Vector Databases** | Pinecone / Weaviate documentation | The storage layer for agent memory and knowledge retrieval |
| **Workflow Orchestration** | Temporal.io docs, Prefect docs | How to make agent loops reliable, retryable, and observable |
| **Prompt Injection & Security** | Riley Goodside's work, promptinjection.com | The primary attack vector against deployed agents |
| **Knowledge Graphs & Ontologies** | Neo4j documentation | Structured memory and reasoning beyond vector similarity |
| **Reinforcement Learning from Human Feedback (RLHF)** | "Learning to summarize with human feedback" — OpenAI | How models are trained to follow agent-style instructions |
| **Model Context Protocol (MCP)** | Anthropic MCP specification | The emerging standard for connecting agents to tools and data sources |

---

## 10. Primary Resources: Papers, Repos & Living Docs

### Must-Follow Paper Lists
- **Awesome LLM Agents** — github.com/hyp1231/awesome-llm-agents
- **Awesome AI Agents** — github.com/e2b-dev/awesome-ai-agents
- **The AI Engineer Newsletter** — aiEngineer.fyi

### Must-Follow Researchers
| Name | Affiliation | Focus |
|---|---|---|
| Lilian Weng | OpenAI | Agent architecture, alignment |
| Yao Fu | University of Edinburgh | LLM reasoning, planning |
| Shunyu Yao | Princeton / OpenAI | ReAct, tree-of-thought |
| Andrew Ng | DeepLearning.AI | Applied AI, agentic workflows |
| Harrison Chase | LangChain | Applied agent frameworks |

### Must-Know Frameworks (hands-on)
| Framework | Use Case |
|---|---|
| **LangChain** | General agent and chain orchestration |
| **LlamaIndex** | Knowledge-augmented agents, RAG |
| **AutoGen** | Multi-agent conversation systems |
| **CrewAI** | Role-based multi-agent teams |
| **DSPy** | Programmatic prompt optimization |
| **Semantic Kernel** | Microsoft's enterprise agent SDK |

---

## 11. Suggested Learning Sequence

**Phase 1 — AI Literacy (Months 1–2)**
1. *The Alignment Problem* — Christian (read first, sets the stakes)
2. Fast.ai Practical Deep Learning *(course, parallel with reading)*
3. *Grokking Deep Learning* — Trask
4. Prompt Engineering Guide — DAIR.AI *(promptingguide.ai)*

**Phase 2 — LLM Mechanics (Months 2–3)**
5. "Attention Is All You Need" — Vaswani et al.
6. "Chain-of-Thought Prompting" — Wei et al.
7. "ReAct" — Yao et al.
8. Lilian Weng's "LLM Powered Autonomous Agents" blog post

**Phase 3 — Agent Architecture (Months 3–5)**
9. "A Survey on LLM-based Autonomous Agents" — Wang et al.
10. "Cognitive Architectures for Language Agents" — Sumers et al.
11. LangChain conceptual documentation *(hands-on parallel)*
12. LlamaIndex conceptual documentation *(hands-on parallel)*

**Phase 4 — Multi-Agent & Memory (Months 5–7)**
13. "Generative Agents" — Park et al.
14. "MemGPT" — Packer et al.
15. AutoGen documentation + experiments
16. CrewAI documentation + experiments

**Phase 5 — Evaluation & Production (Months 7–9)**
17. "AgentBench" — Liu et al.
18. *Reliable Machine Learning* — Chen et al.
19. *Building LLM Powered Applications* — Alto
20. Simon Willison's blog *(ongoing)*

---

## 12. Key Vocabulary to Internalize

| Term | Meaning |
|---|---|
| **Agent** | An AI system that perceives, decides, acts, and updates in a loop toward a goal |
| **ReAct Loop** | Reason → Act → Observe → Reason cycle; the core agent pattern |
| **Tool Use** | An agent's ability to call external functions, APIs, code interpreters, or search |
| **Orchestrator** | An agent (or system) that directs other agents to complete subtasks |
| **Subagent** | An agent that receives tasks from an orchestrator and executes them |
| **Context Window** | The maximum amount of text an LLM can process at once — the agent's working memory |
| **RAG** | Retrieval-Augmented Generation — giving agents access to external knowledge stores |
| **Vector Embedding** | A numerical representation of text that enables semantic similarity search |
| **Few-Shot Prompting** | Providing examples in the prompt to guide model behavior |
| **Chain-of-Thought (CoT)** | Prompting the model to reason step-by-step before answering |
| **Self-Consistency** | Running the same reasoning multiple times and taking the majority answer |
| **Grounding** | Connecting an agent's outputs to verifiable real-world facts or data |
| **Hallucination** | When a model generates confident, plausible, but false information |
| **Prompt Injection** | An attack where malicious content in the environment hijacks agent behavior |
| **Human-in-the-Loop** | A design pattern where humans approve agent actions at defined checkpoints |
| **MCP** | Model Context Protocol — standard for connecting agents to tools and data |
| **Agentic Workflow** | A multi-step, AI-driven process with branching logic and tool use |
| **Eval** | Shorthand for evaluation — the systematic testing of model/agent performance |

---

*Part 3 will map the synthesis: where Systems Design methodology meets Agentic AI architecture — and the projects that build mastery at their intersection.*
