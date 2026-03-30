<!-- PROJECT SUMMARY -->
<div align="center">
  <h1 align="center">Episteme</h1>

  <p align="center">
    A research intelligence system that builds a living knowledge graph from scientific literature — powered by GraphRAG, semantic search, fine-tuned NLP models, and agentic reasoning.
    <br>
    <a href="https://github.com/pallas-lab/episteme/issues">» submit a suggestion </a>
    ·
    <a href="https://github.com/pallas-lab/episteme/issues">» report a bug </a>
    ·
    <a href="https://github.com/pallas-lab/episteme">» contact </a>
  </p>

  <div align="center">

![GitHub forks](https://img.shields.io/github/forks/pallas-lab/episteme?style=social) ![GitHub stars](https://img.shields.io/github/stars/pallas-lab/episteme?style=social)

[![CI](https://github.com/pallas-lab/episteme/actions/workflows/push_on_main.yml/badge.svg)](https://github.com/pallas-lab/episteme/actions/workflows/push_on_main.yml)
![GitHub Pull Request (open)](https://img.shields.io/github/issues-pr/pallas-lab/episteme?color=blue) ![GitHub last commit](https://img.shields.io/github/last-commit/pallas-lab/episteme?color=pink) ![GitHub License](https://img.shields.io/github/license/pallas-lab/episteme?color=green) ![contributions welcome](https://img.shields.io/badge/contributions-welcome-purple.svg?style=flat)

  </div>
</div>

<!-- TABLE OF CONTENT -->
<details open="open">
  <summary><h2 style="display: inline-block">🕹 Table of Content</h2></summary>
  <ol>
    <li>
      <a href="#-about">About</a>
      <ul>
        <li><a href="#-tech-stack">Tech Stack</a></li>
        <li><a href="#-features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#-documentation">Documentation</a>
      <ul>
        <li><a href="#-setup">Setup</a></li>
        <li><a href="#-development">Development</a></li>
      </ul>
    </li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-license">License</a></li>
  </ol>
</details>

<!-- ABOUT -->
## :sunflower: About

Episteme is a research intelligence system built over scientific literature. It ingests papers from arXiv and Semantic Scholar, extracts scientific entities and relationships using fine-tuned NLP models, and constructs a knowledge graph that connects concepts, methods, authors, datasets, and citations across papers. On top of that graph, it layers hybrid semantic search and a LangGraph-powered agent capable of answering multi-step research questions with citations and reasoning traces.

The project implements full ML engineering stack for NLP systems including data ingestion pipelines, information extraction, retrieval-augmented generation, knowledge graph construction, LLM fine-tuning, agent orchestration, evaluation, and a fullstack interface. 

### :hammer_and_wrench: Tech Stack

#### :heavy_plus_sign: Development Tools

- [x] Python 3.11+
- [x] Poetry (dependency management)
- [x] Jupyter Notebooks (experimentation)
- [x] VSCode

#### :heavy_plus_sign: Data & NLP

- [x] arXiv API (paper ingestion)
- [x] Semantic Scholar API (metadata + citations)
- [x] PyMuPDF (PDF parsing)
- [x] spaCy (NLP baseline)
- [x] HuggingFace Transformers (fine-tuning + NER)
- [x] SciSpaCy (scientific NLP models)
- [x] sentence-transformers (embeddings)

#### :heavy_plus_sign: Storage & Retrieval

- [x] ChromaDB (vector store)
- [x] Neo4j Community Edition (knowledge graph)
- [x] SQLite (metadata store)

#### :heavy_plus_sign: ML & Agents

- [x] Ollama + Llama 3 (local LLM inference)
- [x] LangChain + LangGraph (agent orchestration)
- [x] QLoRA via HuggingFace PEFT (fine-tuning)
- [x] RAGAS (RAG evaluation framework)

#### :heavy_plus_sign: Backend

- [x] FastAPI
- [x] Pydantic

#### :heavy_plus_sign: Frontend

- [x] React
- [x] D3.js / Cytoscape.js (graph visualization)

#### :heavy_plus_sign: DevOps

- [x] GitHub Actions (CI)
- [x] Docker (containerization)

### :mushroom: Features

#### :heavy_plus_sign: Paper Ingestion Pipeline

- [x] Fetch papers by keyword, topic, or author from arXiv and Semantic Scholar
- [x] Parse PDFs into structured sections (abstract, introduction, methods, results)
- [x] Chunk and preprocess text for downstream NLP

#### :heavy_plus_sign: Scientific Entity & Relationship Extraction

- [x] Fine-tuned NER model for scientific entities (methods, datasets, concepts, metrics)
- [x] Relationship extraction between entities across sentences and papers
- [x] Structured output pipeline feeding directly into the knowledge graph

#### :heavy_plus_sign: Knowledge Graph Construction

- [x] Neo4j graph of papers, authors, concepts, methods, datasets, institutions, and citations
- [x] Graph traversal queries for concept lineage, author networks, and method evolution
- [x] Visual graph explorer in the frontend

#### :heavy_plus_sign: Hybrid Semantic Search

- [x] Dense retrieval via fine-tuned domain embeddings model
- [x] Sparse retrieval via BM25
- [x] Reranking layer for result quality
- [x] Search over full papers, sections, or entities independently

#### :heavy_plus_sign: GraphRAG Query Layer

- [x] Combines vector retrieval with graph traversal for context-aware answers
- [x] Citations and source attribution on every generated response
- [x] Explainable retrieval — shows which nodes and edges informed the answer

#### :heavy_plus_sign: LangGraph Research Agent

- [x] Multi-step agent that plans, searches, traverses the graph, and synthesizes answers
- [x] Handles compound research questions ("what methods address X, and who pioneered them?")
- [x] Reasoning trace visible in the frontend

#### :heavy_plus_sign: Fine-Tuned Models

- [x] Domain-adapted sentence-transformer for scientific embeddings
- [x] Fine-tuned NER model on SciERC dataset for scientific entity recognition
- [x] Benchmark comparison between base and fine-tuned models

#### :heavy_plus_sign: Evaluation Harness

- [x] RAGAS metrics (faithfulness, answer relevancy, context recall, context precision)
- [x] NER model benchmarks (precision, recall, F1 per entity type)
- [x] Retrieval quality metrics (MRR, NDCG)

<!-- CONTENT -->
## :cactus: Documentation

### :honey_pot: Setup

```bash
# clone the repo
git clone https://github.com/pallas-lab/episteme.git
cd episteme

# install python dependencies
poetry install

# copy environment variables
cp .env.example .env

# start Neo4j (via Docker)
docker-compose up neo4j -d

# start Ollama and pull the model
ollama pull llama3

# start the backend
poetry run uvicorn backend.app.main:app --reload

# install frontend dependencies and start
cd frontend
npm install
npm run dev
```

### :apple: Development

* [Milestone 0 — Project Scaffold](https://github.com/pallas-lab/episteme/milestone/1)
* [Milestone 1 — Data Ingestion Pipeline](https://github.com/pallas-lab/episteme/milestone/2)
* [Milestone 2 — NLP Extraction + Knowledge Graph](https://github.com/pallas-lab/episteme/milestone/3)
* [Milestone 3 — Embeddings + Vector Store](https://github.com/pallas-lab/episteme/milestone/4)
* [Milestone 4 — Hybrid Semantic Search](https://github.com/pallas-lab/episteme/milestone/5)
* [Milestone 5 — GraphRAG Query Layer](https://github.com/pallas-lab/episteme/milestone/6)
* [Milestone 6 — LangGraph Research Agent](https://github.com/pallas-lab/episteme/milestone/7)
* [Milestone 7 — Fine-Tuning (Embeddings + NER)](https://github.com/pallas-lab/episteme/milestone/8)
* [Milestone 8 — FastAPI Backend](https://github.com/pallas-lab/episteme/milestone/9)
* [Milestone 9 — React Frontend](https://github.com/pallas-lab/episteme/milestone/10)
* [Milestone 10 — Evaluation Harness](https://github.com/pallas-lab/episteme/milestone/11)

<!-- CONTRIBUTING -->
## :ear_of_rice: Contributing

> 1. Fork the Project
> 2. Create your Branch (`git checkout -b my-branch`)
> 3. Commit your Changes (`git commit -m 'add my contribution'`)
> 4. Push to the Branch (`git push --set-upstream origin my-branch`)
> 5. Open a Pull Request

<!-- LICENSE -->
## :pencil: License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).