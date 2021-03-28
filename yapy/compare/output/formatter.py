from abc import ABC, abstractmethod


class OutputFormatter(ABC):
    def __init__(self, plagiarism_compare):
        self.plagiarism_compare = plagiarism_compare

        self.headers = list(self.plagiarism_compare.contents.keys())

    @abstractmethod
    def format(self):
        pass

    def export(self, path):
        file = open(path, "w")
        file.write(self.format())
