# coding=utf-8

__all__ = ['random_wait']

import time
import random


def random_wait(interval: float=0.05, deviation: float=0.025) -> None:
        minimum = max(0.0, interval - deviation)
        maximum = interval + deviation
        time.sleep(random.random() * (maximum - minimum) + minimum)
