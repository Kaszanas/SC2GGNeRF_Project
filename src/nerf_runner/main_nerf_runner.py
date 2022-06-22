import argparse
from pathlib import Path

from nerf_runner import prepare_nerf_commands, prepare_transforms, save_commands_to_file

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

    resolved_input = input_dir.resolve()

    prepare_transforms(input_dir=resolved_input)
    nerf_commands = prepare_nerf_commands(
        input_dir=input_dir,
        execution_dir=execution_dir,
        testing=True,
    )
    save_commands_to_file(commands=nerf_commands)
