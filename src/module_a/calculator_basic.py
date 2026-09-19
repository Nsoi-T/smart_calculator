class BasicCalculator:
    """Basic calculator with common operations."""

    def __init__(self, logger=None):
        self.logger = logger

    def _log(self, operation, args, result):
        if self.logger:
            self.logger(operation, args, result)

    def add(self, a, b):
        result = a + b
        self._log("add", (a, b), result)
        return result

    def subtract(self, a, b):
        result = a - b
        self._log("subtract", (a, b), result)
        return result

    def multiply(self, a, b):
        result = a * b
        self._log("multiply", (a, b), result)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")

        result = a / b
        self._log("divide", (a, b), result)
        return result

    def power(self, base, exponent):
        result = base**exponent
        self._log("power", (base, exponent), result)
        return result

    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")

        result = a % b
        self._log("modulus", (a, b), result)
        return result
