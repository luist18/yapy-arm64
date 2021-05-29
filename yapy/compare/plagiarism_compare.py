import os

from yapy.compare.file_instance import FileInstance
from yapy.compare.output.csv_formatter import CSVFormatter
from yapy.compare.output.html_formatter import HtmlFormatter
from yapy.compare.output.json_formatter import JSONFormatter
from yapy.parser.parser import Parser


class PlagiarismCompare:

    def __init__(self, files=None, path=None, threshold=None):
        self.files = files
        self.path = path
        self.threshold = threshold
        self.result_files = []

        self.__read_files()
        self.html_formatter = HtmlFormatter(self)
        self.json_formatter = JSONFormatter(self)
        self.csv_formatter = CSVFormatter(self)

    def __read_files(self):
        if self.path != None:
            self.files = [os.path.join(self.path, file) for file in os.listdir(
                self.path) if os.path.isfile(os.path.join(self.path, file))]

        self.file_instances = []
        self.error_files = []

        for filepath in self.files:
            try:
                file_instance = FileInstance(filepath)

                if file_instance.is_valid():
                    self.file_instances.append(file_instance)
                else:
                    self.error_files.append(file_instance)
            except:
                print(f'Could not read file from path {filepath}')

    def compare(self, score_function):
        self.result = [[None]*len(self.file_instances)
                       for ignored in range(len(self.file_instances))]

        for i in range(0, len(self.file_instances) - 1):
            for j in range(i + 1, len(self.file_instances)):
                lhs = self.file_instances[i]
                rhs = self.file_instances[j]

                if lhs is None or rhs is None:
                    score = None
                else:
                    tmp_score = score_function(
                        lhs.tokens_table(), rhs.tokens_table())

                    if self.threshold is None or tmp_score >= self.threshold:
                        score = tmp_score
                        self.result_files.append({
                            "lhs": lhs.original_name,
                            "rhs": rhs.original_name,
                            "similarity": score
                        })
                    else:
                        score = None

                self.result[i][j] = score
