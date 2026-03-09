import tkinter as tk

from calculator_logic import add, subtract, multiply, divide


class CalculatorCore:
    def __init__(self):
        self.display = "0"
        self.first_number = None
        self.operator = None
        self.start_new_input = False

    def _format_number(self, value):
        if value == int(value):
            return str(int(value))
        return str(value)

    def _reset(self, display_value="0", start_new_input=False):
        self.display = display_value
        self.first_number = None
        self.operator = None
        self.start_new_input = start_new_input

    def _apply(self, first, second):
        if self.operator == "+":
            return add(first, second)
        if self.operator == "-":
            return subtract(first, second)
        if self.operator == "*":
            return multiply(first, second)
        if self.operator == "/":
            return divide(first, second)
        return second

    def press(self, value):
        if value == "C":
            self._reset("0", False)
            return self.display

        if value in "0123456789.":
            if self.display == "Error" or self.start_new_input:
                self.display = "0." if value == "." else value
                self.start_new_input = False
                return self.display

            if value == ".":
                if "." not in self.display:
                    self.display += "."
                return self.display

            if self.display == "0":
                self.display = value
            else:
                self.display += value
            return self.display

        if self.display == "Error":
            return self.display

        if value in "+-*/":
            self.first_number = float(self.display)
            self.operator = value
            self.start_new_input = True
            return self.display

        if value == "=" and self.operator is not None and self.first_number is not None:
            second_number = float(self.display)
            try:
                result = self._apply(self.first_number, second_number)
                self._reset(self._format_number(result), True)
            except ZeroDivisionError:
                self._reset("Error", True)
            return self.display

        return self.display


def run_app():
    root = tk.Tk()
    root.title("Quick-Calc")
    root.resizable(False, False)

    core = CalculatorCore()

    display = tk.Entry(root, justify="right", font=("Segoe UI", 18), width=16)
    display.insert(0, core.display)
    display.grid(row=0, column=0, columnspan=4, padx=8, pady=(8, 6), sticky="nsew")

    def on_click(value):
        result = core.press(value)
        display.delete(0, tk.END)
        display.insert(0, result)

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["0", ".", "=", "+"],
        ["C"],
    ]

    for row_index, row_values in enumerate(buttons, start=1):
        if row_values == ["C"]:
            button = tk.Button(root, text="C", font=("Segoe UI", 14), command=lambda: on_click("C"))
            button.grid(row=row_index, column=0, columnspan=4, padx=8, pady=(0, 8), sticky="nsew")
            continue

        for col_index, label in enumerate(row_values):
            button = tk.Button(root, text=label, font=("Segoe UI", 14), command=lambda v=label: on_click(v))
            button.grid(row=row_index, column=col_index, padx=4, pady=4, sticky="nsew")

    for i in range(4):
        root.grid_columnconfigure(i, weight=1, minsize=60)
    for i in range(1, 6):
        root.grid_rowconfigure(i, weight=1, minsize=50)

    root.mainloop()


if __name__ == "__main__":
    run_app()
