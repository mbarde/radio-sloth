import vlc
import time
import pyttsx3


ttsEngine = pyttsx3.init()


def audioLog(message):
    print('[AUDIO] {0}'.format(message))
    ttsEngine.say(message)
    ttsEngine.runAndWait()


uri = 'http://ice3.somafm.com/groovesalad-256-mp3'
# uri = 'file:///home/mbarde/projects/ttstest/groovesalad256.pls'
player = vlc.MediaPlayer(uri)
player.play()
time.sleep(2)
audioLog('Listening to Groove Salad')
time.sleep(300)
audioLog('Ye-ha, Schweinebacke!')


'''
from channel_loader import load_channels_from_config


channels = load_channels_from_config('channels.json')
audioLog('Listening to {0}'.channel[0].title)
channels[0].play()
time.sleep(100)
'''
