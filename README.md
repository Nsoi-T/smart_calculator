# Smart Calculator

Smart Calculator is a Python desktop application with four calculator modules:
basic arithmetic, advanced mathematics, statistics, and X/Y line graphs.

## Requirements

- Python 3.10 or later
- PySimpleGUI 5.0 or later
- A desktop environment for the graphical interface

## Installation

Create a virtual environment in the project directory:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install --upgrade pip setuptools
python -m pip install -r requirements.txt
```

The project can also be installed as a package:

```bash
python -m pip install .
```

## Running the Application

Run the application directly from the project directory:

```bash
python src/main.py
```

If the project was installed as a package, use:

```bash
smart-calculator
```

## Calculator Modules

- **Module A:** Addition, subtraction, multiplication, division, powers, and modulus
- **Module B:** Square root, logarithm, sine, cosine, tangent, factorial, and absolute value
- **Module C:** Sum, mean, median, mode, variance, standard deviation, maximum, and minimum
- **Module D:** X/Y line graph with labels, markers, and connecting lines

The application also provides operation history, input validation, and clear
error messages.

## Using Module D

Select **Module D**, then enter matching comma-separated X and Y values:

```text
X values: (1, 2, 3, 4)
Y values: (10, 20, 30, 40)
```

Parentheses and square brackets are optional. The X and Y lists must contain
the same number of values.

Click **Insert Graph** to draw the graph. X positions are evenly spaced across
the graph, while each X/Y pair stays in its input order. The lowest Y value is
placed 5 pixels above the X-axis, and higher Y values are scaled proportionally
above it. Y-axis labels are shown from lowest to highest.

## Documentation

- [Requirements](docs/requirements.md)
- [API specification](docs/api_specification.md)
- [Integration plan](docs/integration_plan.md)

## Running Tests

Run the built-in unittest suite with:

```bash
python -m unittest discover -s tests -p "test*.py"
```

If pytest is installed, it can also discover and run the tests with:

```bash
python -m pytest
```


