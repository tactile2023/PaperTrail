import subprocess
import sys
import papertrail.cli as cli
from papertrail.models import ArxivMetadata
import httpx
import pytest



def test_cli_handles_network_errors(monkeypatch, capsys):
    def fake_fetch(arxiv_id):
        raise httpx.ConnectError("Connection failed")

    monkeypatch.setattr(cli, "fetch_arxiv_metadata_xml", fake_fetch)
    monkeypatch.setattr(sys, "argv", ["papertrail", "1706.03762"])

    with pytest.raises(SystemExit) as error:
        cli.main()

    captured = capsys.readouterr()

    assert error.value.code ==2
    assert "Could not retrieve arXiv metadata" in captured.err

    

def test_cli_displays_metadata(monkeypatch, capsys):
    def fake_fetch(arxiv_id):
        assert arxiv_id == "2401.12345"
        return "<feed>fake XML</feed>"

    def fake_parse(xml_text):
        assert xml_text == "<feed>fake XML</feed>"

        return ArxivMetadata(
            arxiv_id="2401.12345v3",
            title="Example Paper",
            summary="Example summary",
            authors=["First Author", "Second Author"],
            published="2024-01-22T20:20:48Z",
            updated="2024-02-01T00:00:00Z",
            categories=["cs.LG"],
            pdf_url="https://arxiv.org/pdf/2401.12345v3",
        )

    monkeypatch.setattr(cli, "fetch_arxiv_metadata_xml", fake_fetch)
    monkeypatch.setattr(cli, "parse_arxiv_metadata", fake_parse)
    monkeypatch.setattr(
        sys,
        "argv",
        ["papertrail", "https://arxiv.org/abs/2401.12345"],
    )

    cli.main()

    output = capsys.readouterr().out

    assert "arXiv ID: 2401.12345v3" in output
    assert "Title: Example Paper" in output
    assert "Authors: First Author, Second Author" in output



def test_cli_rejects_invalid_input_without_traceback():
    result = subprocess.run(
        ["papertrail", "invalid_input"],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "Traceback" not in result.stderr
    assert "Invalid arXiv identifier" in result.stderr