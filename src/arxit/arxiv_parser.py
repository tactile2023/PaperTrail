import xml.etree.ElementTree as ET
from .arxiv_id import normalize_arxiv_id
from .models import ArxivMetadata


ATOM_NAMESPACE = {
    "atom": "http://www.w3.org/2005/Atom"
}

def parse_arxiv_metadata(xml_text):
    root = ET.fromstring(xml_text)
    entry = root.find("atom:entry", ATOM_NAMESPACE)

    

    if entry is None:
        raise ValueError("No arXiv paper found")

    link_elements = entry.findall("atom:link", namespaces=ATOM_NAMESPACE)
    pdf_url = None

    for l in link_elements:
        if l.get("title") == "pdf":
            pdf_url = l.get("href")
            break

    if pdf_url is None:
        raise ValueError("arXiv entry is missing a PDF URL")
    


    entry_id = entry.findtext("atom:id", namespaces=ATOM_NAMESPACE)
    arxiv_id = normalize_arxiv_id(entry_id)

    published = entry.findtext("atom:published", namespaces=ATOM_NAMESPACE)
    published = " ".join(published.split()) # Normalize whitespace

    updated = entry.findtext("atom:updated", namespaces=ATOM_NAMESPACE)
    updated = " ".join(updated.split()) # Normalize whitespace

    category_elements = entry.findall("atom:category", namespaces=ATOM_NAMESPACE)
    categories = []

    for category in category_elements:
        term = category.get("term")
        categories.append(term)



    author_elements = entry.findall("atom:author", namespaces=ATOM_NAMESPACE)
    authors = []

    for element in author_elements:
        name = element.findtext(
            "atom:name", namespaces=ATOM_NAMESPACE
        )
        authors.append(name)
        
        
        
    title = entry.findtext("atom:title", namespaces=ATOM_NAMESPACE)
    title = " ".join(title.split())  # Normalize whitespace

    summary = entry.findtext("atom:summary", namespaces=ATOM_NAMESPACE)
    summary = " ".join(summary.split())  # Normalize whitespace

    return ArxivMetadata(
        title=title,
        summary=summary,
        authors=authors,
        published=published,
        updated=updated,
        categories=categories,
        arxiv_id=arxiv_id,
        pdf_url=pdf_url
    )