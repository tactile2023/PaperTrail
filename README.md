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
PaperTrail accepts an arXiv identifier through its CLI interface:
`papertrail 2401.12345`

Example output:

`Paper requested: 2401:12345`

PaperTrail does NOT retrieve or audit the paper yet.

## Dev Setup
Create and activate a Python 3.12 environment:
```
python3.12 -m venv .venv
source .venv/bin/activate
```
Install PaperTrail and its dev dependencies:

`python -m pip install --editable ".[dev]"`

Run the tests:

`pytest`