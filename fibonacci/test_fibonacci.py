import unittest
import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci.fibonacci(2), [1, 2])


if __name__ == '__main__':
    unittest.main()