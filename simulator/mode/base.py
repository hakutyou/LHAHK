__all__ = ['BaseMapping']


class BaseMapping:
        """
        Base: base function for every mode
        """
        def __init__(self):
                self.MODE = 'base'

        def press(self):
                return {}

        def release(self):
                return {}
