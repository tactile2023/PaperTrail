from dataclasses import dataclass

@dataclass
class ArxivMetadata:
    title: str
    summary: str
    authors: list[str]
    published: str
    updated: str
    categories: list[str]
    arxiv_id: str
    pdf_url: str



@dataclass
class ParsedPage:
    page_number: int
    text: str

@dataclass
class ParsedPaper:
    metadata: ArxivMetadata
    pages: list[ParsedPage]