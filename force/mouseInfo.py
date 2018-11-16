# coding=utf-8

__all__ = ['mouse_position', 'window_position', 'window_relative_position']

import win32gui


def mouse_position(hwnd=None):
        x, y = win32gui.GetCursorPos()
        if hwnd is None:
                return x, y
        return win32gui.ScreenToClient(hwnd, (x, y))


def window_edge_size(hwnd=None):
        if hwnd is None:
                hwnd = win32gui.GetForegroundWindow()
        l, t, r, b = win32gui.GetWindowRect(hwnd)
        _, _, w, h = win32gui.GetClientRect(hwnd)
        x_err = int((r - l - w) / 2)
        y_err = b - t - h - x_err
        return x_err, y_err


def window_position(hwnd=None):  # x_top, y_top, x_bottom, y_bottom
        if hwnd is None:
                hwnd = win32gui.GetForegroundWindow()
        l, t, r, b = win32gui.GetWindowRect(hwnd)
        _, _, w, h = win32gui.GetClientRect(hwnd)
        x_err = int((r - l - w) / 2)
        y_err = b - t - h - x_err
        return l + x_err, t + y_err, r - x_err, b - x_err


def window_relative_position(hwnd=None):
        if hwnd is None:
                hwnd = win32gui.GetForegroundWindow()
        return win32gui.GetClientRect(hwnd)
