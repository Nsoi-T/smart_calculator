# path handler
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", ".."))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")

for module_path in (PROJECT_ROOT, SRC_DIR):
    if os.path.isdir(module_path) and module_path not in sys.path:
        sys.path.insert(0, module_path)

# start of the unit test code
import unittest
from src.module_b.calculator_advanced import AdvancedCalculator


class TestAdvancedCalculator(unittest.TestCase):
    """Test cases for Advanced Calculator Module"""

    def setUp(self):

        self.calc = AdvancedCalculator()

    def test_square_root(self):
        """Test square root function"""

        self.assertEqual(self.calc.square_root(16), 4)

        self.assertEqual(self.calc.square_root(2), 1.4142135623730951)

        self.assertRaises(ValueError, self.calc.square_root, -1)

    def test_logarithm(self):
        """Test logarithm function"""

        self.assertEqual(self.calc.logarithm(100), 2)

        self.assertEqual(self.calc.logarithm(8, 2), 3)

        self.assertRaises(ValueError, self.calc.logarithm, 0)

    def test_sine(self):
        """Test sine function"""

        self.assertAlmostEqual(self.calc.sine(0), 0)

        self.assertAlmostEqual(self.calc.sine(90), 1)

        self.assertAlmostEqual(self.calc.sine(30), 0.5)

    def test_cosine(self):
        """Test cosine function"""

        self.assertAlmostEqual(self.calc.cosine(0), 1)

        self.assertAlmostEqual(self.calc.cosine(60), 0.5)

    def test_tangent(self):
        """Test tangent function"""

        self.assertAlmostEqual(self.calc.tangent(45), 1)

    def test_factorial(self):
        """Test factorial function"""

        self.assertEqual(self.calc.factorial(5), 120)

        self.assertEqual(self.calc.factorial(0), 1)

        self.assertRaises(ValueError, self.calc.factorial, -1)

        self.assertRaises(ValueError, self.calc.factorial, 3.5)

    def test_absolute(self):
        """Test absolute value function"""

        self.assertEqual(self.calc.absolute(-5), 5)

        self.assertEqual(self.calc.absolute(0), 0)

        self.assertEqual(self.calc.absolute(3.14), 3.14)


if __name__ == "__main__":

    unittest.main()
