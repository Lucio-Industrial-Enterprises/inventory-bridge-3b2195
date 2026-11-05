import unittest

from warehouse.quantity import parse_quantity


class ParseQuantityTests(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(parse_quantity("5"), 5)

    def test_whitespace_padded(self):
        self.assertEqual(parse_quantity("  12  "), 12)

    # Regression: zero must be accepted
    def test_zero(self):
        self.assertEqual(parse_quantity("0"), 0)

    # Regression: negative values must be rejected
    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-1")

    def test_large_negative_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("-100")

    def test_non_numeric_raises(self):
        with self.assertRaises(ValueError):
            parse_quantity("abc")
