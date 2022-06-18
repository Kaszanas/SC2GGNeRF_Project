import asyncio

from pathlib import Path
import subprocess

import pyautogui
import keyboard


def record_window(
    name: str,
    output_path: Path,
    filename: Path,
    video_prefix: str = "",
    video_suffix: str = "",
    resolution: str = "",
):
    """
    Exposes the logic for recording a selected window by the window name.
    TODO: This function is not written in a production grade manner. This requires a rewrite.
    Killing an FFMPEG task is

    :param name: Specifies the name of the window that is going to be recorded.
    :type name: str
    :param output_path: Specifies the output path where the final recording will be saved.
    :type output_path: Path
    :param filename: Specifies the filename which will be used for the final recording.
    :type filename: Path
    :param video_prefix: Specifies a possible video prefix for the recording, defaults to ""
    :type video_prefix: str, optional
    :param video_suffix: Specifies a possible video suffix for the recording, defaults to ""
    :type video_suffix: str, optional
    :param resolution: Specifies the resolution that the video will take, defaults to ""
    :type resolution: str, optional
    """

    frame_rate = 30
    video_size = ""
    name = f'"{name}"'

    if resolution:
        print(f"*Rec resolution = {resolution}*")
        video_size = " ".join(["-video_size", resolution])
    else:
        print(f"*Get window resolution*")
        video_size = ""

    # Create folder for specific recordings
    Path(output_path).mkdir(parents=True, exist_ok=True)

    final_path = (
        Path(output_path, video_prefix, filename, video_suffix).resolve().as_posix()
    )

    return subprocess.Popen(
        f"""ffmpeg -y -f dshow -f gdigrab {video_size} -framerate {frame_rate} -i title={name} -vcodec libx264 -preset ultrafast -qp 0 -pix_fmt yuv444p {final_path}"""
    )


async def rec_func(unit_name: str):
    """
    Automates camera movements within StarCraft II
    (because libraries that implement StarCraft II protocol don't support that out of the bos)

    # TODO:
    This function kills an FFMPEG task after the recording is supposed to finish.
    This is in no way production grade code, and leads to corrupted files

    :param unit_name: Specifies the unit name that is going to be recorded.
    :type unit_name: str
    """

    # TODO: Improve camera control, now when zooming in on a unit it moves out of the camera area
    # TODO: get rid of: 1) health bar, 2) HUD

    # Wait for the user to confirm that the unit is selected:
    while True:
        if keyboard.is_pressed("h"):
            break

    # Center on the unit:
    pyautogui.keyDown("ctrl")
    pyautogui.press("f")
    pyautogui.keyUp("ctrl")

    # Rotate camera counterclockwise by 45 degrees:
    with pyautogui.hold(["insert", "ctrl", "f"]):
        # Wait for the camera to move to the right spot
        await asyncio.sleep(2)

    # Start recording the window:
    recording_process = record_window(
        name="StarCraft II",
        output_path="".join(["./rec/", unit_name, "/"]),
        filename="".join([unit_name, "_video", ".mkv"]),
        video_suffix="",
        video_prefix="",
        resolution="",
    )

    # Rotate camera clockwise by 90 degrees:
    with pyautogui.hold(["delete", "ctrl", "f"]):
        await asyncio.sleep(1)

    # Zoom to get another angle on unit
    with pyautogui.hold(["insert", "ctrl", "f"]):
        pyautogui.press("end")
        await asyncio.sleep(1)

    # Rotate camera counterclockwise by 90 degrees:
    with pyautogui.hold(["delete", "ctrl", "f"]):
        await asyncio.sleep(1)

    pyautogui.press("end")
    await asyncio.sleep(2)

    # Kill FFMPEG process --> recordings in 'rec\{unit.name}' folder (.mkv)
    print("Rec_OFF")
    recording_process.terminate()
    # subprocess.run(f"""taskkill /im ffmpeg.exe /t /f""")
