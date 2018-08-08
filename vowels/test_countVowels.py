import unittest
from vowels import countVowels


class TestCountVowels(unittest.TestCase):

    def test_countVowels(self):
        self.assertEqual(countVowels.vowels('aaarfrafr'), (4, 0, 0, 0, 0, 0))
        self.assertEqual(countVowels.vowels('aeiouy'), (1, 1, 1, 1, 1, 1))
        self.assertEqual(countVowels.vowels('nlptgf4t5r7;.l56b4'), (0, 0, 0, 0, 0, 0))


if __name__ == '__main__':
    unittest.main()
