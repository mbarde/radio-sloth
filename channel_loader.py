from stream_channel import StreamChannel

import json


def load_channels_from_config(configFileName):
    channels = []
    f = open(configFileName, 'r')
    configText = f.read()
    config = json.loads(configText)
    for channelConfig in config['channels']:
        if channelConfig['type'] == 'StreamChannel':
            channels.append(StreamChannel(channelConfig))
    return channels
