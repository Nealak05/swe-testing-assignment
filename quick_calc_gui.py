import tkinter as tk

root = tk.Tk()
root.title("Quick-Calc")
root.resizable(False, False)

display = tk.Entry(
    root,
    justify="right",
    font=("Segoe UI", 18),
    width=16,
)
display.insert(0, "0")
display.grid(row=0, column=0, columnspan=4, padx=8, pady=(8, 6), sticky="nsew")

first_number = None
operator = None
start_new_input = False


def set_display(value):
    display.delete(0, tk.END)
    display.insert(0, value)


def format_number(value):
    if value == int(value):
        return str(int(value))
    return str(value)


def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError
        return a / b
    return b


def handle_button_click(value):
    global first_number, operator, start_new_input

    if value == "C":
        first_number = None
        operator = None
        start_new_input = False
        set_display("0")
        return

    current_text = display.get()

    if value in "0123456789.":
        if current_text == "Error" or start_new_input:
            if value == ".":
                set_display("0.")
            else:
                set_display(value)
            start_new_input = False
            return

        if value == ".":
            if "." not in current_text:
                set_display(current_text + ".")
            return

        if current_text == "0":
            set_display(value)
        else:
            set_display(current_text + value)
        return

    if current_text == "Error":
        return

    if value in "+-*/":
        first_number = float(display.get())
        operator = value
        start_new_input = True
        return

    if value == "=" and operator is not None and first_number is not None:
        second_number = float(display.get())
        try:
            result = calculate(first_number, second_number, operator)
            set_display(format_number(result))
            first_number = None
            operator = None
            start_new_input = True
        except ZeroDivisionError:
            set_display("Error")
            first_number = None
            operator = None
            start_new_input = True

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"],
]

for row_index, row_values in enumerate(buttons, start=1):
    if row_values == ["C"]:
        button = tk.Button(
            root,
            text="C",
            font=("Segoe UI", 14),
            command=lambda: handle_button_click("C"),
        )
        button.grid(
            row=row_index,
            column=0,
            columnspan=4,
            padx=8,
            pady=(0, 8),
            sticky="nsew",
        )
        continue

    for col_index, label in enumerate(row_values):
        button = tk.Button(
            root,
            text=label,
            font=("Segoe UI", 14),
            command=lambda v=label: handle_button_click(v),
        )
        button.grid(
            row=row_index,
            column=col_index,
            padx=4,
            pady=4,
            sticky="nsew",
        )

for i in range(4):
    root.grid_columnconfigure(i, weight=1, minsize=60)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1, minsize=50)

root.mainloop()
