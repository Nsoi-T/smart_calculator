# Integration Plan

This project is a smart calculator app made of four modules:

- Module A: basic arithmetic
- Module B: advanced math
- Module C: statistics
- Module D: graph drawing

The app connects these modules through the main entry file in `src/main.py` and the tests confirm that the modules work together correctly.

## 1. Project integration structure

The main application uses a central registry in `src/main.py`:

- `MODULE_OPERATIONS` stores each operation for each module
- `CALCULATORS` links each module name to its calculator class
- `MODULE_INPUTS` defines how each module receives inputs
- `calculate()` handles normal calculation requests
- `draw_graph()` handles graph requests
- `run()` manages the GUI event loop

This means the UI, calculator logic, and graph logic are connected through one central place instead of being completely separate.

## 2. How modules work together

When the user selects a module:

1. The app changes the visible inputs and operations.
2. The correct calculator class is selected from `CALCULATORS`.
3. The user enters values.
4. The app calls the matching method from the selected module.
5. The result is shown in the GUI and saved in history.

For Module D, the app does a special graph action:

- it parses X and Y values
- sends them to the graph calculator
- draws the graph inside the window

## 3. Testing flow in this project

The project uses `unittest`.

### Unit tests

The unit tests are in `tests/unit/` and check each module individually:

- `test_module_a.py` checks arithmetic functions
- `test_module_b.py` checks advanced math functions
- `test_module_c.py` checks statistics functions
- `test_module_d.py` checks graph drawing behavior

### Integration tests

The main integration test is in `tests/integration/test_integration.py`.

It checks that:

- all modules are registered correctly
- Module A, B, C, and D are all connected to the main app
- each module calculation returns the expected output
- graph drawing works through the main integration layer
- operation lists are present for each module

## 4. How to run tests

Use this command from the project root:

```bash
python -m unittest discover -s tests -p "test*.py"
```

This project is already set up to run the full test suite successfully.

## 5. Simple integration plan

For future updates, the team should follow this simple process:

1. Add or update unit tests for each module.
2. Check that the module still works by itself.
3. Run the integration test to confirm the app still connects all modules correctly.
4. Validate GUI behavior for input, result display, and error handling.
5. If a module is added, register it in the main app and test it in the integration suite.

## 6. Current status

The current test suite passes successfully:

- 29 tests run
- all tests passed
- status: OK

This confirms that the calculator modules and the main application integration are currently working together as expected.
