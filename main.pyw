import pythoncom
import listen.keyListen as keyListen
import feedback.keyFeedback as keyFeedback

debug = False


if __name__ == '__main__':
        key_holder = keyFeedback.init()
        listen = keyListen.KeyListen(keyFeedback.PRESS_MAPPING,
                                     keyFeedback.RELEASE_MAPPING,
                                     key_holder.hold_lock,
                                     debug=debug)
        pythoncom.PumpMessages()
