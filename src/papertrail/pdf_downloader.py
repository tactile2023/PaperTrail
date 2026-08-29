import httpx


def download_pdf(pdf_url):
    response = httpx.get(
        pdf_url,
        timeout=30.0,
        follow_redirects=True

    )
    response.raise_for_status()

    if not response.content.startswith(b"%PDF-"):
        raise ValueError("Downloaded content is not a PDF")

    return response.content


