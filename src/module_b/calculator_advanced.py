import math


class AdvancedCalculator:

    def square_root(self, x):

        if x < 0:

            raise ValueError("Cannot calculate square root of negative number")

        return math.sqrt(x)

    def logarithm(self, x, base=10):

        if x <= 0:

            raise ValueError("Logarithm undefined for non-positive numbers")

        return math.log(x, base)

    def sine(self, angle_degrees):

        return math.sin(math.radians(angle_degrees))

    def cosine(self, angle_degrees):

        return math.cos(math.radians(angle_degrees))

    def tangent(self, angle_degrees):

        return math.tan(math.radians(angle_degrees))

    def factorial(self, n):

        if n < 0 or not isinstance(n, int):

            raise ValueError(
                "Factorial only defined for non-negative integers")

        return math.factorial(n)

    def absolute(self, x):

        return abs(x)
