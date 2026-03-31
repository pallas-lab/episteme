# Notes

## Milestone 0

### I1

Why Poetry?

Poetry is the professional standard for Python projects because it does three things pip doesn't:

- Lockfile
  - `poetry.lock` records the exact version of every dependency and every sub-dependency. Anyone who clones the repo gets the identical environment vs with requirements.txt you often get "it works on my machine" problems.
- Dependency resolution
  - Poetry detects version conflicts before install anything. `pip` will happily install incompatible versions and let you discover the problem at runtime.
- Separation of dev and prod dependencies
  - Testing tools (like `pytest`, `jupyter`) don't go into production, and Poetry handles this cleanly.

### I2

- Mac issues with certificates, so we need to run the certificate installer that came with Python to fix it before installing Poetry. Or use `brew install poetry` to avoid this issue

```bash
open /Applications/Python\ 3.12/Install\ Certificates.command
```

- reads pyproject.toml, resolves all dependencies, creates the virtual environment, and generates `poetry.lock`

```bash
curl -sSL https://install.python-poetry.org | python3 -
poetry --version
poetry --install
```

- verify core import works

```bash
poetry run python -c "import fastapi, langchain, chromadb, neo4j, spacy; print('all good')"
```

- verify server starts

```bash
poetry run uvicorn backend.app.main:app --reload
```

### I3

Why Neo4j?

- Neo4j is a graph database so instead of storing data in tables with rows and columns like a traditional database, it stores nodes (entities) and edges (relationships between them).
  - For Episteme:
    - Scientific knowledge is inherently a graph: a paper uses a method, a method evaluates on a dataset, an author is affiliated with an institution.
    - Trying to represent that in a relational database means lots of painful JOIN queries. In Neo4j it's a natural traversal.

Why Docker for Neo4j?

- Neo4j is a Java application with its own server process. It's not a Python package you can just pip install.
  - Docker can run it as a contained service without installing Java or Neo4j globally on local machine.
  - When finished with the project, `docker-compose down` removes it cleanly, thus no system pollution.
- Verify & Start
  - http://localhost:7474/browser/

```bash
docker --version
docker compose up neo4j -d
docker compose logs neo4j
```

What is APOC?

- Awesome Procedures on Cypher (APOC) is Neo4j's standard plugin library
  - Adds hundreds of utility procedures for things like data import, graph algorithms, and text processing.

### I4

- Ollama is a tool that runs large language models entirely on local machine with no API calls, no internet required, no cost per token.
  - Every LLM call in Episteme (generating answers, extracting relationships, agent reasoning) goes through Ollama instead of OpenAI or Anthropic.
- Legal data is sensitive: client information, case strategy, privileged communications.
  - Running models locally means data never leaves the machine. No risk of leaks or breaches through third-party APIs.
- Why Llama 3?
  - It's Meta's open-weight model: free, no usage restrictions, strong performance on reasoning and instruction following. Open-weight indicates the model weights are publicly released so anyone can run them locally, which is different from GPT-4 or Claude which are closed and only accessible via API.
- Test Ollama
  - `http://localhost:11434/`
  - `ollama run llama3 "What is retrieval augmented generation? Answer in 2 sentences."`
    - Retrieval-Augmented Generation (RAG) is a type of language model that combines the strengths of both traditional retrieval-based and generative models by leveraging external knowledge retrieved from a database to augment its generated text. In RAG, the model first retrieves relevant information from the database and then uses this information to inform its generation process, leading to more accurate and informative text.

## Milestone 1

## Milestone 2

## Milestone 3

## Milestone 4

## Milestone 5

## Milestone 6

## Milestone 7

## Milestone 8

## Milestone 9

## Milestone 10
