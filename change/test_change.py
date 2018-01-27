import unittest
import change


class TestChange(unittest.TestCase):

    def test_change(self):
        self.assertEqual(change.typeofchange(1.11), {'500zl': 0, '200zl': 0, '100zl': 0, '50zl': 0, '20zl': 0, '10zl': 0, '5zl': 0, '2zl': 0, '1zl': 1, '50gr': 0,
          '20gr': 0, '10gr': 1, '5gr': 0, '2gr': 0, '1gr': 1})


if __name__ == '__main__':
    unittest.main()