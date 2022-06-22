from pathlib import Path
from typing import List

import random
import json

# TODO: This is a duplicate function from colmap_runner.py.
# There should be a module containing such functions.
def save_commands_to_file(
    commands: List[str],
    output_file: Path = Path("nerf_commands.bat"),
):
    """
    Helper function that saves list of commands to a file.

    :param output_file: Specifies the path to the output file that will contain the commands, please note that the file will be overwriten after each execution.
    :type output_file: Path
    :param commands: Specifies the list of commands that will be saved to the file.
    :type commands: List[str]
    """

    with output_file.open(mode="w") as file:
        file.writelines(commands)


def prepare_nerf_commands(
    input_dir: Path,
    execution_dir: Path,
    testing: bool,
    n_steps: int = 1000,
) -> List[str]:
    """
    Helper that prepares the commands that can be used with instant-ngp 'run.py' script.
    This is required to streamline the training and testing for multiple recordings.

    Please be aware that this function is not universal at this moment.

    :param input_dir: Specifies the input directory that contains multiple datasets.
    :type input_dir: Path
    :param execution_dir: Specifies the directory where the execution of Python interpreter is supposed to take place.
    :type execution_dir: Path
    :param testing: Specifies the number of training steps that the NeRF will perform.
    :type testing: Path
    :param n_steps: Specifies the number of training steps that the NeRF will perform.
    :type n_steps: Path
    :return: Returns a list of strings representing commands that have to be run to train and test instant-ngp NeRF.
    :rtype: List[str]
    """

    all_commands = []

    for member in input_dir.iterdir():
        if member.is_dir():

            # Getting all of the paths constructed:
            path_to_cropped_dir = Path(input_dir, member.name, member.name + "_cropped")
            path_to_train_json = Path(path_to_cropped_dir, "train_transforms.json")
            path_to_test_json = Path(path_to_cropped_dir, "test_transforms.json")
            path_to_snapshot = Path(path_to_cropped_dir, f"train_test_{member.name}")
            nerf_runner_path = Path(
                execution_dir, "src", "instant-ngp", "scripts", "run.py"
            )

            # Standard command for training the model:
            command = f'python {nerf_runner_path.as_posix()} --scene {path_to_train_json.as_posix()} --n_steps {n_steps} --save_snapshot "{path_to_snapshot.as_posix()}"'

            # For testing the command looks differently:
            if testing:
                path_to_snapshot = Path(path_to_cropped_dir, f"train_{member.name}")
                command = f'python {nerf_runner_path.as_posix()} --scene {path_to_train_json.as_posix()} --test_transforms {path_to_test_json.as_posix()} --n_steps {n_steps} --save_snapshot "{path_to_snapshot.as_posix()}";'

            all_commands.append(command)

    return all_commands


def prepare_transforms(input_dir: Path):
    """
    Helper that splits a single transforms.json into separate train and test sets.

    :param input_dir: Specifies the input directory that contains multiple datasets within nested directories.
    :type input_dir: Path
    """

    # Go through all of the directories:
    for member in input_dir.iterdir():
        if member.is_dir():
            # Getting all of the paths constructed:
            path_to_cropped_dir = Path(input_dir, member.name, member.name + "_cropped")
            path_to_transforms = Path(path_to_cropped_dir, "transforms.json")
            path_to_train_json = Path(path_to_cropped_dir, "train_transforms.json")
            path_to_test_json = Path(path_to_cropped_dir, "test_transforms.json")

            # Open and parse transforms.json:
            with path_to_transforms.open("r") as transforms:
                loaded_data = json.load(transforms)

                list_of_frames = loaded_data["frames"]

                copy_data = {
                    "camera_angle_x": loaded_data["camera_angle_x"],
                    "camera_angle_y": loaded_data["camera_angle_y"],
                    "fl_x": loaded_data["fl_x"],
                    "fl_y": loaded_data["fl_y"],
                    "k1": loaded_data["k1"],
                    "k2": loaded_data["k2"],
                    "p1": loaded_data["p1"],
                    "p2": loaded_data["p2"],
                    "cx": loaded_data["cx"],
                    "cy": loaded_data["cy"],
                    "w": loaded_data["w"],
                    "h": loaded_data["h"],
                    "aabb_scale": loaded_data["aabb_scale"],
                }

                number_of_test_frames = len(list_of_frames) // 5
                test_frames = []
                for _ in range(number_of_test_frames):
                    random_test_frame = list_of_frames.pop(
                        random.randrange(len(list_of_frames))
                    )
                    test_frames.append(random_test_frame)

                # Creating and saving separate train and test files:
                with path_to_train_json.open("w") as train_file:
                    copy_data["frames"] = list_of_frames
                    json.dump(copy_data, train_file)
                with path_to_test_json.open("w") as test_file:
                    copy_data["frames"] = test_frames
                    json.dump(copy_data, test_file)
