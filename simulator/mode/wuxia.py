__all__ = ['wuxiaMapping']

import threading
import general
import simulator.core
import simulator.mouseInfo

from . import general_lib
from . import base
from . import normal


class _WuxiaMapping(base.BaseMapping):
        def __init__(self):
                super().__init__()
                self.MODE = 'wuxia'

                self.hwnd = None
                self.mouse_x, self.mouse_y = 0, 0
                self.rush_flags = False

        def press(self):
                result = {
                        "#['F2']": self.choose_hwnd(),
                        "#['F3']": self.cancel_hwnd(),
                        "#['F5']": self.clear_auction(1),
                        "#['F6']": self.rush_voyage(4),
                        "#['F7']": self.rush_voyage(5),
                        "#['F8']": self.rush_key(['W', 'G'], 1),
                        "#['F9']": self.rush_click(),
                        "#['F10']": self.rush_stop(),
                        "#['F11']": self.rush_key(['F']),
                }
                result.update({'*Escape': general_lib.switch_mode('normal', normal.normalMapping, self.rush_stop()[1])})
                result.update(super().press())
                return result

        def release(self):
                result = {}
                result.update(super().press())
                return result

        def choose_hwnd(self):
                def __choose_hwnd(hwnd):
                        self.hwnd = hwnd
                        self.mouse_x, self.mouse_y = simulator.mouseInfo.mouseInfo.mouse_position(hwnd)

                return '锁定激活窗口', __choose_hwnd

        def cancel_hwnd(self):
                def __cancel_hwnd(_):
                        self.hwnd = None

                return '取消窗口锁定', __cancel_hwnd

        def rush_stop(self):
                def __rush_stop(_):
                        self.rush_flags = False

                return '取消连续', __rush_stop

        def rush_voyage(self, hosi):
                def __rush_voyage_thread():
                        while self.rush_flags:
                                simulator.core.mouseBack.click('left', 820, 180, self.hwnd, wait=.2)
                                general.random_wait()
                                if hosi == 4:
                                        simulator.core.mouseBack.click('right', 662 - 1, 351 - 26, self.hwnd)
                                if hosi == 5:
                                        simulator.core.mouseBack.click('right', 471 - 1, 423 - 26, self.hwnd)
                                general.random_wait()
                                simulator.core.mouseBack.click('left', 971, 535, self.hwnd)
                                general.random_wait()

                def __rush_voyage(_):
                        if self.rush_flags or self.hwnd is None:
                                return
                        self.rush_flags = True
                        t = threading.Thread(target=__rush_voyage_thread, )
                        t.setDaemon(True)
                        t.start()

                comment = '抢 {0} 星流行'.format(hosi)
                return comment, __rush_voyage

        def rush_key(self, key_list, wait_time=0.05):
                def __rush_key_thread():
                        while self.rush_flags:
                                for x in key_list:
                                        general_lib.input_key(x, self.hwnd)
                                        general.random_wait(wait_time)

                def __rush_key(_):
                        if self.rush_flags:
                                return
                        self.rush_flags = True
                        t = threading.Thread(target=__rush_key_thread, )
                        t.setDaemon(True)
                        t.start()

                comment = '连续 {0}'.format(key_list)
                return comment, __rush_key

        def clear_auction(self, which=1):
                def __clear_auction_thread():
                        while self.rush_flags:
                                # 不计算边框坐标, (x-1, y-26)
                                simulator.core.mouseBack.click('left', 405, 197, self.hwnd, wait=.2)  # 搜索
                                general.random_wait()
                                simulator.core.mouseBack.click('left', 594, 260, self.hwnd, wait=.2)  # 第 which 个
                                general.random_wait()
                                simulator.core.mouseBack.click('left', 994, 642, self.hwnd, wait=.2)  # 购买
                                general.random_wait()
                                simulator.core.mouseBack.click('left', 662, 470, self.hwnd, wait=.2)  # 数量
                                general.random_wait()
                                simulator.core.mouseBack.click('left', 597, 419, self.hwnd, wait=.2)  # 确认
                                general.random_wait(.5)
                                simulator.core.mouseBack.click('left', 700, 418, self.hwnd, wait=.2)  # 二次确认
                                general.random_wait()

                def __clear_auction(_):
                        if self.rush_flags or self.hwnd is None:
                                return
                        self.rush_flags = True
                        t = threading.Thread(target=__clear_auction_thread, )
                        t.setDaemon(True)
                        t.start()

                return '扫拍卖', __clear_auction

        def rush_click(self):
                def __rush_click_thread():
                        if self.hwnd is None:
                                mouse_x, mouse_y = simulator.mouseInfo.mouseInfo.mouse_position()
                        else:
                                mouse_x, mouse_y = self.mouse_x, self.mouse_y
                        while self.rush_flags:
                                general_lib.click(mouse_x, mouse_y, 'left', self.hwnd, wait=.3)
                                general.random_wait()

                def __rush_click(_):
                        if self.rush_flags:
                                return
                        self.rush_flags = True
                        t = threading.Thread(target=__rush_click_thread, args=())
                        t.setDaemon(True)
                        t.start()

                return '连续左键', __rush_click


wuxiaMapping = _WuxiaMapping()
