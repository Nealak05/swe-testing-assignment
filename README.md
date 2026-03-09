# Quick-Calc

Quick-Calc is a simple calculator application built with Python and Tkinter. It supports the four basic arithmetic operations (addition, subtraction, multiplication, and division), includes a clear/reset function, and handles division by zero by showing an error state instead of crashing.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Clear (`C`) to reset the calculator
- Basic decimal input support

## Project Structure

- `quick_calc_gui.py`: Tkinter GUI and `CalculatorCore` input flow logic
- `calculator_logic.py`: core arithmetic functions (`add`, `subtract`, `multiply`, `divide`)
- `tests/test_logic.py`: unit tests for arithmetic functions
- `tests/test_integration.py`: integration tests for calculator input flow

## Setup Instructions

1. Clone the repository.
2. Open a terminal in the project root.
3. (Optional) Create and activate a virtual environment.
4. Install test dependency:

```bash
python -m pip install pytest
```

## Run the Application

```bash
python quick_calc_gui.py
```

## How to Run Tests

Run all tests with one command:

```bash
python -m pytest -q
```

## Testing Framework Research: Pytest vs Unittest

Python has two common testing options: `unittest` and `pytest`. `unittest` is part of the Python standard library, so it requires no external installation and uses a class-based structure similar to JUnit. It is stable, widely known, and a good choice for teams that prefer very explicit setup/teardown patterns. However, test code can become verbose because each test case usually needs a class, and assertion methods are less readable than plain `assert` statements.

`pytest` is an external framework focused on simple and readable tests. It supports plain functions, automatic test discovery, detailed failure messages, and powerful fixtures. For small-to-medium projects, this usually reduces boilerplate and makes tests easier to understand for beginners. Pytest also has strong plugin support, which is useful if the project grows and later needs coverage reporting, parallel test execution, or CI-friendly extensions.

For this project, `pytest` was selected because it provides cleaner syntax and faster development for both unit and integration tests. The assignment requires a clear multi-layered testing strategy, and pytest helps achieve that with minimal setup while keeping test output easy to read during debugging and grading.
