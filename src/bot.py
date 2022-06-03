import asyncio
from sc2.observer_ai import ObserverAI

from utils import find_window

import pyautogui
import pywinauto
import win32gui, win32con


class ObserverBot(ObserverAI):
    """
    A replay bot that can run replays.
    Check sc2/observer_ai.py for more available functions
    """

    units_recorded = []

    async def rec_func(self):
        print("Rec_Func")

        # TODO: Focus on SC2 window

        input("Is the unit selected?")

        await asyncio.sleep(1)

        #if not self.window.isActive:
            # hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(self.window._hWnd, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(self.window._hWnd)

        # TODO: Hold hotkey Ctrl + F or find toggle for centering on unit:
        
        print(f"Unit on screen? = {self.unit_alive_center.is_on_screen}")

        await asyncio.sleep(2)

        pyautogui.keyDown("ctrl")
        pyautogui.press("f")
        pyautogui.keyUp("ctrl")

        print(f"Unit on screen? = {self.unit_alive_center.is_on_screen}")

        await asyncio.sleep(2)

        # TODO: Hold insert before starting recording to rotate camera:

        # TODO: Start rec

        # TODO: keyUp("HOLD")

        # TODO: Hold Del button to rotate camera:

        # TODO: press END / zoom
        # TODO: 

        print("Rec_OFF")

    async def on_start(self):
        print("Replay on_start() was called")
        # Initializing window as not found, no window handle exists:
        self.found_window = False
        self.recording_started = False
        self.unit_alive_center = False

        # Get map center coordinates used to find units:
        self.distance_from_center = 10
        self.center_map = self.game_info.map_center

        # Center camera:
        # self.client.obs_move_camera(self.game_info.map_center)

        # Attempting to find a window that contains a specific substring:
        self.found_window, self.window = find_window(title="StarCraft II")
        print(f"Window SC2 found? = {self.found_window}")

    async def on_step(self, iteration: int):
        # print(iteration)

        # If StarCrarft II window was still not found - look for it!
        if not self.found_window:
            self.found_window, self.window = find_window(title="StarCraft II")
        else:
            # Center camera:
            self.client.obs_move_camera(self.game_info.map_center)

            # Find Units close to center
            units_close_to_center = self.all_units.closer_than(
                self.distance_from_center, self.center_map
            )
            # print(units_close_to_center)

            # Start recording -> Check if unit close to center exists and was not recorded
            if (
                units_close_to_center.exists
                and not self.recording_started
                and units_close_to_center not in self.units_recorded
            ):
                print("Unit created close to center...")
                # print(units_close_to_center)
                self.unit_alive_center = units_close_to_center[0]
                print(self.unit_alive_center)
                print(self.unit_alive_center.position)

                # TODO: SELECT UNIT -> Rec_Func -> FOCUS WINDOW -> ROTATE CAMERA WITH REC -> STOP REC -> NEXT UNIT

                # TODO: Select Unit:

                self.all_own_units.select(self.all_own_units)

                # Check if UNIT is on screen
                # print(self.unit_alive_center.is_on_screen)

                # os.run("python helper_rotate.py")
                self.recording_started = True
                print("*** START RECORDING ***")

                await self.rec_func()

                # TODO: Hold insert before starting recording to rotate camera:

                # self.client.move_camera_spatial(self.unit_alive_center.position)
                # Add unit to list of recorded units and start recording
                self.units_recorded.append(units_close_to_center)
                # TODO: Press Del button to rotate camera:

            # Stop recording -> No units close to center
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

    # NOT WORKING #
    # async def on_unit_created(self, unit):
    #     print(f"Unit created: {unit}")
    #     print(f"Unit position: {unit.position}")
    #     print("*** START RECORDING ***")

    # Bugs - sometimes did not detect destroyed units
    # async def on_unit_destroyed(self, unit_tag: int):
    #     print(f"Unit destroyed: {unit_tag}")
    #     if(self.recording_started == True and self.unit_alive_center.tag == unit_tag):
    #         print("*** END RECORDING ***")
    #         self.recording_started = False
    #         #print(f"\nList with recorded Units: {len(self.units_recorded)}")
    #         #print(self.units_recorded)
