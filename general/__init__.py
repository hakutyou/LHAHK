# coding=utf-8

__all__ = ['random_wait']

import time
import random


def random_wait(interval=0.05, deviation=0.025):
        time.sleep(2 * random.random() * deviation - deviation + interval)
