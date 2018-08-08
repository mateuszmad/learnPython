import unittest
import fizzbuzz


class TestFizzbuzz(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), 'Fizz')
        self.assertEqual(fizzbuzz.fizzbuzz(5), 'Buzz')
        self.assertEqual(fizzbuzz.fizzbuzz(15), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()