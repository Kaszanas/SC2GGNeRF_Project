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
    parser.add_argument(
        "--bool_crop",
        type=bool,
        help="Please provide if video cropping should be performed.",
        default=True,
    )
    parser.add_argument(
        "--bool_export_frames",
        type=bool,
        help="Please provide if exporting frames from the video should be performed.",
        default=True,
    )

    args = parser.parse_args()

    bool_crop = args.bool_crop
    bool_export_frames = args.bool_export_frames

    # Getting the directory:
    input_dir = Path(args.input_dir)
    test = input_dir.resolve().as_posix()

    input_ext = args.input_ext

    pre_process_videos(
        input_dir=input_dir,
        bool_crop=bool_crop,
        bool_export_frames=bool_export_frames,
        input_extension=input_ext,
    )
