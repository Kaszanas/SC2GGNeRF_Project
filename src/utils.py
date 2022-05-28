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
            print(window)
            return (True, window)

    return (False, None)


def get_unit_in_center():
    pass
