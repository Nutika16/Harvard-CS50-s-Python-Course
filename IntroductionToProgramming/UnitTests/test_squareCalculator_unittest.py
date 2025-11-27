import unittest
from squareCalculator import square

class TestSquare(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(square(3), 9)

    def test_zero(self):
        self.assertEqual(square(0), 0)

    def test_negative(self):
        self.assertEqual(square(-2), 4)

if __name__ == "__main__":
    unittest.main()

