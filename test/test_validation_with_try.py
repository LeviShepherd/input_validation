import unittest
from input_validation.validation_with_try import *


class MyTestCase(unittest.TestCase):

    # Test for score1 as a negative
    def test_average_negative_input(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)


if __name__ == '__main__':
    unittest.main()
