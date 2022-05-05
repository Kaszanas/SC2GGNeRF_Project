from sc2.observer_ai import ObserverAI
from sc2.main import run_replay
# from sc2 import maps
# from sc2.player import Bot
# from sc2.main import run_game
# from sc2.data import Race
# from sc2.bot_ai import BotAI


# TODO: Sprawdzic czy jednostka jest "zywa" -> wlaczenie nagrywania
# TODO: Kamera -> rotowanie i przyblizanie

class ObserverBot(ObserverAI):
    """
    A replay bot that can run replays.
    Check sc2/observer_ai.py for more available functions
    """
    async def on_start(self):
        print("Replay on_start() was called")

    async def on_step(self, iteration: int):
        print(f"Replay iteration: {iteration}")

if __name__ == "__main__":

    observer_bot = ObserverBot()
    replay_path = "D:\\Projects\\SCI_EsportsComputerVision\\code\\dataset_generator\\src\\GGNeRF_DatasetGenerator_Rs\\target\\debug\\test_replay.SC2Replay"

    run_replay(ai=observer_bot, replay_path=replay_path)