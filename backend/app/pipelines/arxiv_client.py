import json
import logging
from pathlib import Path
from dataclasses import dataclass, field

import arxiv

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create data directory if it doesn't exist
DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Define a dataclass for papers
@dataclass
class Paper:
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    categories: list[str]
    published: str
    pdf_url: str
    source: str = "arxiv"

# Fetch papers from arXiv based on a query and optional category filters
def fetch_papers(
    query: str,
    max_results: int = 10,
    categories: list[str] = None,
) -> list[Paper]:
    """
    Fetch papers from arXiv by keyword query and optional category filter.
    Results are cached locally to data/raw/ to avoid re-fetching.
    """
    cache_key = query.replace(" ", "_").lower()
    cache_path = DATA_DIR / f"{cache_key}.json"

    if cache_path.exists():
        logger.info(f"Loading cached results for: {query}")
        with open(cache_path) as f:
            raw = json.load(f)
        return [Paper(**p) for p in raw]

    logger.info(f"Fetching papers from arXiv for: {query}")

    search_query = query
    if categories:
        category_filter = " OR ".join(f"cat:{c}" for c in categories)
        search_query = f"({query}) AND ({category_filter})"

    search = arxiv.Search(
        query=search_query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance,
    )

    client = arxiv.Client()
    papers = []

    for result in client.results(search):
        paper = Paper(
            arxiv_id=result.entry_id.split("/")[-1],
            title=result.title,
            authors=[str(a) for a in result.authors],
            abstract=result.summary,
            categories=result.categories,
            published=str(result.published.date()),
            pdf_url=result.pdf_url,
        )
        papers.append(paper)
        logger.info(f"Fetched: {paper.title[:60]}...")

    with open(cache_path, "w") as f:
        json.dump([p.__dict__ for p in papers], f, indent=2)

    logger.info(f"Saved {len(papers)} papers to {cache_path}")
    return papers