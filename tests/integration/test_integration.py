import unittest 

from src.main import SmartCalculator 

class TestIntegration(unittest.TestCase): 

    """Integration tests for the entire system""" 

     

    def setUp(self): 

        self.calc = SmartCalculator() 

     

    def test_basic_integration(self): 

        """Test basic operations integrated""" 

        result = self.calc.basic.add(5, 3) 

        self.assertEqual(result, 8) 

         

        result = self.calc.basic.divide(10, 2) 

        self.assertEqual(result, 5) 

     

    def test_advanced_integration(self): 

        """Test advanced operations integrated""" 

        result = self.calc.advanced.square_root(16) 

        self.assertEqual(result, 4) 

         

        result = self.calc.advanced.factorial(5) 

        self.assertEqual(result, 120) 

     

    def test_stats_integration(self): 

        """Test statistical operations integrated""" 

        data = [1, 2, 3, 4, 5] 

        analysis = self.calc.analyze_data(data) 

         

        self.assertEqual(analysis['sum'], 15) 

        self.assertEqual(analysis['mean'], 3) 

        self.assertEqual(analysis['median'], 3) 

        self.assertEqual(analysis['max'], 5) 

        self.assertEqual(analysis['min'], 1) 

     

    def test_operation_history(self): 

        """Test history logging""" 

        self.calc.basic.add(5, 3) 

        self.calc.basic.multiply(4, 2) 

         

        history = self.calc.get_history() 

        self.assertEqual(len(history), 2) 

        self.assertEqual(history[0]['result'], 8) 

        self.assertEqual(history[1]['result'], 8) 

         

        self.calc.clear_history() 

        self.assertEqual(len(self.calc.get_history()), 0) 

 

if __name__ == '__main__': 

    unittest.main() 

 