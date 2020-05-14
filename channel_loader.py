from stream_channel import StreamChannel

import json


def load_channels_from_config(configFileName):
    channels = []
    f = open(configFileName, 'r')
    configText = f.read()
    config = json.parse(configText)
    for channelCfg in config['channels']:
        if config['title'] == 'StreamChannel':
            channels.append(StreamChannel(channelCfg))
    return channels
