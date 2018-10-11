__all__ = ['KeyLocker']


class KeyLocker:
        def __init__(self):
                self.locker = False

        def is_lock(self):
                return self.locker

        def lock(self):
                self.locker = True

        def unlock(self):
                self.locker = False
