from unittest import TestCase
import json

from yapy import PlagiarismCompare
from yapy.score.similarity_score import sorensen_dice_coefficient


class PlagiarismCompareTest(TestCase):
    def test_parse(self):
        p_compare = PlagiarismCompare(path='test/resources/ex5')
        p_compare.compare(sorensen_dice_coefficient)
        p_compare.html_formatter.export('test.html')

    def test_true(self):
        self.assertTrue(True)
