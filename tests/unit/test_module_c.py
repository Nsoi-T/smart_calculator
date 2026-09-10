import unittest
from src.module_c.calculator_stats import StatisticalCalculator

class TestStatisticalCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc       = StatisticalCalculator()
        self.test_data  = [1,2,3,4,5,6,7,8,9,10]
        
    def test_mean(self):
        self.assertEqual(self.calc.mean(self.test_data), 5.5)
        self.assertEqual(self.calc.mean([1,2,3]),2)
        self.assertRaises(ValueError, self.calc.mean, [])

from src.module_c.calculator_stats import StatisticalCalculator 

 

class TestStatisticalCalculator(unittest.TestCase): 

    """Test cases for Statistical Calculator Module""" 

     

    def setUp(self): 

        self.calc = StatisticalCalculator() 

        self.test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

     

    def test_mean(self): 

        """Test mean calculation""" 

        self.assertEqual(self.calc.mean(self.test_data), 5.5) 

        self.assertEqual(self.calc.mean([1, 2, 3]), 2) 

        self.assertRaises(ValueError, self.calc.mean, []) 

     

    def test_median(self): 

        """Test median calculation""" 

        self.assertEqual(self.calc.median(self.test_data), 5.5) 

        self.assertEqual(self.calc.median([1, 2, 3]), 2) 

        self.assertEqual(self.calc.median([1, 2, 3, 4]), 2.5) 

     

    def test_mode(self): 

        """Test mode calculation""" 

        self.assertEqual(self.calc.mode([1, 1, 2, 2, 3]), [1, 2]) 

        self.assertEqual(self.calc.mode([1, 2, 3, 3, 3]), [3]) 

        self.assertRaises(ValueError, self.calc.mode, []) 

     

    def test_variance(self): 

        """Test variance calculation""" 

        self.assertEqual(self.calc.variance([1, 2, 3]), 0.6666666666666666) 

        self.assertRaises(ValueError, self.calc.variance, []) 

     

    def test_standard_deviation(self): 

        """Test standard deviation calculation""" 

        self.assertEqual(self.calc.standard_deviation([1, 2, 3]), 0.816496580927726) 

     

    def test_max_value(self): 

        """Test maximum value""" 

        self.assertEqual(self.calc.max_value([1, 5, 3, 8, 2]), 8) 

        self.assertRaises(ValueError, self.calc.max_value, []) 

     

    def test_min_value(self): 

        """Test minimum value""" 

        self.assertEqual(self.calc.min_value([1, 5, 3, 8, 2]), 1) 

        self.assertRaises(ValueError, self.calc.min_value, []) 

     

    def test_sum_data(self): 

        """Test sum calculation""" 

        self.assertEqual(self.calc.sum_data([1, 2, 3, 4]), 10) 

        self.assertEqual(self.calc.sum_data([]), 0) 

 

if __name__ == '__main__': 

    unittest.main() 