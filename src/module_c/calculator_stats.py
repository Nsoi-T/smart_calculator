# -*- coding: utf-8 -*-
from typing import List, Union 

import statistics 

 

class StatisticalCalculator: 

    def mean(self, numbers): 

        if not numbers: 

            raise ValueError("Empty list provided") 

        return sum(numbers) / len(numbers) 

     

    def median(self, numbers): 

        if not numbers: 

            raise ValueError("Empty list provided") 

        sorted_nums = sorted(numbers) 

        n = len(sorted_nums) 

        mid = n // 2 

        if n % 2 == 0:   

            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2 

        return sorted_nums[mid] 

     

    def mode(self, numbers): 

        if not numbers: 

            raise ValueError("Empty list provided") 

        return statistics.multimode(numbers) 

     

    def variance(self, numbers): 

        if not numbers: 

            raise ValueError("Empty list provided") 

        mean_val = self.mean(numbers) 

        return sum((x - mean_val) ** 2 for x in numbers) / len(numbers) 

     

    def standard_deviation(self, numbers): 

        return self.variance(numbers) ** 0.5 

     

    def max_value(self, numbers): 

        if not numbers: 

            raise ValueError("Empty list provided") 

        return max(numbers) 

     

    def min_value(self, numbers): 

        if not numbers: 

            raise ValueError("Empty list provided") 

        return min(numbers) 

     

    def sum_data(self, numbers): 

        return sum(numbers) 

 

# Example
#calculator = StatisticalCalculator()

#numbers = [10, 20, 30, 40, 50]

#result = calculator.mean(numbers)

#print("Mean:", result)


