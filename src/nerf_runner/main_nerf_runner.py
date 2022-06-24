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
    parser.add_argument(
        "--testing",
        type=bool,
        help="Please provide information if the NeRF will also test against some transforms.json.",
        default=True,
    )
    parser.add_argument(
        "--n_steps",
        type=int,
        help="Please provide number of training steps.",
        default=400,
    )

    args = parser.parse_args()

    testing_bool = args.testing
    n_steps = args.n_steps

    # Getting the directory:
    input_dir = Path(args.input_dir)
    execution_dir = Path("./")

    resolved_input = input_dir.resolve()

    prepare_transforms(input_dir=resolved_input)
    nerf_commands = prepare_nerf_commands(
        input_dir=input_dir,
        execution_dir=execution_dir,
        testing=testing_bool,
        n_steps=n_steps,
    )
    save_commands_to_file(commands=nerf_commands)
