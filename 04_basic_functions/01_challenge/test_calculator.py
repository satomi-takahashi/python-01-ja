import unittest
from calculator import add, subtract, multiply, divide


class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add("hello", 5), "bad input")
        self.assertEqual(add("hello", "world"), "bad input")
        self.assertEqual(add("5", 5), "bad input")
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract("hello", 5), "bad input")
        self.assertEqual(subtract("hello", "world"), "bad input")
        self.assertEqual(subtract("5", 5), "bad input")
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply("hello", 5), "bad input")
        self.assertEqual(multiply("hello", "world"), "bad input")
        self.assertEqual(multiply("5", 5), "bad input")
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4.0)
        self.assertEqual(divide("hello", 5), "bad input")
        self.assertEqual(divide("hello", "world"), "bad input")
        self.assertEqual(divide("5", 5), "bad input")
        self.assertAlmostEqual(divide(10, 3), 3.3333333333333335)
        self.assertEqual(divide(5, 0), "Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()