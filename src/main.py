from sc2.main import run_replay

from src.bot import ObserverBot

if __name__ == "__main__":

    observer_bot = ObserverBot()
    replay_path = "./replays/test_replay_spawner.SC2Replay"

    run_replay(ai=observer_bot, replay_path=replay_path)


# client_bot = Client()
# client_bot.obs_move_camera((76.0, 80.0))

### Notes:

# Center of the map = 76.0 & 80.0
# Client -> obs_move_camera(Point2(76.0, 80.0))
