#!/usr/bin/python3
"""unittests for the function max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """define different scenarions of max_integer"""

    def test_max_integer(self):
        """Test case for a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        """Test case for a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        """Test case for a list of mixed integers"""
        self.assertEqual(max_integer([-10, 5, 0, 10, -20]), 10)

        """Test case for an empty list"""
        self.assertIsNone(max_integer([]))

        """Test case for a list with only one element"""
        self.assertEqual(max_integer([5]), 5)

        """Test case for a list of floats"""
        self.assertEqual(max_integer([1.5, 2.6, 3.7, 4.9]), 4.9)


if __name__ == '__main__':
    unittest.main()
