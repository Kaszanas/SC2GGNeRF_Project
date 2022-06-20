from pathlib import Path


from sc2.main import run_replay
from sc2.observer_ai import ObserverAI


class ObserverBot(ObserverAI):
    """
    A replay bot that can run replays.
    Check sc2/observer_ai.py for more available functions
    """

    async def on_start(self):
        print("Replay on_start() was called")

    async def on_step(self, iteration: int):
        print(f"Replay iteration: {iteration}")

    async def on_enemy_unit_entered_vision(self, unit):
        print("enemy unit spotted")

    async def on_enemy_unit_left_vision(self, unit):
        print("unit_left_vision")

    async def on_unit_took_damage(self, unit, damage):
        print("unit took damage")


if __name__ == "__main__":
    my_observer_ai = ObserverBot()
    replay_path = (
        Path("./src/replays/test_replay_spawner.SC2Replay").resolve().as_posix()
    )

    run_replay(my_observer_ai, replay_path=replay_path, observed_id=0)
