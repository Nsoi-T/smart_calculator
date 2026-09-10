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

 

if __name__ == '__main__': 

    unittest.main() 