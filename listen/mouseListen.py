__all__ = ['mouseListen']

import win32gui


class _MouseListen:
        def __init__(self):
                pass

        @staticmethod
        def mouse_position():
                return win32gui.GetCursorPos()

        @staticmethod
        def window_position(hwnd=None):  # x_top, y_top, x_bottom, y_bottom
                if hwnd is None:
                        hwnd = win32gui.GetForegroundWindow()
                return win32gui.GetWindowRect(hwnd)


mouseListen = _MouseListen()