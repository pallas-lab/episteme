from backend.app.pipelines.arxiv_client import fetch_papers

papers = fetch_papers(
    query="retrieval augmented generation",
    max_results=5,
    categories=["cs.AI", "cs.CL"],
)

for p in papers:
    print(f"\nTitle: {p.title}")
    print(f"Authors: {', '.join(p.authors[:3])}")
    print(f"Published: {p.published}")
    print(f"arXiv ID: {p.arxiv_id}")
    print(f"Categories: {p.categories}")
    print(f"Abstract preview: {p.abstract[:150]}...")