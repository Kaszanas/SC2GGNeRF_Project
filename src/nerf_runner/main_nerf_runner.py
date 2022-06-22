import argparse
from pathlib import Path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="CLI for running COLMAP on pre-processed videos."
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Please provide a path to the directory that contains directories that hold the videos.",
        default="./rec",
    )

    args = parser.parse_args()

    # Getting the directory:
    input_dir = Path(args.input_dir)
    execution_dir = Path("./")
