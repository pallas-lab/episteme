# Notes

## M1

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
