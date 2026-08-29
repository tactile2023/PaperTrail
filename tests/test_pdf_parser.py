from io import BytesIO
from pypdf import PdfWriter
from papertrail.pdf_parser import parse_pdf
import pytest
from pypdf.errors import PdfReadError


def create_test_pdf():
    pdf_stream = BytesIO()

    writer = PdfWriter()
    writer.add_blank_page(width=612, height=792)
    writer.add_blank_page(width=612, height=792)
    writer.write(pdf_stream)

    return pdf_stream.getvalue()


def test_parse_pdf_rejects_corrup_pdf():
    corrupt_pdf = b"%PDF-1.7 this is not a complete PDF"

    with pytest.raises(PdfReadError):
        parse_pdf(corrupt_pdf)


def test_parse_pdf_preserves_pages():
    pdf_bytes = create_test_pdf()

    pages = parse_pdf(pdf_bytes)

    assert len(pages) == 2
    assert pages[0].page_number == 1
    assert pages[1].page_number == 2
    assert pages[0].text == ""