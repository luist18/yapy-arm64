import os
from ..parser import Parser
from .output.html_formatter import HtmlFormatter


class PlagiarismCompare:

    def __init__(self, files=None, path=None, contents=None):
        self.files = files
        self.path = path
        self.contents = contents

        if contents == None:
            self.__read_files()

        self.__parse_files()

    def __read_files(self):
        if self.path != None:
            self.files = [os.path.join(self.path, file) for file in os.listdir(
                self.path) if os.path.isfile(os.path.join(self.path, file))]

        self.contents = {}

        for filepath in self.files:
            try:
                basename = os.path.basename(filepath)
                self.contents[basename] = open(filepath, 'r').read()
            except:
                print(f'Could not read file from path {filepath}')

    def __parse_files(self):
        self.parsed_files = {}

        for key, value in self.contents.items():
            try:
                self.parsed_files[key] = Parser.parse(value)
            except:
                self.parsed_files[key] = None
                print(f'Could not parse file {key}')

    def compare(self, score_function):
        self.result = [None*len(self.contents)
                       for ignored in range(len(self.contents))]

        for i in range(0, len(self.contents) - 1):
            for j in range(i + 1, len(self.contents)):
                lhs = self.parsed_files.values[i]
                rhs = self.parsed_files.values[j]
                self.result[i][j] = 0 if lhs == None or rhs == None else score_function(
                    lhs, rhs)
