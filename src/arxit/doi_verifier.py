from .crossref_client import (fetch_crossref_metadata)

from .models import (DoiCitationResult, Reference, Finding)

def collect_unique_dois(references: list[Reference]) -> list[str]:
    unique_dois = []
    seen_dois = set()

    for reference in references: 
        doi = reference.doi

        if (doi is not None and doi not in seen_dois):
            unique_dois.append(doi)
            seen_dois.add(doi)

    return unique_dois


def verify_doi_references(references: list[Reference]) -> list[DoiCitationResult]:
    unique_dois = collect_unique_dois(references)

    metadata_by_doi = {
        doi: fetch_crossref_metadata(doi)
        for doi in unique_dois
    }

    return [
        DoiCitationResult(
            reference=reference,
            metadata=metadata_by_doi[
                reference.doi
            ],
        )
        for reference in references
        if reference.doi is not None
    ]



def find_unresolved_doi_citations(results: list[DoiCitationResult]) -> list[Finding]:
    findings = []

    for result in results:
        if result.metadata is None:
            doi = result.reference.doi

            findings.append(
                Finding(
                    finding_type=("unresolved_doi_citation"), 
                    message=(f"DOI {doi} could not be resolved."), 
                    reference = result.reference))

    return findings