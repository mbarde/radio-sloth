from abc import ABC, abstractmethod


class Channel(ABC):

    def __init__(self, config):
        self.title = config['title']
        self.description = config['description']
        self.args = config['args']
        super().__init__()

    @abstractmethod
    def play(self):
        pass

    def stop(self):
        pass
