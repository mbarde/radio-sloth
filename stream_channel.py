from channel import Channel

import random
import vlc


class StreamChannel(Channel):

    def __init__(self, config):
        super().__init__(config)
        self.urls = self.args['urls']
        self.player = None

    def play(self):
        url = random.choice(self.urls)
        self.player = vlc.MediaPlayer(url)
        self.player.play()

    def stop(self):
        if self.player is not None:
            self.player.stop()
