from io import BytesIO
from pypdf import PdfReader
from .models import ParsedPage


def parse_pdf(pdf_bytes):
    reader = PdfReader(BytesIO(pdf_bytes))
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        pages.append(ParsedPage(page_number=page_number, text=text))
    return pages

    