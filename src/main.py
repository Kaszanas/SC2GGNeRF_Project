from gettext import find
from turtle import position
from typing import Any, Tuple

# import sc2

from sc2.observer_ai import ObserverAI
from sc2.main import run_replay, _play_replay
from sc2.client import Client
from sc2.position import Point2
from sc2.unit import Unit

# from sc2 import maps
# from sc2.player import Bot
# from sc2.main import run_game
# from sc2.data import Race
# from sc2.bot_ai import BotAI
import pyautogui


# TODO: Sprawdzic czy jednostka jest "zywa" -> wlaczenie nagrywania
# TODO: Kamera -> rotowanie i przyblizanie


def find_window(title: str) -> Tuple[bool, None | Any]:
    """
    Helper that looks for a window that contains a title substring in the list of processes and returns a boolean and the window handle.

    :param title: Title substring that will be searched.
    :type title: str
    :return: Returns True and window handle if the window was found, otherwise returns False, and None.
    :rtype: Tuple[bool, None | Any]
    """
    for window in pyautogui.getAllWindows():
        if title in window.title:
            print(window)
            return (True, window)

    return (False, None)


def get_unit_in_center():
    pass


class ObserverBot(ObserverAI):
    """
    A replay bot that can run replays.
    Check sc2/observer_ai.py for more available functions
    """

    async def on_start(self):
        print("Replay on_start() was called")
        # Initializing window as not found, no window handle exists:
        self.found_window = False
        self.recording_started = False

        # Get map center coordinates used to find units:
        self.center_x = self.game_info.map_center.x
        self.center_y = self.game_info.map_center.y

        # Attempting to find a window that contains a specific substring:
        self.found_window, self.window = find_window(title="StarCraft II")

    async def on_step(self, iteration: int):
        # If StarCrarft II window was still not found - look for it!
        if not self.found_window:
            self.found_window, self.window = find_window(title="StarCraft II")
        else:
            # Otherwise check if unit is in the center and if the recording was started
            units = self.game_data.units
            for unit_id, unit_type_data in units.items():
                unit_position = unit_type_data.position

            print("Window not found")

    async def on_unit_created(self, unit):
        print(f"Unit created: {unit}")
        print(f"Unit position: {unit.position}")
        print("*** START RECORDING ***")
        self.client.obs_move_camera(unit.position)

    async def on_unit_destroyed(self, unit_tag: int):
        print(f"Unit destroyed: {unit_tag}")
        print("*** END RECORDING ***")


if __name__ == "__main__":

    observer_bot = ObserverBot()
    replay_path = "./replays/test_replay_spawner.SC2Replay"

    run_replay(ai=observer_bot, replay_path=replay_path)


# client_bot = Client()
# client_bot.obs_move_camera((76.0, 80.0))

### Notes:

# Center of the map = 76.0 & 80.0
# Client -> obs_move_camera(Point2(76.0, 80.0))
