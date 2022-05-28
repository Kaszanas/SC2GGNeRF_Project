from sc2.observer_ai import ObserverAI
from sc2.client import Client
from sc2.position import Point2
from sc2.unit import Unit

from src.utils import find_window


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

        self.center_precision = 5

        # Center camera:
        self.client.obs_move_camera(self.game_info.map_center)

        # Attempting to find a window that contains a specific substring:
        self.found_window, self.window = find_window(title="StarCraft II")

    async def on_step(self, iteration: int):
        # If StarCrarft II window was still not found - look for it!
        if not self.found_window:
            self.found_window, self.window = find_window(title="StarCraft II")
        else:
            print("Window found")

            # Otherwise check if unit is in the center and if the recording was started
            units = self.game_data.units
            center_unit_id = None
            for unit_id, unit_type_data in units.items():
                unit_position = unit_type_data.position
                # Checking if the unit is roughly in the center:
                if (
                    unit_position.x >= self.center_x - self.center_precision
                    or unit_position.x <= self.center_x + self.center_precision
                ) and (
                    unit_position.y >= self.center_y - self.center_precision
                    or unit_position.y <= +self.center_precision
                ):
                    center_unit_id = unit_id

            # Center camera on the unit:
            self.client.obs_move_camera(units[center_unit_id].position)
            print("Centered camera")

            # Start recording:
            print("Started Recording")

    async def on_unit_created(self, unit):
        print(f"Unit created: {unit}")
        print(f"Unit position: {unit.position}")
        print("*** START RECORDING ***")
        self.client.obs_move_camera(unit.position)

    async def on_unit_destroyed(self, unit_tag: int):
        print(f"Unit destroyed: {unit_tag}")
        print("*** END RECORDING ***")
