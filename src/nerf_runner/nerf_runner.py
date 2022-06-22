from pathlib import Path
from typing import List


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

    # TODO: Go through all of the directories

    # Open and parse transforms.json

    # Create two separate files train_transforms.json and test_transforms.json

    pass
