from arxit.citation_verifier import (
    collect_unique_arxiv_ids,
)
from arxit.models import Reference, ArxivMetadata
import arxit.citation_verifier as verifier


from arxit.citation_verifier import (collect_unique_arxiv_ids, fetch_reference_metadata, verify_arxiv_references, match_reference_metadata)


def test_verify_arxiv_references(
    monkeypatch,
):
    reference = Reference(
        label="1",
        raw_text="Attention paper.",
        arxiv_id="1706.03762",
    )

    metadata = ArxivMetadata(
        title="Attention Is All You Need",
        summary="A Transformer architecture.",
        authors=["Ashish Vaswani"],
        published="2017-06-12T17:57:34Z",
        updated="2023-08-02T00:41:18Z",
        categories=["cs.CL"],
        arxiv_id="1706.03762v7",
        pdf_url="https://arxiv.org/pdf/1706.03762v7",
    )

    monkeypatch.setattr(
        verifier,
        "fetch_reference_metadata",
        lambda references: [metadata],
    )

    results = verify_arxiv_references(
        [reference]
    )

    assert len(results) == 1
    assert results[0].reference == reference
    assert results[0].metadata == metadata


def test_match_reference_metadata():
    resolved_reference = Reference(
        label="1",
        raw_text="Attention paper.",
        arxiv_id="1706.03762",
    )
    missing_reference = Reference(
        label="2",
        raw_text="Unknown paper.",
        arxiv_id="9999.99999",
    )

    metadata = ArxivMetadata(
        title="Attention Is All You Need",
        summary="A Transformer architecture.",
        authors=["Ashish Vaswani"],
        published="2017-06-12T17:57:34Z",
        updated="2023-08-02T00:41:18Z",
        categories=["cs.CL"],
        arxiv_id="1706.03762v7",
        pdf_url="https://arxiv.org/pdf/1706.03762v7",
    )

    results = match_reference_metadata(
        [resolved_reference, missing_reference],
        [metadata],
    )

    assert len(results) == 2

    assert results[0].reference == resolved_reference
    assert results[0].metadata == metadata

    assert results[1].reference == missing_reference
    assert results[1].metadata is None




def test_fetch_reference_metadata_uses_one_batch(monkeypatch):
    references = [
        Reference(
            label="1",
            raw_text="First paper.",
            arxiv_id="1302.4389",
        ),
        Reference(
            label="2",
            raw_text="Repeated paper.",
            arxiv_id="1302.4389",
        ),
        Reference(
            label="3",
            raw_text="Another paper.",
            arxiv_id="1706.03762",
        ),
    ]

    expected_metadata = ["first metadata", "second metadata"]

    def fake_fetch(arxiv_ids):
        assert arxiv_ids == [
            "1302.4389",
            "1706.03762",
        ]
        return "<feed>batch response</feed>"

    def fake_parse(xml_text):
        assert xml_text == "<feed>batch response</feed>"
        return expected_metadata

    monkeypatch.setattr(
        verifier,
        "fetch_arxiv_metadata_batch_xml",
        fake_fetch,
    )
    monkeypatch.setattr(
        verifier,
        "parse_arxiv_metadata_batch",
        fake_parse,
    )

    result = fetch_reference_metadata(references)

    assert result == expected_metadata


def test_fetch_reference_metadata_skips_empty_batch(
    monkeypatch,
):
    references = [
        Reference(
            label="1",
            raw_text="No arXiv identifier.",
        )
    ]

    def fail_if_called(arxiv_ids):
        raise AssertionError(
            "The arXiv API should not be called"
        )

    monkeypatch.setattr(
        verifier,
        "fetch_arxiv_metadata_batch_xml",
        fail_if_called,
    )

    assert fetch_reference_metadata(references) == []





def test_collect_unique_arxiv_ids():
    references = [
        Reference(
            label="1",
            raw_text="First paper. arXiv:1302.4389.",
            arxiv_id="1302.4389",
        ),
        Reference(
            label="2",
            raw_text="A reference without an arXiv ID.",
        ),
        Reference(
            label="3",
            raw_text="Repeated paper. arXiv:1302.4389.",
            arxiv_id="1302.4389",
        ),
        Reference(
            label="4",
            raw_text="Another paper. arXiv:1706.03762.",
            arxiv_id="1706.03762",
        ),
    ]

    assert collect_unique_arxiv_ids(references) == [
        "1302.4389",
        "1706.03762",
    ]


def test_collect_unique_arxiv_ids_returns_empty_list():
    references = [
        Reference(
            label="1",
            raw_text="A reference without an arXiv ID.",
        )
    ]

    assert collect_unique_arxiv_ids(references) == []