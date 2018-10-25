__all__ = ['wuxiaMapping']

import threading
from .. import core
from .. import mouseListen

from . import general_lib
from . import base


class _WuxiaMapping(base.BaseMapping):
        def __init__(self):
                super().__init__()
                self.MODE = 'wuxia'

                self.hwnd = None
                self.mouse_x, self.mouse_y = 0, 0
                self.rush_flags = False

        def press(self):
                return dict({
                        "#['F2']": self.choose_hwnd,
                        "#['F3']": self.cancel_hwnd,
                        "#['F5']": self.clear_auction,
                        "#['F6']": self.rush_hosi_4,
                        "#['F7']": self.rush_hosi_5,
                        "#['F8']": self.rush_w_g,
                        "#['F9']": self.rush_click,
                        "#['F10']": self.rush_stop,
                        "#['F11']": self.rush_f,
                        '*Escape': general_lib.switch_normal,
                }, **super().press())

        def release(self):
                return dict({}, **super().release())

        def choose_hwnd(self, hwnd):
                """
                锁定激活窗口
                """
                self.hwnd = hwnd
                self.mouse_x, self.mouse_y = mouseListen.mouseListen.mouse_position(hwnd)
                return

        def cancel_hwnd(self, _):
                """
                取消窗口锁定
                """
                self.hwnd = None

        def rush_stop(self, _):
                """
                取消连续
                """
                self.rush_flags = False

        def clear_auction(self, _):
                """
                扫拍卖
                """
                if self.rush_flags or self.hwnd is None:
                        return
                self.rush_flags = True
                t = threading.Thread(target=self._clear_auction, args=(1,))
                t.setDaemon(True)
                t.start()

        def _clear_auction(self, which=1):
                while self.rush_flags:
                        core.mouseHwnd.click('left', 406 - 1, 223 - 26, self.hwnd, wait=.2)
                        # 不计算边框坐标
                        core.wait.random_wait()
                        core.mouseHwnd.click('left', 595 - 1, 286 - 26, self.hwnd, wait=.2)
                        core.wait.random_wait()
                        core.mouseHwnd.click('left', 995 - 1, 668 - 26, self.hwnd, wait=.2)
                        core.wait.random_wait()
                        core.mouseHwnd.click('left', 663 - 1, 496 - 26, self.hwnd, wait=.2)
                        core.wait.random_wait()
                        core.mouseHwnd.click('left', 598 - 1, 445 - 26, self.hwnd, wait=.2)
                        core.wait.random_wait(.5)
                        core.mouseHwnd.click('left', 701 - 1, 444 - 26, self.hwnd, wait=.2)
                        core.wait.random_wait()

        def rush_hosi_4(self, _):
                """
                抢四星流行
                """
                if self.rush_flags or self.hwnd is None:
                        return
                self.rush_flags = True
                t = threading.Thread(target=self._rush_liuxing, args=(4,))
                t.setDaemon(True)
                t.start()

        def rush_hosi_5(self, _):
                """
                抢五星流行
                """
                if self.rush_flags or self.hwnd is None:
                        return
                self.rush_flags = True
                t = threading.Thread(target=self._rush_liuxing, args=(5,))
                t.setDaemon(True)
                t.start()

        def _rush_liuxing(self, hosi=5):
                while self.rush_flags:
                        core.mouseHwnd.click('left', 821 - 1, 206 - 26, self.hwnd, wait=.2)
                        core.wait.random_wait()
                        if hosi == 4:
                                core.mouseHwnd.click('right', 662 - 1, 351 - 26, self.hwnd)
                        if hosi == 5:
                                core.mouseHwnd.click('right', 471 - 1, 423 - 26, self.hwnd)
                        core.wait.random_wait()
                        core.mouseHwnd.click('left', 972 - 1, 561 - 26, self.hwnd)
                        core.wait.random_wait()

        def rush_f(self, _):
                """
                连续 f
                """
                if self.rush_flags:
                    return
                self.rush_flags = True
                t = threading.Thread(target=self._rush_f, args=(['f'],))
                t.setDaemon(True)
                t.start()

        def rush_w_g(self, _):
                """
                自动开船
                """
                if self.rush_flags:
                        return
                self.rush_flags = True
                t = threading.Thread(target=self._rush_f, args=(['w', 'g'], 1))
                t.setDaemon(True)
                t.start()

        def _rush_f(self, keys, wait_time=0.05):
                while self.rush_flags:
                        for x in keys:
                                core.keyboardHwnd.input_key(x, self.hwnd)
                                core.wait.random_wait(wait_time)

        def rush_click(self, _):
                """
                连续左键
                """
                if self.rush_flags:
                        return
                self.rush_flags = True
                t = threading.Thread(target=self._rush_click, args=())
                t.setDaemon(True)
                t.start()

        def _rush_click(self):
                if self.hwnd is None:
                        mouse_x, mouse_y = mouseListen.mouseListen.mouse_position()
                else:
                        mouse_x, mouse_y = self.mouse_x, self.mouse_y
                while self.rush_flags:
                        core.mouseGlob.click('left', mouse_x, mouse_y, self.hwnd, wait=.3)
                        core.wait.random_wait()


wuxiaMapping = _WuxiaMapping()
