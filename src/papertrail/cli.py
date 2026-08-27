import argparse


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

    print(f"Paper requested: {args.paper}")
