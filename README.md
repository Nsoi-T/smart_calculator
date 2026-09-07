# Smart Calculator Suite

A modular calculator application with three specialized modules.

## Installation
pip install -r requirements.txt

Running Tests
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=src

# Run specific test file
python -m pytest tests/unit/test_module_a.py

Usage
from src.main import SmartCalculator

calc = SmartCalculator()
result = calc.basic.add(5, 3)
print(result)  # 8
