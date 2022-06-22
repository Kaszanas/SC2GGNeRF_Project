import argparse
from pathlib import Path

from colmap_runner import prepare_colmap_commands, save_commands_to_file


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
    parser.add_argument(
        "--aabb_scale",
        type=int,
        help="Please provide aabb_scale.",
        default=8,
    )

    args = parser.parse_args()

    aabb_scale = args.aabb_scale

    # Getting the directory:
    input_dir = Path(args.input_dir)
    execution_dir = Path("./")

    colmap_commands = prepare_colmap_commands(
        input_dir=input_dir, execution_dir=execution_dir, aabb_scale=aabb_scale
    )
    save_commands_to_file(commands=colmap_commands)
