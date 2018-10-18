__all__ = ['BaseMapping']


class BaseMapping:
        """
        Base: base function for every mode
        """
        def __init__(self):
                self.MODE = 'base'
                self.HELP = False

        def press(self):
                return {
                        "#['Rshift', 'S']": self.__get_mode,
                }

        def release(self):
                return {}

        def __get_mode(self, _):
                """
                打印当前模式
                """
                print(self.MODE)
