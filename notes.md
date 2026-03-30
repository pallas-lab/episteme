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
