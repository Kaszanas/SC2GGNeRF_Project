import argparse


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
