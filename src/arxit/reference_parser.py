import re
from datetime import datetime, timezone

YEAR_PATTERN = re.compile(r"(?<!\d)(\d{4})(?!\d)")
MIN_PUBLICATION_YEAR = 1800


def extract_year(raw_text: str) -> int | None:
    current_year = datetime.now(timezone.utc).year

    for match in YEAR_PATTERN.finditer(raw_text):
        year = int(match.group(1))

        if MIN_PUBLICATION_YEAR <= year <= current_year:
            return year
        
    return None