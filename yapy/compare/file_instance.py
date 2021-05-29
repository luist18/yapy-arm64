import os
import re
import unidecode

from yapy.parser.parser import Parser


class FileInstance:

    def __init__(self, path):
        self.path = path

        self.__read_file()
        self.__parse_file()

    def __read_file(self):
        try:
            self.name = os.path.basename(self.path)
            self.original_name = self.name

            match = re.search(r"(.*_)?.*?_up(\d{9})_.*\.s$", self.name)

            if match:
                self.name = match.group(2)
                
            contents = open(
                self.path, 'r', encoding='utf8', errors='replace').read()

            self.contents = unidecode.unidecode(contents)
        except:
            print(f'Could not read file from path {self.path}')

    def __parse_file(self):
        try:
            self.parsed_file = Parser.parse(self.contents)
        except Exception as e:
            self.parsed_file = None
            print(f'Could not parse file {self.name}\n{e}')

    def is_valid(self):
        return self.parsed_file is not None

    def tokens_table(self):
        return self.parsed_file.tokens_table
