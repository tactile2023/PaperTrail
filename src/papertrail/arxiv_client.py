import httpx

ARXIV_API_URL = "https://export.arxiv.org/api/query"

def fetch_arxiv_metadata_xml(arxiv_id):
    response = httpx.get(
        ARXIV_API_URL,
        params={"id_list": arxiv_id},
        timeout=30.0,
    )
    response.raise_for_status()

    return response.text