import pytest

from arxit.arxiv_parser import parse_arxiv_metadata

SAMPLE_XML = """
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <title>Attention Is 
    All You Need
    </title>

    <summary>
        We introduce the Transformer, an architecture based solely on attention mechanisms.
    </summary>

    <author>
        <name>Monkey See</name>
    </author>

    <author>
        <name>Monkey Do</name>
    </author>

    <published> 2017-06-12T17:57:34Z </published>
    <updated>2023-08-02T00:41:18Z</updated>

    <category term="cs.CL" />
    <category term="cs.LG" />

    <id>http://arxiv.org/abs/1706.03762v7</id>

    <link
        href="https://arxiv.org/abs/1706.03762v7"
        rel="alternate"
        type="text/html"
    />
    <link
        title="pdf"
        href="https://arxiv.org/pdf/1706.03762v7"
        rel="related"
        type="application/pdf"
    />



</entry>
</feed>
"""

xml_without_pdf = SAMPLE_XML.replace("""<link
        title="pdf"
        href="https://arxiv.org/pdf/1706.03762v7"
        rel="related"
        type="application/pdf"
    />""","")



def test_parser_extracts_id():
    metadata = parse_arxiv_metadata(SAMPLE_XML)
    assert metadata.arxiv_id == "1706.03762v7"

def test_parser_raises_for_missing_pdf():
    with pytest.raises(ValueError, match="arXiv entry is missing a PDF URL"):
        parse_arxiv_metadata(xml_without_pdf)

def test_parser_extracts_dates():
    metadata = parse_arxiv_metadata(SAMPLE_XML)

    assert metadata.published == "2017-06-12T17:57:34Z"
    assert metadata.updated == "2023-08-02T00:41:18Z"


def test_parser_extracts_authors():
    metadata = parse_arxiv_metadata(SAMPLE_XML)

    assert metadata.authors == [
    "Monkey See",
    "Monkey Do",
    ]

def test_parser_extracts_pdf_url():
    metadata = parse_arxiv_metadata(SAMPLE_XML)
    assert metadata.pdf_url == "https://arxiv.org/pdf/1706.03762v7"


def test_parser_extracts_summary():
    metadata = parse_arxiv_metadata(SAMPLE_XML)

    assert metadata.summary == (

        "We introduce the Transformer, an architecture based solely on attention mechanisms."
    )


def test_parser_extracts_categories():
    metadata = parse_arxiv_metadata(SAMPLE_XML)

    assert metadata.categories == [
        "cs.CL",
        "cs.LG"
    ]


def test_parser_rejects_feed_without_entry():
    emptyfeed = """
    <feed xmlns="http://www.w3.org/2005/Atom">
    </feed>
"""
    with pytest.raises(ValueError):
        parse_arxiv_metadata(emptyfeed)


        
def test_parser_extracts_title():
    metadata = parse_arxiv_metadata(SAMPLE_XML)
    
    assert metadata.title == "Attention Is All You Need"
