import httpx
import pytest


from arxit.pdf_downloader import download_pdf

def test_download_pdf_returns_bytes(monkeypatch):
    expected_pdf = b"%PDF-1.7 fake PDF content"

    def fake_get(url, timeout, follow_redirects):
        assert url == "https://arxiv.org/pdf/1706.03762v7"
        assert timeout == 30.0
        assert follow_redirects is True

        request = httpx.Request("GET", url)
        return httpx.Response(
            200,
            content = expected_pdf,
            request = request,
        )

    monkeypatch.setattr(httpx, "get", fake_get)

    result = download_pdf(
        "https://arxiv.org/pdf/1706.03762v7"
    )

    assert result == expected_pdf
    assert isinstance(result, bytes)






def test_download_pdf_rejects_non_pdf_content(monkeypatch):
    def fake_get(url, timeout, follow_redirects):
        request = httpx.Request("GET", url)

        return httpx.Response(
            200,
            content=b"<html>Not a PDF</html>",
            request=request,
        )

    monkeypatch.setattr(httpx, "get", fake_get)

    with pytest.raises(
        ValueError,
        match="Downloaded content is not a PDF",
    ):
        download_pdf("https://example.com/not-a-paper")
