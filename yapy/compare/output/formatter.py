from abc import ABC, abstractmethod


class OutputFormatter(ABC):

    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def export(self, path):
        pass
