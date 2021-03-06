import asyncio
import time
from typing import Any, Tuple
import pyautogui


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
            print(window.title)
            return (True, window)

    return (False, None)


async def hold_key(key: str, hold_time: int) -> bool:
    """
    Helper holding a key for a set time.

    :param key: Specifies the key to be pressed.
    :type key: str
    :param hold_time: Specifies the hold time of a key.
    :type hold_time: int
    :return: Returns a boolean when the hold time is finished.
    :rtype: bool
    """

    with pyautogui.hold(key):
        await asyncio.sleep(hold_time)

    # start = time.time()
    # while time.time() - start < hold_time:
    #     pyautogui.keyDown(key)

    return True


def sync_hold_key(key: str, hold_time: int) -> bool:
    """
    Helper holding a key for a set time.

    :param key: Specifies the key to be pressed.
    :type key: str
    :param hold_time: Specifies the hold time of a key.
    :type hold_time: int
    :return: Returns a boolean when the hold time is finished.
    :rtype: bool
    """
    print(f"Starting to hold a key: {key}")

    with pyautogui.hold(key):
        pyautogui.sleep(hold_time)
    # start = time.time()
    # while time.time() - start < hold_time:
    #     pyautogui.keyDown(key)

    print(f"Key was held: {key}")

    return True


def get_unit_in_center():
    pass
