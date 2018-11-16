# coding=utf-8

__all__ = ['transform_array',
           'binary', 'similar']

import math
import numpy as np
import exception
from .image import Image


@exception.general_exception(None)
def transform_array(image: Image):
        if image.image is None:
                raise exception.ObjectException('Can\'t get image!')
        return np.asarray(image.image)


# numpy operation
def binary(array: np.ndarray):  # must input grey image
        def __each_line(line):
                def __each_pixel(pixel):
                        return 255 if pixel > 125 else 0
                return np.array([__each_pixel(l) for l in line])
        return np.array([__each_line(x) for x in array])


# pillow operation
def similar(image_1: Image, image_2: Image):
        h_image_1 = image_1.image.histogram()
        h_image_2 = image_2.image.histogram()
        return math.sqrt(sum(map(lambda a, b: (a - b) ** 2, h_image_1, h_image_2)) / len(h_image_1))
