# coding=utf-8

__all__ = ['mouseInfo']

import win32gui


class MouseInfo:
        def __init__(self):
                pass

        @staticmethod
        def mouse_position(hwnd=None):
                x, y = win32gui.GetCursorPos()
                if hwnd is None:
                        return x, y
                return win32gui.ScreenToClient(hwnd, (x, y))

        @staticmethod
        def window_position(hwnd=None):  # x_top, y_top, x_bottom, y_bottom
                if hwnd is None:
                        hwnd = win32gui.GetForegroundWindow()
                return win32gui.GetWindowRect(hwnd)


mouseInfo = MouseInfo()
