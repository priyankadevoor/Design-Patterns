from abc import ABC, abstractmethod

class Subscriber:
    @abstractmethod
    def on_message(self, message):
        pass