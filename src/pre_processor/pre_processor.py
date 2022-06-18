from pathlib import Path
import subprocess
from typing import Tuple


def crop_video(
    video_filepath: Path,
    output_dir: Path,
    output_extension: str = ".mkv",
) -> Tuple[bool, Path]:
    """
    Helper method that crops a single video with some settings using FFMPEG

    :param video_filepath: Specifies a path pointing to the video file that is going to be cropped.
    :type video_filepath: Path
    :param output_dir: Specifies a path that will be used as output directory for the cropped video.
    :type output_dir: Path
    :return: Returns a path to the cropped video.
    :rtype: Path
    """

    # ffmpeg -i .\BroodLord_video.mkv -vf "crop=1050:800:out_w/2-186:0" BroodLord_video_cropped.mkv

    output_filepath = Path(
        output_dir, video_filepath.name, "_cropped", output_extension
    )

    commands = [
        "ffmpeg",
        "-i",
        video_filepath.resolve().as_posix(),
        "-vf",
        '"crop=1050:800:out_w/2-186:0"',
        output_filepath.resolve().as_posix(),
    ]

    # TODO: Need better error handling here!
    if subprocess.run(commands).returncode == 0:
        print(f"Successfully cropped {video_filepath.name}")
    else:
        print(f"Failed to crop {video_filepath.name}")
        return False, Path("")

    return True, output_filepath


def export_frames() -> Path:
    pass


# TODO: This function could be more universal with cropping parameters:
def pre_process_videos(input_dir: Path, input_extension: str = ".mkv"):
    """
    Helper function that pre processes the videos with hardcoded settings

    :param input_dir: Specifies the input path which is a directory containing directories that hold the recordings.
    :type input_dir: Path
    :param input_extension: Specifies the extension that will be used to search for the video that is going to be processed with the cropping, defaults to ".mkv"
    :type input_extension: str, optional
    """

    # Iterate over all of the members of the input directory:
    for member in input_dir.iterdir():
        # Detect if the member is a directory itself:
        if member.is_dir():
            # Name of the member should correspond to the
            # name of the video that is going to be processed:
            video_file = Path(member, member.name, input_extension)
            output_dir = Path(member, member.name, "_cropped")

            # Cropping the video:
            ok_crop, crop_output = crop_video(
                video_filepath=video_file,
                output_dir=output_dir,
                output_extension=input_extension,
            )

            # Cannot export frames if the video was not cropped:
            if ok_crop:
                export_frames()