class BaseMapping:
        def __init__(self):
                self.MODE = 'base'

        def press(self):
                return {
                        "#['Rshift', 'S']": lambda _: self.get_mode(),
                }

        def release(self):
                return {}

        def get_mode(self):
                print(self.MODE)
