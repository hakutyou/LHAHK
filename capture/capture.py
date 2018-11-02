# coding=utf-8

import win32gui
import win32ui
from ctypes import windll
import math
from PIL import Image  # pillow
import numpy as np
import setting
import exception


class Capture:
        def __init__(self):
                self.image = None

        @exception.general_exception(False)
        def shot(self, hwnd=None) -> bool:
                if hwnd is None:
                        setting.debug('Get active window')
                        hwnd = windll.user32.GetForegroundWindow()

                wdc = win32gui.GetWindowDC(hwnd)
                dc_obj = win32ui.CreateDCFromHandle(wdc)
                cdc = dc_obj.CreateCompatibleDC()

                left, top, right, bottom = win32gui.GetClientRect(hwnd)
                w = (right - left)
                h = (bottom - top)

                save_bit_map = win32ui.CreateBitmap()
                save_bit_map.CreateCompatibleBitmap(dc_obj, w, h)
                cdc.SelectObject(save_bit_map)
                if windll.user32.PrintWindow(hwnd, cdc.GetSafeHdc(), 1):
                        cdc.DeleteDC()
                        dc_obj.DeleteDC()
                        win32gui.ReleaseDC(hwnd, wdc)

                        bmp_info = save_bit_map.GetInfo()
                        bmp_bits = save_bit_map.GetBitmapBits(True)
                        win32gui.DeleteObject(save_bit_map.GetHandle())
                        self.image = Image.frombuffer('RGB',
                                                      (bmp_info['bmWidth'], bmp_info['bmHeight']),
                                                      bmp_bits, 'raw', 'BGRX', 0, 1)
                        return True
                else:
                        self.image = None
                        raise exception.ObjectException('Can\'t get image!')

        @exception.general_exception(False)
        def crop(self, left: int = 0, top: int = 0, width: int = 0, height: int = 0) -> bool:
                if self.image is None:
                        raise exception.ObjectException('Can\'t get image!')
                x_max = self.image.size[0]
                y_max = self.image.size[1]
                if left < 0 or top < 0 or width < 0 or height < 0 \
                        or left + width > x_max or top + height > y_max:
                        raise Exception('wrong argument: {left} {top} {width} {height} with'
                                        'window {window_width} {window_height}'.format(
                                                left=left, top=top, width=width, height=height,
                                                window_width=x_max, window_height=y_max))
                right = x_max if width == 0 else left + width
                bottom = y_max if height == 0 else top + height
                self.image = self.image.crop((left, top, right, bottom))
                return True

        @exception.general_exception(False)
        def resize(self, width: int = 0, height: int = 0) -> bool:
                if self.image is None:
                        raise exception.ObjectException('Can\'t get image!')
                if width < 0 or height < 0:
                        raise Exception('wrong argument: {width} {height}'.format(
                                width=width, height=height))
                width = self.image.size[0] if width == 0 else width
                height = self.image.size[1] if height == 0 else height
                self.image = self.image.resize((width, height), Image.ANTIALIAS)
                return True

        @exception.general_exception(False)
        def file(self, path: str) -> bool:
                self.image = Image.open(path)
                return True

        @exception.general_exception(False)
        def save(self, path: str) -> bool:
                if self.image is None:
                        raise exception.ObjectException('Can\'t get image!')
                self.image = self.image.save(path)
                return True

        @exception.general_exception(float('+inf'))
        def similar(self, path: str, grey: bool = False) -> float:
                def __convert(image):
                        if grey:
                                return image.convert('L')
                        return image

                if self.image is None:
                        raise exception.ObjectException('Can\'t get image!')
                h_image_1 = __convert(self.image).histogram()
                h_image_2 = __convert(Image.open(path)).histogram()
                return math.sqrt(sum(map(lambda a, b: (a - b) ** 2, h_image_1, h_image_2)) / len(h_image_1))

        @exception.general_exception(False)
        def show(self) -> bool:
                if self.image is None:
                        raise exception.ObjectException('Can\'t get image!')
                self.image = self.image.convert('L')
                self.image.show()
                return True

        @property
        @exception.general_exception(np.asanyarray([]))
        def network_data(self):
                if self.image is None:
                        raise exception.ObjectException('Can\'t get image!')
                # !!!Need fix here!!!
                return np.asarray(self.image.convert('1')).flatten() / 255


if __name__ == '__main__':
        from network.resnet import ResNet
        import time

        resnet = ResNet()
        resnet.build()

        capture = Capture()
        # while True:
        # time.sleep(1)
        capture.shot()
        capture.crop(1409, 800, 8, 23)
        capture.resize(28, 28)
        print(resnet.read(capture.network_data))
        # capture.file('C:/Users/kakoi/Desktop/1/1.bmp')
        # capture.resize(100, 200)
        # capture.shot()
        # capture.crop(100, 0, 100, 300)
        # result = capture.similar('C:/Users/kakoi/Desktop/1/1.bmp', grey=False)
        # print(result)
        # capture.save('')
        capture.show()
