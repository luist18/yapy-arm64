import os
from yapy.compare.output.csv_formatter import CSVFormatter
from yapy.compare.output.json_formatter import JSONFormatter
from yapy.parser.parser import Parser
from yapy.compare.output.html_formatter import HtmlFormatter


class PlagiarismCompare:

    def __init__(self, files=None, path=None, contents=None, threshold=None):
        self.files = files
        self.path = path
        self.contents = contents
        self.threshold = threshold

        if contents == None:
            self.__read_files()

        self.__parse_files()
        self.html_formatter = HtmlFormatter(self)
        self.json_formatter = JSONFormatter(self)
        self.csv_formatter = CSVFormatter(self)

    def __read_files(self):
        if self.path != None:
            self.files = [os.path.join(self.path, file) for file in os.listdir(
                self.path) if os.path.isfile(os.path.join(self.path, file))]

        self.contents = {}

        for filepath in self.files:
            try:
                basename = os.path.basename(filepath)
                self.contents[basename] = open(
                    filepath, 'r', encoding='utf8', errors='replace').read()
            except:
                print(f'Could not read file from path {filepath}')

    def __parse_files(self):
        self.parsed_files = {}

        for key, value in self.contents.items():
            try:
                self.parsed_files[key] = Parser.parse(value)
            except Exception as e:
                print(e)
                self.parsed_files[key] = None
                print(f'Could not parse file {key}')

    def compare(self, score_function):
        self.result = [[None]*len(self.contents)
                       for ignored in range(len(self.contents))]

        results = list(self.parsed_files.values())
        for i in range(0, len(self.contents) - 1):
            for j in range(i + 1, len(self.contents)):
                lhs = results[i]
                rhs = results[j]

                if lhs is None or rhs is None:
                    score = None
                else:
                    tmp_score = score_function(
                        lhs.tokens_table, rhs.tokens_table)
                        
                    score = None if self.threshold is not None and tmp_score < self.threshold else tmp_score

                self.result[i][j] = score
