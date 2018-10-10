import pythoncom
import keyListen.keyListen as keyListen
import keyFeedback.keyFeedback as keyFeedback

debug = True


if __name__ == '__main__':
        key_feedback = keyFeedback.KeyFeedback(debug=debug)
        listen = keyListen.KeyListen(keyFeedback.PRESS_MAPPING,
                                     keyFeedback.RELEASE_MAPPING,
                                     debug=debug)
        pythoncom.PumpMessages()
