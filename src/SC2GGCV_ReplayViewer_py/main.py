from turtle import position

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

class ObserverBot(ObserverAI):
    """
    A replay bot that can run replays.
    Check sc2/observer_ai.py for more available functions
    """

    watch_flag = 0

    async def on_start(self):
        print("Replay on_start() was called")

        for x in pyautogui.getAllWindows():  
            if str(x).find("StarCraft II") > 0:
                print(x)
                self.watch_flag = 1
    
    async def on_step(self, iteration: int):
        print(f"Replay iteration: {iteration}")
        

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
    # replay_path = "D:\\Projects\\SCI_EsportsComputerVision\\code\\dataset_generator\\src\\GGNeRF_DatasetGenerator_Rs\\target\\debug\\test_replay.SC2Replay"
    replay_path = "C:\\Users\\install\\Desktop\\GitHub\\SC2GGCV_DatasetGenerator\\src\\test_replay_spawner.SC2Replay"

    # client_bot = Client()
    # client_bot.obs_move_camera((76.0, 80.0))
    
    run_replay(ai=observer_bot, replay_path=replay_path)




### Notes:

# Center of the map = 76.0 & 80.0
# Client -> obs_move_camera(Point2(76.0, 80.0))