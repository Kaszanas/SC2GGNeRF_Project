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

    subprocess.Popen(
        f"""ffmpeg -y -f dshow -f gdigrab {video_size} -framerate {frame_rate} -i title={name} -vcodec libx264 -preset ultrafast -qp 0 -pix_fmt yuv444p {final_path}"""
    )

    async def rec_func():

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
        record_window(
            name="StarCraft II",
            output_path="".join(["./rec/", self.unit_alive_center.name, "/"]),
            filename="".join([self.unit_alive_center.name, "_video", ".mkv"]),
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
        subprocess.run(f"""taskkill /im ffmpeg.exe /t /f""")
