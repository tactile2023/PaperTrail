import argparse

from .arxiv_id import normalize_arxiv_id

def build_parser():
    parser = argparse.ArgumentParser(
        prog="papertrail",
        description="Audit machine-learning papers on arXiv.",
    )

    parser.add_argument("paper", help="An arXiv URL or identifier.",)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:    
        arxiv_id = normalize_arxiv_id(args.paper)
    except ValueError as e:
        parser.error(str(e))

        
    print(f"Paper requested: {arxiv_id}")
