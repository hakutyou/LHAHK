__all__ = ['hold', 'release', 'init']

_key_holder = None


def init(key_holder):
        global _key_holder
        _key_holder = key_holder
        pass


def hold(key: str, extra=0):
        # print('hold')
        _key_holder.press(key, extra)


def release(key: str, extra=0):
        # print('release')
        _key_holder.release(key, extra)
