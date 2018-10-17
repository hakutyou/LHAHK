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
                        "#['Rshift', 'S']": lambda _: self.__get_mode(),
                        "#['Rshift', 'H']": lambda _: self.__get_help(),
                        "#['Rshift', 'F1']": lambda _: self.__detail_help(),
                }

        def release(self):
                return {}

        def __detail_help(self):
                self.HELP = True

        def __get_mode(self):
                print(self.MODE)

        def __get_help(self):
                print(self.__doc__)

        def _action_head(self, caller):
                if self.HELP:
                        print(caller.__doc__)
                        self.HELP = False
                        return True
                return False
