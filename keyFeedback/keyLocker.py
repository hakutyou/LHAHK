__all__ = ['KeyLocker']


class KeyLocker:
        def __init__(self):
                self._locker = False

        def is_lock(self):
                return self._locker

        def lock(self):
                self._locker = True

        def unlock(self):
                self._locker = False
