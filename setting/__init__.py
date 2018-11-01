# coding=utf-8

__all__ = ['info', 'debug', 'DEBUG', 'TRAY', 'MACS']


DEBUG = False
INFO = True
TRAY = True
MACS = True     # Check Meta Ctrl Shift Win Key


def info(message: str):
        if INFO:
                print('info: {0}'.format(message))


def debug(message: str):
        if DEBUG:
                print('debug: {0}'.format(message))
