# M0 Architecture Decisions

---

## FastAPI

**What it is:**

- FastAPI is a modern Python web framework for building REST APIs.
- Built on top of Starlette (async web layer) and Pydantic (data validation), it
  auto-generates interactive API docs at `/docs` directly from type annotations, zero extra configuration needed.

**What problem it solves:**

- Episteme needs a web layer that can handle slow, concurrent operations:
  querying Neo4j, calling Ollama, searching ChromaDB, without blocking.
- A synchronous framework handles these one at a time. An async framework
  handles them concurrently. For an ML application, that difference matters.

**The alternative:**

- Flask: the most popular Python web framework. Mature, widely documented,
  and simpler to get started with.

**Why FastAPI over Flask:**

- Flask is synchronous by default. Every LLM call, every vector search, every
  graph traversal in Episteme involves waiting, and those waits stack up in a
  synchronous framework.
- FastAPI async support means those waits happen concurrently instead of sequentially.
- Pydantic integration means every request and response is automatically
  validated and documented, which becomes valuable as the API surface grows
  across ten milestones.

**Honest trade-off:**

- Flask has a larger ecosystem of extensions.
- FastAPI is newer so some edge cases have less community documentation, but
  the async and validation benefits outweigh that for this specific use case.

---

## Poetry

**What it is:**

- Poetry is a Python dependency management tool.
- It resolves dependencies, creates isolated virtual environments, and generates
  a lockfile (`poetry.lock`) that records the exact version of every package
  and every sub-dependency installed.

**What problem it solves:**

- ML projects have complex, fragile dependency trees. Sentence-transformers,
  LangChain, spaCy, and ChromaDB each pull in dozens of sub-dependencies.
- pip with a `requirements.txt` will silently install incompatible versions
  and the conflict only shows up at runtime.
- Poetry detects conflicts before installation and guarantees that anyone who
  clones the repo gets an identical environment.

**The alternative:**

- pip plus `requirements.txt`, which is the standard Python approach.
- Simple, universally understood, no additional tooling required.

**Why Poetry over pip:**

- First, the lockfile:
  - `poetry.lock` pins every transitive dependency, not just the top-level ones.
- Second, dependency resolution:
  - Poetry solves the full dependency graph before installing anything and
    raises an error on conflicts rather than silently breaking things.
- Third, dev vs prod separation:
  - Testing tools like pytest and jupyter live in
    `[tool.poetry.group.dev.dependencies]` and never end up in production.
  - pip has no clean equivalent without maintaining multiple requirements
    files manually.

**Honest trade-off:**

- Poetry adds tooling that contributors need to install before working on the
  project. pip requires nothing beyond Python itself.
- Worth documenting clearly in the README for anyone cloning the repo.

---

## Neo4j

**What it is:**

- Neo4j is a graph database.
  - Instead of storing data in tables with rows and columns, it stores nodes
    (entities) and edges (relationships between them).
  - Queries are written in Cypher, a language designed specifically for
    traversing graph structures.
  - The Community Edition is free and runs locally via Docker.

**What problem it solves:**

- Scientific knowledge is inherently a graph. A paper uses a method, a method
  gets evaluated on a dataset, an author is affiliated with an institution,
  a concept builds on another concept.
- Representing this in a relational database means complex JOIN queries that
  get exponentially slower as the data grows.
- Neo4j traverses relationships in constant time regardless of graph size.

**The alternative:**

- PostgreSQL with a relational schema, or SQLite for something lighter.
- Both are well-understood, widely used, and require no additional infrastructure.

**Why Neo4j over a relational database:**

- The core query in Episteme is finding all papers related to concept X, their
  authors, and the methods those papers share. That is a multi-hop graph traversal.
- In SQL that becomes multiple nested JOINs across several tables.
  In Cypher it is one readable query.
- The data model also maps naturally. Nodes and edges in Neo4j directly
  represent the entities and relationships extracted from papers, which means
  no translation layer between the extraction pipeline and the database.

**Honest trade-off:**

- Neo4j requires Docker to run locally and Cypher is a new query language to
  learn on top of everything else.
- A relational database would have been simpler to set up for anyone already
  comfortable with SQL.
- The complexity is justified because graph traversal is not a peripheral
  feature of Episteme. It is the core of what makes GraphRAG possible.

---

## ChromaDB

**What it is:**

- ChromaDB is an open-source vector database.
- It stores vector embeddings, which are numerical representations of text,
  and supports fast approximate nearest neighbor search to find the most
  semantically similar chunks for a given query.
- Runs entirely in-process with Python, persists to disk, no separate server
  required.

**What problem it solves:**

- Semantic search requires comparing a query embedding against potentially
  hundreds of thousands of document embeddings.
- Brute-force comparison with numpy is too slow at scale.
- ChromaDB indexes embeddings using HNSW (Hierarchical Navigable Small World
  graphs) so similarity search stays fast even over large corpora.

**The alternative:**

- Pinecone: a managed vector database service. Production-grade, scalable,
  requires no infrastructure management.
- Weaviate and Qdrant are other open-source alternatives with more features.

**Why ChromaDB over Pinecone:**

- Pinecone is a paid cloud service.
- Episteme is designed to run entirely locally with no external API costs and
  no data leaving the machine. That is a deliberate architectural choice given
  the sensitive nature of research data and the legal AI context this project
  is built to demonstrate.
- ChromaDB runs in-process, persists to a local directory, and requires zero
  infrastructure beyond a path in `.env`.
- A production deployment could migrate to Weaviate or Qdrant for more
  operational features without changing the retrieval logic.

**Honest trade-off:**

- ChromaDB is less feature-rich than Pinecone or Weaviate.
- No built-in monitoring, no multi-tenancy, and limited filtering compared to
  more mature vector stores.
- For the scale of Episteme, thousands of papers not millions, these
  limitations are not a problem.
- At production scale with millions of documents, migrating the vector store
  would be the right move.

---

## Ollama

**What it is:**

- Ollama is a tool for running large language models locally on your own hardware.
- It manages model downloads, quantization, and inference through a simple CLI
  and a local HTTP API at `localhost:11434`.
- Episteme uses it to run Llama 3 8B, which is Meta open-weight model.

**What problem it solves:**

- Every LLM call in Episteme, generating answers, extracting relationships,
  agent reasoning steps, needs a model to run against.
- The alternative is an external API like OpenAI or Anthropic, which costs
  money per token and sends data to external servers.

**The alternative:**

- OpenAI API (GPT-4o) or Anthropic API (Claude).
- Both produce higher quality outputs than a locally run 8B model and require
  no hardware considerations.
- Standard choice for production LLM applications.

**Why Ollama over OpenAI:**

- First, cost:
  - Every LLM call during development and testing is free.
  - A project making thousands of calls during development would accumulate
    real API costs otherwise.
- Second, data privacy:
  - Legal AI specifically requires that sensitive data does not leave the machine.
  - Running locally is not a nice-to-have in that context, it is a hard requirement.
- Third, open weights:
  - Llama 3 is a publicly released model.
  - Knowing how to work with open-weight models is a distinct and valuable
    skill compared to knowing how to call a closed API.
  - The system is designed so swapping Ollama for an OpenAI endpoint requires
    changing one config value, not rewriting the pipeline.

**Honest trade-off:**

- Llama 3 8B is meaningfully less capable than GPT-4o on complex reasoning tasks.
- Answer quality in the agent layer will be lower than it would be with a
  frontier model.
- For learning the full stack and demonstrating the architecture, this is an
  acceptable trade-off.

---

## LangGraph

**What it is:**

- LangGraph is a framework for building stateful, multi-step AI agents.
- Agent logic is modeled as a directed graph where nodes are processing steps
  and edges are conditional transitions between them.
- Part of the LangChain ecosystem and integrates with LangSmith for observability.

**What problem it solves:**

- A single LLM call cannot answer a complex research question like "what methods
  have been proposed for X, who pioneered them, and what datasets were used to
  evaluate them?"
- That requires planning, multiple retrieval steps, graph traversal, and synthesis.
- LangGraph provides the orchestration layer to manage that multi-step process
  with explicit state, conditional routing, and recoverable errors.

**The alternative:**

- A simple LangChain chain: a linear sequence of LLM calls.
- Or no framework at all, just Python functions calling each other.
- CrewAI is another agent framework that uses a role-based metaphor instead
  of a graph structure.

**Why LangGraph over a simple chain:**

- Linear chains cannot handle branching logic.
- If the first retrieval returns insufficient results, the agent needs to try
  a different query strategy. A chain cannot do that.
- LangGraph graph structure makes conditional routing explicit and inspectable.
- The state object means every step can see what previous steps found, which
  is essential for multi-hop research questions.
- The reasoning trace is fully visible, which is a requirement for the frontend
  and a genuine differentiator when explaining the system to an interviewer.

**Why LangGraph over CrewAI:**

- CrewAI role-based metaphor works well for multi-agent systems where different
  agents have distinct personas.
- Episteme has one agent with multiple tools, not multiple agents with roles.
  LangGraph lower-level graph control is a better fit for that architecture.
- LangGraph is the framework used in production by companies like Klarna,
  LinkedIn, and JPMorgan, making it the more professionally relevant choice
  to demonstrate.

**Honest trade-off:**

- LangGraph has a steeper learning curve than a simple chain or CrewAI.
- The graph, state, and node abstractions take time to internalize.
- CrewAI would have been faster to get a demo running.
- The investment in LangGraph pays off in control, observability, and
  professional relevance.