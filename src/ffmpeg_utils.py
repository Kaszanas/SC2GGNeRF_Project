import os
import glob
from pathlib import Path


def record_window(
    name: str,
    output_path: Path,
    filename: Path,
    video_prefix: str = "",
    video_suffix: str = "",
):

    video_size = "1366x768"

    final_path = (
        Path(output_path, video_prefix, filename, video_suffix).resolve().as_posix()
    )

    os.system(
        f"""ffmpeg -rtbufsize 1500M -f dshow -f gdigrab -framerate 30 -draw_mouse 1 -i title={name} -pix_fmt yuv420p -profile:v baseline -y {final_path}"""
    )


# record_vid("Steam")


# Dzialajaca linijka FFMPEG
# ffmpeg -rtbufsize 1500M -f dshow -f gdigrab -framerate 30 -draw_mouse 1 -i title=Steam -pix_fmt yuv420p -profile:v baseline -y Huangbaohua.mp4
# Video do Klatek -> ffmpeg -i 0.mp4 %04dout.png
