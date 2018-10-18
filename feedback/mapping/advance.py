__all__ = ['advanceMapping']

from ..base import mapping
from .. import simulation
from .. import mouseListen

from . import base
from . import normal


class _AdvanceMapping(base.BaseMapping):
        """
        Advance: 命令模式
        可切换以下模式 [S]: Normal
        """
        def __init__(self):
                super().__init__()
                self.MODE = 'advance'

        def press(self):
                return dict({
                        "#['A']": self._reverse_window_title,
                        "#['S']": lambda _: mapping.mode_switch(normal.normalMapping),
                        "#['D']": lambda _: simulation.press('left_win'),
                        "#['F']": self.cmd_input,
                        "#['G']": lambda _: self.mouse_right(True),
                        "#['H']": self.mouse_double_click,
                        "#['Q']": self.cmd_mouse_click,
                }, **super().press())

        def release(self):
                return dict({
                        "['D']": lambda _: simulation.release('left_win'),
                        "['G']": lambda _: self.mouse_right(False),
                }, **super().press())

        def _reverse_window_title(self, window_name: str):
                """
                反向打印激活窗口标题
                """
                if self._action_head(self._reverse_window_title):
                        return
                print(window_name[::-1])

        @staticmethod
        def mouse_right(down):
                x, y = mouseListen.mouseListen.mouse_position()
                if down:
                        simulation.mouse_down('right', x, y)
                else:
                        simulation.mouse_up('right', x, y)

        @staticmethod
        def mouse_double_click(_):
                x, y = mouseListen.mouseListen.mouse_position()
                simulation.double_click('left', x, y)

        @staticmethod
        def cmd_input(_):
                import win32gui
                hwnd = win32gui.FindWindow(0, 'G:\Windows\system32\cmd.exe')
                simulation.input_string('ls', hwnd)
                simulation.random_wait()
                simulation.input_key('enter', hwnd)

        @staticmethod
        def cmd_mouse_click(_):
                import win32gui
                hwnd = win32gui.FindWindow(0, 'G:\Windows\system32\cmd.exe')
                simulation.click('right', 0, 0, hwnd)


advanceMapping = _AdvanceMapping()
