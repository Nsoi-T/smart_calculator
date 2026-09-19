import os
import sys
import unittest

PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", ".."))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
for path in (PROJECT_ROOT, SRC_DIR):
    if path not in sys.path:
        sys.path.insert(0, path)

from src.main import (
    CALCULATORS,
    MODULE_INPUTS,
    MODULE_OPERATIONS,
    MODULE_TITLES,
    calculate,
)


class TestMainIntegration(unittest.TestCase):
    """Integration tests for the main calculator dispatch."""

    def test_all_modules_have_calculators_and_titles(self):
        self.assertEqual(
            set(CALCULATORS), {"Module A", "Module B", "Module C"})
        self.assertEqual(
            set(MODULE_TITLES), set(CALCULATORS))
        self.assertEqual(set(MODULE_INPUTS), set(CALCULATORS))

    def test_module_a_calculation(self):
        values = {
            "-FIRST-": "10",
            "-SECOND-": "4",
            "-OPERATION-": "Subtract (-)",
        }
        result = calculate(values, CALCULATORS["Module A"](), "Module A")
        self.assertEqual(result, "10 - 4 = 6")

    def test_module_b_calculation(self):
        values = {
            "-FIRST-": "16",
            "-SECOND-": "",
            "-OPERATION-": "Square root",
        }
        result = calculate(values, CALCULATORS["Module B"](), "Module B")
        self.assertEqual(result, "sqrt(16) = 4.0")

    def test_module_c_calculation(self):
        values = {
            "-FIRST-": "1, 2, 3, 4",
            "-SECOND-": "",
            "-OPERATION-": "Mean",
        }
        result = calculate(values, CALCULATORS["Module C"](), "Module C")
        self.assertEqual(result, "[1, 2, 3, 4] mean = 2.5")

    def test_operations_are_registered_for_each_module(self):
        self.assertEqual(len(MODULE_OPERATIONS["Module A"]), 6)
        self.assertEqual(len(MODULE_OPERATIONS["Module B"]), 7)
        self.assertEqual(len(MODULE_OPERATIONS["Module C"]), 8)


if __name__ == "__main__":
    unittest.main()
