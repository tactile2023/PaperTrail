import argparse
import httpx
from .arxiv_client import fetch_arxiv_metadata_xml
from .arxiv_parser import parse_arxiv_metadata
from .arxiv_id import normalize_arxiv_id

def build_parser():
    parser = argparse.ArgumentParser(
        prog="papertrail",
        description="Audit machine-learning papers on arXiv.",
    )

    parser.add_argument("paper", help="An arXiv URL or identifier.",)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:    
        arxiv_id = normalize_arxiv_id(args.paper)
        xml_text = fetch_arxiv_metadata_xml(arxiv_id)
        metadata = parse_arxiv_metadata(xml_text)

    except ValueError as e:
        parser.error(str(e))

    except httpx.HTTPError as e:
        parser.error(f"Could not retrieve arXiv metadata: {e}")

        
    print(f"arXiv ID: {metadata.arxiv_id}")
    print(f"Title: {metadata.title}")
    print(f"Authors: {', '.join(metadata.authors)}")
    print(f"Published: {metadata.published}")
    print(f"PDF: {metadata.pdf_url}")
