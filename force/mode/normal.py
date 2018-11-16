# coding=utf-8

__all__ = ['MODE', 'press', 'release']

from . import general_lib
from . import numpad
from . import wuxia
from . import mouse

MODE = 'normal'


def press() -> dict:
        result = {
                "0002#['1']": general_lib.switch_mode(numpad),
                "0002#['Z']": general_lib.switch_mode(mouse),
                "0002#['X']": general_lib.switch_mode(wuxia),
                # "0002#['A']": general_lib.switch_mode(image.imageMapping),
        }
        return result


def release() -> dict:
        result = {}
        return result

# @staticmethod
# def _print_window_title(window_name: str):
#         """
#         打印激活窗口标题
#         """
#         print(window_name)
