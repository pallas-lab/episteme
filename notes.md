# Notes

## Why Poetry?

Poetry is the professional standard for Python projects because it does three things pip doesn't:

- Lockfile
  - `poetry.lock` records the exact version of every dependency and every sub-dependency. Anyone who clones the repo gets the identical environment vs with requirements.txt you often get "it works on my machine" problems.
- Dependency resolution
  - Poetry detects version conflicts before install anything. `pip` will happily install incompatible versions and let you discover the problem at runtime.
- Separation of dev and prod dependencies
  - Testing tools (like `pytest`, `jupyter`) don't go into production, and Poetry handles this cleanly.
