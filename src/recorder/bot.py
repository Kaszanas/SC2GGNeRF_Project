import os
import sys
from sc2.observer_ai import ObserverAI

from src.recorder.utils import find_window

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.recorder.ffmpeg_utils import rec_func


class ObserverBot(ObserverAI):
    """
    A replay bot that can run replays.
    Check sc2/observer_ai.py for more available functions
    """

    async def on_start(self):
        print("Replay on_start() was called")

        self.units_recorded = []

        # Initializing window as not found, no window handle exists:
        self.found_window = False
        self.recording_started = False
        self.unit_alive_center = False

        # Get map center coordinates used to find units:
        self.distance_from_center = 10
        self.center_map = self.game_info.map_center

        # TODO: API needs fixing - Center camera --> not working:
        # self.client.obs_move_camera(self.game_info.map_center)

        # Attempting to find a window that contains a specific substring:
        self.found_window, self.window = find_window(title="StarCraft II")
        print(f"Window SC2 found? = {self.found_window}")

    async def on_step(self, iteration: int):

        # If StarCrarft II window was still not found - look for it!
        if not self.found_window:
            self.found_window, self.window = find_window(title="StarCraft II")
        else:
            # Center camera:
            self.client.obs_move_camera(self.game_info.map_center)

            # Find Units close to center:
            units_close_to_center = self.all_units.closer_than(
                self.distance_from_center, self.center_map
            )

            # Start recording -> Check if unit close to center exists and was not recorded:
            if (
                units_close_to_center.exists
                and not self.recording_started
                and units_close_to_center not in self.units_recorded
                and iteration % 22 == 0
            ):
                print("Unit created close to center...")
                self.unit_alive_center = units_close_to_center[0]
                print(self.unit_alive_center)
                print(self.unit_alive_center.position)

                self.recording_started = True
                print("*** START RECORDING ***")
                await rec_func(unit_name=self.unit_alive_center.name)

                # Add unit to list of recorded units and start recording:
                self.units_recorded.append(units_close_to_center)

            # Stop recording -> No units close to center:
            if self.recording_started and units_close_to_center.empty:
                print("*** END RECORDING ***")
                self.recording_started = False
                print(f"\nList with recorded Units: {len(self.units_recorded)} \n")
                # print(self.units_recorded)

    async def on_enemy_unit_entered_vision(self, unit):
        # print("enemy unit spotted")
        pass

    async def on_enemy_unit_left_vision(self, unit):
        # print("unit_left_vision")
        pass

    async def on_unit_took_damage(self, unit, damage):
        # print("unit took damage")
        pass
