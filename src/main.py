import PySimpleGUI as sg

from module_a.calculator_basic import BasicCalculator
from module_b.calculator_advanced import AdvancedCalculator
from module_c.calculator_stats import StatisticalCalculator


MODULE_OPERATIONS = {
    "Module A": {
        "Add (+)": ("add", "+", "binary"),
        "Subtract (-)": ("subtract", "-", "binary"),
        "Multiply (*)": ("multiply", "*", "binary"),
        "Divide (/)": ("divide", "/", "binary"),
        "Power (^)": ("power", "^", "binary"),
        "Modulus (%)": ("modulus", "%", "binary"),
    },
    "Module B": {
        "Square root": ("square_root", "sqrt", "single"),
        "Logarithm": ("logarithm", "log", "single"),
        "Sine": ("sine", "sin", "single"),
        "Cosine": ("cosine", "cos", "single"),
        "Tangent": ("tangent", "tan", "single"),
        "Factorial": ("factorial", "factorial", "single"),
        "Absolute": ("absolute", "abs", "single"),
    },
    "Module C": {
        "Sum": ("sum_data", "sum", "list"),
        "Mean": ("mean", "mean", "list"),
        "Median": ("median", "median", "list"),
        "Mode": ("mode", "mode", "list"),
        "Variance": ("variance", "variance", "list"),
        "Standard deviation": ("standard_deviation", "std dev", "list"),
        "Maximum": ("max_value", "max", "list"),
        "Minimum": ("min_value", "min", "list"),
    },
}

CALCULATORS = {
    "Module A": BasicCalculator,
    "Module B": AdvancedCalculator,
    "Module C": StatisticalCalculator,
}

MODULE_BUTTONS = {
    "-MODULE-A-": "Module A",
    "-MODULE-B-": "Module B",
    "-MODULE-C-": "Module C",
}

MODULE_TITLES = {
    "Module A": "Module A - Basic Calculator",
    "Module B": "Module B - Advanced Calculator",
    "Module C": "Module C - Statistical Calculator",
}

MODULE_INPUTS = {
    "Module A": ("First number", "Second number", True),
    "Module B": ("Number", "Second number", False),
    "Module C": ("Numbers\n(comma-separated)", "Second number", False),
}


def _parse_number(value):
    """Convert an input string to an int when possible, otherwise a float."""
    number = float(value.strip())
    return int(number) if number.is_integer() else number


def _parse_numbers(value):
    return [_parse_number(item) for item in value.split(",") if item.strip()]


def create_window():
    """Create the calculator window without starting its event loop."""
    sg.theme("LightBlue3")
    layout = [
        [sg.Text(MODULE_TITLES["Module A"], key="-TITLE-",
                 font=("Any", 16, "bold"))],
        [sg.Text("Module", size=(14, 1)),
         sg.Button("Module A", key="-MODULE-A-"),
         sg.Button("Module B", key="-MODULE-B-"),
         sg.Button("Module C", key="-MODULE-C-")],
        [sg.Text("Input", size=(14, 2), key="-FIRST-LABEL-"),
         sg.Input(key="-FIRST-", expand_x=True)],
        [sg.Text("Operation", size=(14, 1)), sg.Combo(
            list(MODULE_OPERATIONS["Module A"]), default_value="Add (+)",
            readonly=True, key="-OPERATION-", expand_x=True)],
        [sg.Text("Second number", size=(14, 1), key="-SECOND-LABEL-"),
         sg.Input(key="-SECOND-", expand_x=True)],
        [sg.Button("Calculate", bind_return_key=True),
         sg.Button("Clear"), sg.Button("Exit")],
        [sg.HorizontalSeparator()],
        [sg.Text("Result", size=(14, 1)), sg.Text(
            "", key="-RESULT-", expand_x=True)],
        [sg.Text("History", size=(14, 1)), sg.Button("Clear History")],
        [sg.Listbox([], size=(44, 6), key="-HISTORY-", expand_x=True)],
    ]
    return sg.Window("Smart Calculator", layout, finalize=True, resizable=True)


def _select_module(window, module_name):
    """Update the GUI controls for the selected module."""
    first_label, second_label, show_second = MODULE_INPUTS[module_name]
    operations = list(MODULE_OPERATIONS[module_name])
    window["-TITLE-"].update(MODULE_TITLES[module_name])
    window["-OPERATION-"].update(values=operations, value=operations[0])
    window["-FIRST-LABEL-"].update(first_label)
    window["-SECOND-LABEL-"].update(second_label, visible=show_second)
    window["-SECOND-"].update(visible=show_second, value="")
    window["-FIRST-"].update("")
    window["-RESULT-"].update("")


def calculate(values, calculator, module_name):
    """Calculate one operation and return its display text."""
    operation = MODULE_OPERATIONS[module_name][values["-OPERATION-"]]
    method_name, symbol, input_type = operation

    if input_type == "list":
        numbers = _parse_numbers(values["-FIRST-"])
        result = getattr(calculator, method_name)(numbers)
        return f"{numbers} {symbol} = {result}"

    first = _parse_number(values["-FIRST-"])
    if input_type == "single":
        result = getattr(calculator, method_name)(first)
        return f"{symbol}({first}) = {result}"

    second = _parse_number(values["-SECOND-"])
    result = getattr(calculator, method_name)(first, second)
    return f"{first} {symbol} {second} = {result}"


def run():
    """Run the calculator GUI until the user closes it."""
    module_name = "Module A"
    calculator = CALCULATORS[module_name]()
    history = []
    window = create_window()

    try:
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Exit"):
                break
            if event in MODULE_BUTTONS:
                module_name = MODULE_BUTTONS[event]
                calculator = CALCULATORS[module_name]()
                _select_module(window, module_name)
                continue
            if event == "Clear":
                window["-FIRST-"].update("")
                window["-SECOND-"].update("")
                window["-RESULT-"].update("")
                continue
            if event == "Clear History":
                history.clear()
                window["-HISTORY-"].update(history)
                continue
            if event != "Calculate":
                continue

            try:
                expression = calculate(values, calculator, module_name)
            except (KeyError, TypeError, ValueError):
                window["-RESULT-"].update(
                    "Please enter number to do operation", text_color="red")
                continue

            history.insert(0, expression)
            window["-RESULT-"].update(expression, text_color="black")
            window["-HISTORY-"].update(history)
    finally:
        window.close()


if __name__ == "__main__":
    run()
