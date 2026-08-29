# PaperTrail
PaperTrail is an evidence-backed scientific paper integrity auditor for machine-learning papers on arXiv. 


## Motive
With there being a rise in papers submitted to academic journals, top conferences, and publishings on arXiv with AI slop, PaperTrail was inspired to help readers evaluate papers by identifying potential integrity and reproducibility issues to filter submitted "AI Slop."

## Planned Capabilities
- Retrieve and parse arXiv papers
- Extract paper metadata
- Verify Citations
- Audit reproducibility information
- Detect potential inconsistencies across paper results
- Generate evidence-backed reports
- Evaluate the system using a manually annotated benchmark


## Current Usage
PaperTrail can:

- Accept a modern or legacy arXiv identifier or URL
- Normalize `/abs/`, `/pdf/`, and `/html/` URLs
- Retrieve metadata from the arXiv API
- Extract the paper ID, title, summary, authors, dates, categories, and PDF URL
- Handle invalid identifiers, missing papers, missing PDF links, and network errors
- Run automated tests without depending on a live internet connection

## Installation
```bash
git clone git@github.com:tactile2023/PaperTrail.git
cd PaperTrail
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
