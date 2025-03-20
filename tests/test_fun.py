import unittest
from adip_calculator_unique.functions import add, subtract, multiply, divide, modulo


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        with self.assertRaises(ValueError):
            divide(5, 0)
    def test_modulo(self):
        self.assertEqual(modulo(3,2),1)
        

if __name__ == "__main__":
    unittest.main()
