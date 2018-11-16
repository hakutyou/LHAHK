# coding=utf-8

__all__ = ['Image']

import win32gui
import win32ui
from ctypes import windll
import numpy as np
import PIL.Image
import exception
import setting


class Image:
        def __init__(self):
                self.__image = None

        @property
        def image(self):
                return self.__image

        @exception.general_exception(False)
        def shot(self, hwnd=None) -> bool:
                if hwnd is None:
                        setting.debug('Get active window')
                        hwnd = windll.user32.GetForegroundWindow()

                wdc = win32gui.GetWindowDC(hwnd)
                dc_obj = win32ui.CreateDCFromHandle(wdc)
                cdc = dc_obj.CreateCompatibleDC()

                _left, _top, _right, _bottom = win32gui.GetClientRect(hwnd)
                w = (_right - _left)
                h = (_bottom - _top)

                save_bit_map = win32ui.CreateBitmap()
                save_bit_map.CreateCompatibleBitmap(dc_obj, w, h)
                cdc.SelectObject(save_bit_map)

                # cdc.BitBlt((-left-x_err, -top-y_err), (w+2*x_err, h+x_err+y_err), dc_obj, (0, 0), win32con.SRCCOPY)
                result = windll.user32.PrintWindow(hwnd, cdc.GetSafeHdc(), 1)
                if result:
                        cdc.DeleteDC()
                        dc_obj.DeleteDC()
                        win32gui.ReleaseDC(hwnd, wdc)

                        bmp_info = save_bit_map.GetInfo()
                        bmp_bits = save_bit_map.GetBitmapBits(True)
                        win32gui.DeleteObject(save_bit_map.GetHandle())
                        self.__image = PIL.Image.frombuffer('RGB',
                                                            (bmp_info['bmWidth'], bmp_info['bmHeight']),
                                                            bmp_bits, 'raw', 'BGRX', 0, 1)
                        return True
                else:
                        self.__image = None
                        raise exception.ObjectException('Can\'t get image!')

        @exception.general_exception(False)
        def open(self, path: str) -> bool:
                self.__image = PIL.Image.open(path)
                return True

        @exception.general_exception(False)
        def read(self, array: np.array):
                self.__image = PIL.Image.fromarray(array)

        @exception.general_exception(False)
        def show(self) -> bool:
                if self.__image is None:
                        raise exception.ObjectException('Can\'t get image!')
                self.__image = self.__image.convert('L')
                self.__image.show()
                return True

        @exception.general_exception(False)
        def save(self, path: str) -> bool:
                if self.__image is None:
                        raise exception.ObjectException('Can\'t get image!')
                self.__image = self.__image.save(path)
                return True

        @exception.general_exception(False)
        def crop(self, left: int = 0, top: int = 0, width: int = 0, height: int = 0) -> bool:
                if self.__image is None:
                        raise exception.ObjectException('Can\'t get image!')
                x_max = self.__image.size[0]
                y_max = self.__image.size[1]
                if left < 0 or top < 0 or width < 0 or height < 0 \
                        or left + width > x_max or top + height > y_max:
                        raise Exception('wrong argument: {left} {top} {width} {height} with'
                                        'window {window_width} {window_height}'.format(
                                                left=left, top=top, width=width, height=height,
                                                window_width=x_max, window_height=y_max))
                right = x_max if width == 0 else left + width
                bottom = y_max if height == 0 else top + height
                self.__image = self.__image.crop((left, top, right, bottom))
                return True

        @exception.general_exception(False)
        def resize(self, width: int = 0, height: int = 0) -> bool:
                if self.__image is None:
                        raise exception.ObjectException('Can\'t get image!')
                if width < 0 or height < 0:
                        raise Exception('wrong argument: {width} {height}'.format(
                                width=width, height=height))
                width = self.__image.size[0] if width == 0 else width
                height = self.__image.size[1] if height == 0 else height
                self.__image = self.__image.resize((width, height), PIL.Image.ANTIALIAS)
                return True

        @exception.general_exception(False)
        def grey(self) -> bool:
                if self.__image is None:
                        raise exception.ObjectException('Can\'t get image!')
                self.__image = self.__image.convert('L')
                return True
