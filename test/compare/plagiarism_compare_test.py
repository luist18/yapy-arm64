from unittest import TestCase

from yapy import PlagiarismCompare
from yapy.score.similarity_score import sorensen_dice_coefficient


class PlagiarismCompareTest(TestCase):
    def test_parse(self):
        p_compare = PlagiarismCompare(path='test/resources/ex4')
        p_compare.compare(sorensen_dice_coefficient)
        p_compare.csv_formatter.export('test.csv')

    def test_true(self):
        self.assertTrue(True)
