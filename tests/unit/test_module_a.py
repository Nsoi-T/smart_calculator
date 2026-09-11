import unittest 

from src.module_a.calculator_basic import BasicCalculator 

 

class TestBasicCalculator(unittest.TestCase): 

    """Test cases for Basic Calculator Module""" 

     

    def setUp(self): 

        """Set up test fixture""" 

        self.calc = BasicCalculator() 

     

    def test_add(self): 

        """Test addition operation""" 

        self.assertEqual(self.calc.add(2, 3), 5) 

        self.assertEqual(self.calc.add(-1, 1), 0) 

        self.assertEqual(self.calc.add(0, 0), 0) 

        self.assertEqual(self.calc.add(2.5, 3.5), 6.0) 

     

    def test_subtract(self): 

        """Test subtraction operation""" 

        self.assertEqual(self.calc.subtract(5, 3), 2) 

        self.assertEqual(self.calc.subtract(0, 5), -5) 

        self.assertEqual(self.calc.subtract(-5, -3), -2) 

     

    def test_multiply(self): 

        """Test multiplication operation""" 

        self.assertEqual(self.calc.multiply(2, 3), 6) 

        self.assertEqual(self.calc.multiply(0, 5), 0) 

        self.assertEqual(self.calc.multiply(-2, 3), -6) 

     

    def test_divide(self): 

        """Test division operation""" 

        self.assertEqual(self.calc.divide(6, 3), 2) 

        self.assertEqual(self.calc.divide(5, 2), 2.5) 

        self.assertRaises(ValueError, self.calc.divide, 5, 0) 

     

    def test_power(self): 

        """Test power operation""" 

        self.assertEqual(self.calc.power(2, 3), 8) 

        self.assertEqual(self.calc.power(5, 0), 1) 

        self.assertEqual(self.calc.power(4, 0.5), 2) 

     

    def test_modulus(self): 

        """Test modulus operation""" 

        self.assertEqual(self.calc.modulus(7, 3), 1) 

        self.assertEqual(self.calc.modulus(10, 5), 0) 

        self.assertRaises(ValueError, self.calc.modulus, 5, 0) 

 

if __name__ == '__main__': 

    unittest.main() 