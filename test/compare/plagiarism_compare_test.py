from unittest import TestCase
import json

from yapy import PlagiarismCompare
from yapy.score.similarity_score import sorensen_dice_coefficient


class PlagiarismCompareTest(TestCase):
    def test_parse(self):
        p_compare = PlagiarismCompare(path='test/resources/debug')
        p_compare.compare(sorensen_dice_coefficient)
        p_compare.html_formatter.export('test.html')

        for file in p_compare.file_instances:
            print(file.name, json.dumps(file.tokens_table(), indent=4))
            print(file.parsed_file.lark_result.pretty())

    def test_true(self):
        self.assertTrue(True)
