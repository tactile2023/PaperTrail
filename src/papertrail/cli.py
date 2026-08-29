import argparse
import httpx
from .arxiv_client import fetch_arxiv_metadata_xml
from .arxiv_parser import parse_arxiv_metadata
from .arxiv_id import normalize_arxiv_id
from pypdf.errors import PdfReadError

from .models import ParsedPaper
from .pdf_downloader import download_pdf
from .pdf_parser import parse_pdf







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

        pdf_bytes = download_pdf(metadata.pdf_url)
        pages = parse_pdf(pdf_bytes)

        paper = ParsedPaper(metadata=metadata, pages=pages)

    except ValueError as e:
        parser.error(str(e))

    except httpx.HTTPStatusError as e:
        if e.response.status_code ==429:
            parser.error(
                "arXiv rate limit reached. "
                "Wait before trying again."
            )
        parser.error(f"Coult not retrieve arXiv metadata: {e}")

    except httpx.HTTPError as e:
        parser.error(f"Could not retrieve arXiv metadata: {e}")

    except PdfReadError as e:
        parser.error(f"Could not parse PDF: {e}")


    character_count = sum(len(page.text) for page in paper.pages)

        
    print(f"arXiv ID: {metadata.arxiv_id}")
    print(f"Title: {metadata.title}")
    print(f"Authors: {', '.join(metadata.authors)}")
    print(f"Published: {metadata.published}")
    print(f"PDF: {metadata.pdf_url}")
    print(f"Pages parsed: {len(paper.pages)}")
    print(f"Characters extracted: {character_count}")
