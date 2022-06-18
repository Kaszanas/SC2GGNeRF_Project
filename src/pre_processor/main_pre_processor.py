import argparse
from pathlib import Path
from pre_processor import pre_process_videos


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="CLI for the pre processing of videos used for SC2GGNeRF."
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        help="Please provide a path to the directory that contains directories that hold the videos.",
        default="./rec",
    )
    parser.add_argument(
        "--input_ext",
        type=str,
        help="Please provide the extension that the input videos have.",
        default=".mkv",
    )

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    test = input_dir.resolve().as_posix()

    input_ext = args.input_ext

    pre_process_videos(input_dir=input_dir, input_extension=input_ext)
