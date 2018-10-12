__all__ = ['KeyLocker']


class KeyLocker:
        def __init__(self):
                self._locker = 0

        def is_lock(self):
                return self._locker > 0

        def lock(self):
                self._locker += 1

        def unlock(self):
                self._locker -= 1
