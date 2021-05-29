from abc import ABC, abstractmethod


class OutputFormatter(ABC):
    def __init__(self, plagiarism_compare):
        self.plagiarism_compare = plagiarism_compare

        self.headers = list(map(lambda x: x.name, self.plagiarism_compare.file_instances))

    @abstractmethod
    def format(self):
        pass

    @abstractmethod
    def format_suspicious(self):
        pass

    def export(self, path):
        file = open(path, "w")
        file.write(self.format())

    def export_suspicious(self, path):
        file = open(path, "w")
        file.write(self.format_suspicious())
