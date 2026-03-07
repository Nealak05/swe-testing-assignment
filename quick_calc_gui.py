import tkinter as tk

root = tk.Tk()
root.title("Quick-Calc")

display = tk.Entry(
    root,
    justify="right",
    font=("Segoe UI", 18),
    width=16,
)
display.insert(0, "0")
display.grid(row=0, column=0, columnspan=4, padx=8, pady=(8, 6), sticky="nsew")

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

