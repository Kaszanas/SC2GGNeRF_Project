from pathlib import Path
import subprocess
from typing import Tuple


def crop_video(
    video_filepath: Path,
    output_dir: Path,
    output_extension: str = ".mkv",
) -> Tuple[bool, Path]:
    """
    Helper that crops a single video with some settings using FFMPEG

    :param video_filepath: Specifies a path pointing to the video file that is going to be cropped.
    :type video_filepath: Path
    :param output_dir: Specifies a path that will be used as output directory for the cropped video.
    :type output_dir: Path
    :return: Returns a path to the cropped video.
    :rtype: Path
    """

    output_filepath = Path(
        video_filepath.parent,
        output_dir,
        video_filepath.stem + "_cropped" + output_extension,
    )

    commands = [
        "ffmpeg",
        "-i",
        video_filepath.as_posix(),
        "-vf",
        "crop=1050:800:out_w/2-186:0",
        "-y",
        output_filepath.resolve().as_posix(),
    ]

    # Checking if the ffmpeg successfully performed the cropping:
    if subprocess.run(commands).returncode == 0:
        print(f"Successfully cropped: {video_filepath.name}")
    else:
        print(f"Failed to crop {video_filepath.name}")
        return False, Path("")

    return True, output_filepath


def export_frames(
    input_video: Path,
    output_dir: Path,
    extension: str = ".jpg",
) -> Tuple[bool, Path]:
    """
    Helper that export frames from some input video to the specified output directory.

    :param input_video: Specifies the path to the input video that will be used in the export process.
    :type input_video: Path
    :param output_dir: Specifies the output directory where the exported frames will be placed.
    :type output_dir: Path
    :param output_dir: Specifies the output extension.
    :type output_dir: Path
    :return: Returns a path to the output directory
    :rtype: Path
    """

    output_file_path = Path(output_dir, input_video.stem + "%03d" + ".png")

    commands = [
        "ffmpeg",
        "-i",
        input_video.resolve().as_posix(),
        output_file_path.resolve().as_posix(),
    ]

    # Checking if the ffmpeg successfully performed the cropping:
    if subprocess.run(commands).returncode == 0:
        print(f"Successfully exported frames of: {input_video.name}")
    else:
        print(f"Failed to crop {input_video.name}")
        return False, Path("")

    return True, output_dir


# TODO: This function could be more universal with cropping parameters:
def pre_process_videos(
    input_dir: Path,
    bool_export_frames: bool,
    bool_crop: bool = True,
    input_extension: str = ".mkv",
):
    """
    Helper function that pre processes the videos with hardcoded settings

    :param input_dir: Specifies the input path which is a directory containing directories that hold the recordings.
    :type input_dir: Path
    :param bool_crop: Specifies if cropping should be performed.
    :type bool_crop: bool
    :param bool_export_frames: Specifies if exporting frames should be performed.
    :type bool_export_frames: Path
    :param input_extension: Specifies the extension that will be used to search for the video that is going to be processed with the cropping, defaults to ".mkv"
    :type input_extension: str, optional
    """

    # Iterate over all of the members of the input directory:
    for member in input_dir.iterdir():
        # Detect if the member is a directory itself:
        if member.is_dir():
            # Name of the member should correspond to the
            # name of the video that is going to be processed:
            video_file = Path(
                input_dir,
                member.name,
                member.name + "_video" + input_extension,
            ).resolve()
            crop_output_dir = Path(
                input_dir,
                member.name,
                member.name + "_cropped",
            ).resolve()

            # Creating path if it does not exists:
            crop_output_dir.mkdir(parents=False, exist_ok=True)
            # if not crop_output_dir.exists():
            #     os.mkdir(crop_output_dir.resolve().as_posix())

            # Cropping the video:
            if bool_crop:
                ok_crop, crop_output = crop_video(
                    video_filepath=video_file,
                    output_dir=crop_output_dir,
                    output_extension=input_extension,
                )

    for member in input_dir.iterdir():
        if member.is_dir():
            for nested1_member in member.iterdir():
                if nested1_member.is_dir():
                    # Cannot export frames if the video was not cropped:
                    if bool_export_frames:

                        crop_output_dir = Path(
                            input_dir,
                            member.name,
                            member.name + "_cropped",
                        ).resolve()

                        export_frames_output_dir = Path(
                            crop_output_dir, member.name + "_frames"
                        )
                        # Creating path if it does not exists:
                        export_frames_output_dir.mkdir(parents=False, exist_ok=True)

                        crop_output = Path(
                            crop_output_dir,
                            member.name + "_video_cropped" + input_extension,
                        )

                        export_frames(
                            input_video=crop_output,
                            output_dir=export_frames_output_dir,
                        )
