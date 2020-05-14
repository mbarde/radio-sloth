from channel_loader import load_channels_from_config

import time
import pyttsx3


ttsEngine = pyttsx3.init()


def audioLog(message):
    print('[AUDIO] {0}'.format(message))
    ttsEngine.say(message)
    ttsEngine.runAndWait()


channels = load_channels_from_config('channels.json')
audioLog('Listening to {0}'.format(channels[0].title))
channels[0].play()
time.sleep(10)
channels[0].stop()
