from src.module_a.calculator_basic import BasicCalculator

from src.module_b.calculator_advanced import AdvancedCalculator

from src.module_c.calculator_stats import StatisticalCalculator

 

class SmartCalculator: 

    """Integrated calculator combining all modules""" 

     

    def __init__(self): 

        self.history = []

        self.basic = BasicCalculator(self.log_operation)

        self.advanced = AdvancedCalculator() 

        self.stats = StatisticalCalculator() 

        self.history = [] 

     

    def log_operation(self, operation, args, result): 

        """Log operation to history""" 

        self.history.append({ 

            'operation': operation, 

            'args': args, 

            'result': result 

        }) 

     

    def clear_history(self): 

        """Clear operation history""" 

        self.history = [] 

     

    def get_history(self): 

        """Get operation history""" 

        return self.history 

     

    # Convenience methods that use all modules 

    def analyze_data(self, numbers): 

        """Perform statistical analysis on data""" 

        return { 

            'sum': self.stats.sum_data(numbers), 

            'mean': self.stats.mean(numbers), 

            'median': self.stats.median(numbers), 

            'mode': self.stats.mode(numbers), 

            'variance': self.stats.variance(numbers), 

            'std_dev': self.stats.standard_deviation(numbers), 

            'max': self.stats.max_value(numbers), 

            'min': self.stats.min_value(numbers) 

        } 

     

    def evaluate_expression(self, expression): 

        """Evaluate a simple mathematical expression""" 

        # This could be extended to parse complex expressions 

        # using all three modules 

        pass 

 

# Example usage 

if __name__ == "__main__": 

    calc = SmartCalculator() 

     

    # Test basic operations 

    print(f"Add: {calc.basic.add(5, 3)}") 

    print(f"Divide: {calc.basic.divide(10, 2)}") 

     

    # Test advanced operations 

    print(f"Square root: {calc.advanced.square_root(16)}") 

    print(f"Factorial: {calc.advanced.factorial(5)}") 

     

    # Test statistical operations 

    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

    analysis = calc.analyze_data(data) 

    print(f"Data analysis: {analysis}") 