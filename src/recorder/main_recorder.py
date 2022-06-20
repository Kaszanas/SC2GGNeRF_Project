from pathlib import Path

# Third party:
from sc2.main import run_replay

# Own Imports:
from bot import ObserverBot

if __name__ == "__main__":

    observer_bot = ObserverBot()
    replay_path = (
        Path("./src/recorder/replays/test_replay_spawner.SC2Replay")
        .resolve()
        .as_posix()
    )

    run_replay(ai=observer_bot, replay_path=replay_path, realtime=True, observed_id=1)
