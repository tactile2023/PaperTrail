import re
from datetime import datetime, timezone


MODERN_ARXIV_ID_PATTERN = re.compile(
    r"(?:arxiv\s*:\s*|arxiv\.org/(?:abs|pdf)/)"
    r"(\d{4}\.\d{4,5}(?:v\d+)?)",
    re.IGNORECASE,
)

LEGACY_ARXIV_ID_PATTERN = re.compile(
    r"(?:arxiv\s*:\s*|arxiv\.org/(?:abs|pdf)/)"
    r"([a-z][a-z0-9.-]*/\d{7}(?:v\d+)?)",
    re.IGNORECASE,
)

YEAR_PATTERN = re.compile(r"(?<!\d)(\d{4})(?!\d)")
MIN_PUBLICATION_YEAR = 1800


def extract_arxiv_id(raw_text: str) -> str | None:
    for pattern in (MODERN_ARXIV_ID_PATTERN, LEGACY_ARXIV_ID_PATTERN):
        match = pattern.search(raw_text)
        if match: 
            return match.group(1)

    return None



def extract_year(raw_text: str) -> int | None:
    current_year = datetime.now(timezone.utc).year

    for match in YEAR_PATTERN.finditer(raw_text):
        year = int(match.group(1))

        if MIN_PUBLICATION_YEAR <= year <= current_year:
            return year
        
    return None