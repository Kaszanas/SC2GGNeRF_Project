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
        # print("Rec_Func")

        # TODO: Improved camera control, now when zooming in on a unit it moves out of the camera area
        # TODO: get rid of: 1) health bar, 2) HUD

        # Wait for the user to confirm that the unit is selected:
        while True:
            if keyboard.is_pressed("h"):
                break

        # Center on the unit:
        pyautogui.keyDown("ctrl")
        pyautogui.press("f")
        pyautogui.keyUp("ctrl")

        # print(f"Unit on screen? = {self.unit_alive_center.is_on_screen}")

        # Rotate camera counterclockwise by 45 degrees:
        with pyautogui.hold(["insert", "ctrl", "f"]):
            await asyncio.sleep(2)
        # Wait for the camera to move to the right spot

        # Recording window starts here:
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
        # await hold_key(key="delete", hold_time=1)

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


# Notes:

# working 'title' must be in ""     -->     name = f'"{name}"'
# working desktop rec               -->     ffmpeg -f dshow -f gdigrab -video_size 1920x1080 -framerate 30 -i desktop -vcodec libx264 -preset ultrafast -qp 0 -pix_fmt yuv444p video.mkv
# overwrite output file if exists   -->     ffmpeg -y ...
# in case .mp4 broke                -->     ffmpeg -i foo.mp4.part -c copy -f mp4 foo.mp4
# in case .mkv -> .mp4              -->     ffmpeg -i inputVideoName.mkv -c:v copy -c:a copy outputVideoName.mp4
# video to frames                   -->     ffmpeg -i 0.mp4 %04dout.png
# kill ffmpeg process               -->     taskkill /im ffmpeg.exe /t /f
# force PathLib to create folder    -->     .mkdir(parents=True, exist_ok=True)

# can save 'subprocess.Popen' to variable       # but need to return object to kill outside function
# rec_out.stdin.write(bytes("q",'UTF-8'))       # pass 'q' for ffmpeg, sometimes cant kill process
