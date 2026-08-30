import pytest
from arxit.arxiv_id import normalize_arxiv_id


def test_http_abs_url_is_normalized():
    result = normalize_arxiv_id("http://arxiv.org/abs/1706.03762v7")
    assert result == "1706.03762v7"

def test_http_pdf_url_is_normalized():
    result = normalize_arxiv_id("http://arxiv.org/pdf/1706.03762v7.pdf")
    assert result == "1706.03762v7"

def test_http_html_url_is_normalized():
    result = normalize_arxiv_id("http://arxiv.org/html/1706.03762v7")
    assert result == "1706.03762v7"

def test_whitespace_input_is_rejected():
    with pytest.raises(ValueError):
        normalize_arxiv_id("    ")

def test_invalid_input_is_rejected():
    with pytest.raises(ValueError):
        normalize_arxiv_id("invalid_input")


def test_plain_modern_id_is_unchanged():
    result = normalize_arxiv_id("2401.12345")
    assert result == "2401.12345"

def test_abs_url_is_normalized():
    result = normalize_arxiv_id("https://arxiv.org/abs/2401.12345")
    assert result == "2401.12345"

def test_pdf_url_is_normalized():
    result = normalize_arxiv_id("https://arxiv.org/pdf/2401.12345.pdf")
    assert result == "2401.12345"

def test_pdf_url_without_pdf_extension_is_normalized():
    result = normalize_arxiv_id("https://arxiv.org/pdf/2401.12345")
    assert result == "2401.12345"

def test_abs_url_with_version_is_normalized():
    result = normalize_arxiv_id("https://arxiv.org/abs/2307.15043v1")
    assert result == "2307.15043v1"

def test_plain_modern_id_with_version_is_unchanged():
    result = normalize_arxiv_id("2307.15043v1")
    assert result == "2307.15043v1"

def test_pdf_url_with_version_is_normalized():
    result = normalize_arxiv_id("https://arxiv.org/pdf/2307.15043v1.pdf")
    assert result == "2307.15043v1"

def test_html_url_is_normalized():
    result = normalize_arxiv_id("https://arxiv.org/html/2401.12345v1")
    assert result == "2401.12345v1"

def test_abs_archive_url_is_normalized():
    result = normalize_arxiv_id("https://arxiv.org/abs/hep-th/9901001v2")
    assert result == "hep-th/9901001v2"

def test_plain_archive_id_is_unchanged():
    result = normalize_arxiv_id("hep-th/9901001v2")
    assert result == "hep-th/9901001v2"

def test_whitespace_is_normalized():
    result = normalize_arxiv_id(" https://arxiv.org/abs/2401.12345v1 ")
    assert result == "2401.12345v1"
