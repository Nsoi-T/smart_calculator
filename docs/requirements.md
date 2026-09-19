# Smart Calculator - Requirements Document

## 1. Overview

Smart Calculator is a Python desktop application with four calculator modules:

- Module A: Basic arithmetic
- Module B: Advanced mathematical operations
- Module C: Statistical calculations
- Module D: X/Y line graph display

The modules are connected through a PySimpleGUI application in `src/main.py`.

## 2. Environment Requirements

- Python 3.10 or later
- PySimpleGUI 5.0 or later
- A desktop environment capable of displaying a GUI window

Install dependencies with:

```bash
python -m pip install -r requirements.txt
```

## 3. Functional Requirements

### 3.1 Module A: Basic Calculator

The application must provide:

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers
- Power calculation
- Modulus calculation

Division by zero and modulus by zero must produce a user-handled error.

### 3.2 Module B: Advanced Calculator

The application must provide:

- Square root with negative-input validation
- Logarithm with a default base of 10
- Sine, cosine, and tangent using degree input
- Factorial with non-negative integer validation
- Absolute value

Invalid mathematical input must produce a user-handled error.

### 3.3 Module C: Statistical Calculator

The application must accept comma-separated numbers and provide:

- Sum
- Mean
- Median
- Mode
- Population variance
- Population standard deviation
- Maximum
- Minimum

Operations that require data must reject empty input.

### 3.4 Module D: Graph Display

The application must provide two input fields for:

- X values
- Y values

Values may be entered as comma-separated numbers, optionally surrounded by parentheses or square brackets. For example:

```text
X values: (1, 2, 3, 4)
Y values: (10, 20, 30, 40)
```

The graph must:

- Require non-empty X and Y data
- Require equal numbers of X and Y values
- Display the points in input order
- Space X points evenly across the graph
- Show X and Y value labels
- Draw a horizontal X-axis
- Draw lines between consecutive points
- Display each coordinate beside its point
- Provide a dedicated Insert Graph action

### 3.5 Input and Display Behavior

The application must:

- Convert valid integer and decimal text into numeric values
- Display a clear error message for invalid input
- Allow the user to clear current inputs and results
- Allow the user to clear operation history
- Keep the GUI responsive while it is running

## 4. Integration Requirements

The main application must:

- Register all four calculator modules
- Provide module selection buttons
- Display the correct controls for the selected module
- Route operations to the correct calculator class
- Maintain a visible operation history
- Display calculation and graph results in the GUI

The integrated `SmartCalculator` class must also support:

- Basic, advanced, and statistical calculator objects
- Operation logging
- Clearing operation history
- Reading operation history
- Combined statistical analysis through `analyze_data()`

## 5. Error-Handling Requirements

The application must handle, without unexpectedly closing:

- Non-numeric input
- Empty list input
- Division by zero
- Modulus by zero
- Negative square-root input
- Non-positive logarithm input
- Invalid factorial input
- Empty graph data
- Graph X/Y lists with different lengths

## 6. Documentation Requirements

The project must include documentation for:

- Installation
- Running the application
- Running tests
- Each calculator module
- Each public function and class method
- Graph input format and behavior

The detailed function documentation is in `docs/function_reference.md`.

## 7. Testing Requirements

The project must include:

- Unit tests for Modules A, B, C, and D
- Integration tests for the main application
- Integration tests for the combined `SmartCalculator`
- Tests for valid calculations
- Tests for invalid input and edge cases
- Tests for graph point placement, labels, spacing, and line drawing

Run the complete test suite with:

```bash
python -m unittest discover -s tests -p "test*.py"
```

The current test suite contains 27 tests.

## 8. Quality Requirements

- Keep modules independent and reusable.
- Use clear function and class names.
- Keep GUI code in `src/main.py` and calculation logic in the module files.
- Avoid committing generated cache files such as `__pycache__` and `.pytest_cache`.
- Keep dependencies listed in `requirements.txt` and package metadata in `setup.py`.
