import argparse
import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.utils import sync_hold_key


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Tool used for processing StarCraft 2 (SC2) datasets. with https://github.com/Kaszanas/SC2InfoExtractorGo"
    )
    parser.add_argument(
        "--key",
        type=str,
        help="Provide key to be held.",
    )
    parser.add_argument(
        "--hold_time",
        type=int,
        help="Provide time for the key to be held for.",
    )
    args = parser.parse_args()

    sync_hold_key(key=args.key, hold_time=args.hold_time)
