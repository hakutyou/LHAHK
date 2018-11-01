__all__ = ['general_exception', 'PathException', 'ObjectException']

import setting


def general_exception(err_ret=False):
        def deco(func):
                def __wrap(*args, **kwargs):
                        try:
                                return func(*args, **kwargs)
                        except ObjectException as e:
                                if e.t is True:
                                        setting.info('ObjectException, {0}'.format(str(e)))
                                else:
                                        setting.debug('ObjectException, {0}'.format(str(e)))
                                return err_ret
                        except PathException as e:
                                if e.t is True:
                                        setting.info('PathException, {0}'.format(str(e)))
                                else:
                                        setting.debug('PathException, {0}'.format(str(e)))
                                return err_ret
                        except Exception as e:
                                setting.info(str(e))
                                return err_ret
                return __wrap
        return deco


class PathException(Exception):
        def __init__(self, message='path error', t=True):
                super(__class__, self).__init__(message)
                self.t = t


class ObjectException(Exception):
        def __init__(self, message='path error', t=True):
                super(__class__, self).__init__(message)
                self.t = t
