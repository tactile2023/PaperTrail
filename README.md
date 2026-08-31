# arXit
arXit is an evidence-backed scientific paper integrity auditor for machine-learning papers on arXiv. 


## Motive
With there being a rise in papers submitted to academic journals, top conferences, and publishings on arXiv with AI slop, arXit was inspired to help readers evaluate papers by identifying potential integrity and reproducibility issues to filter submitted "AI Slop."

## Planned Capabilities
- Retrieve and parse arXiv papers
- Extract paper metadata
- Verify Citations
- Audit reproducibility information
- Detect potential inconsistencies across paper results
- Generate evidence-backed reports
- Evaluate the system using a manually annotated benchmark


## Current Usage
arXit can:

- Normalize a modern or legacy arXiv identifier or URL
- Retrieve metadata from the arXiv API
- Extract the paper ID, title, summary, authors, dates, categories, and PDF URL
- Extract and detect numbered sections and subsectoins
- Extract numbered/unnumbered references
- Report network, metadata, download, and PDF parsing errors

Academic PDF formatting varies, so unusual layouts may require additional rules. 


## Installation
```bash
git clone git@github.com:tactile2023/arXit.git
cd arXit
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
