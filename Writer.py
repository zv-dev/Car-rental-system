from abc import ABC, abstractmethod

class Writer(ABC):
    @abstractmethod
    def print(self, msg):
        pass