import tkinter as tk
from tkinter import ttk, scrolledtext
import matplotlib.pyplot as plt
import numpy as np
from simpleeval import simple_eval
import pyperclip

class GraphPlotter:
    def __init__(self, master):
        self.master = master
        master.title("Function Plotter")

        self.equations = []
        self.calculator_formula = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.equation_entry = tk.Entry(self.master, width=30)
        self.equation_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Add Equation", command=self.add_equation)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.calculator_button = tk.Button(self.master, text="Calculator", command=self.open_calculator)
        self.calculator_button.grid(row=0, column=2, padx=10, pady=10)

        self.log_text = scrolledtext.ScrolledText(self.master, width=40, height=10, wrap=tk.WORD)
        self.log_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.plot_button = tk.Button(self.master, text="Plot Graph", command=self.plot_graph)
        self.plot_button.grid(row=2, column=0, columnspan=3, pady=10)

        hint_label = tk.Label(self.master, text="Supported formulas: sin(x), cos(x), x**2, exp(x), 1/x, sqrt(x), etc.")
        hint_label.grid(row=3, column=0, columnspan=3, pady=5)

    def add_equation(self):
        equation = self.equation_entry.get()
        self.equations.append(equation)
        self.log_text.insert(tk.END, f"Equation added: {equation}\n")
        self.equation_entry.delete(0, tk.END)

    def evaluate_equation(self, equation, x):
        try:
            result = simple_eval(equation, names={'x': x})
            return result
        except:
            return float('nan')

    def plot_graph(self):
        x_values = np.linspace(-50, 50, 200)
        y_values = []

        for x in x_values:
            y = []
            for equation in self.equations:
                y.append(self.evaluate_equation(equation, x))
            y_values.append(y)

        plt.figure(figsize=(10, 6))
        for i in range(len(self.equations)):
            plt.plot(x_values, [y[i] for y in y_values], label=self.equations[i])

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of Equations')
        plt.legend()
        plt.grid(True)
        plt.show()

        self.log_text.insert(tk.END, "\nGraph Plotted:\n")
        for i, equation in enumerate(self.equations):
            self.log_text.insert(tk.END, f"Equation {i + 1}: {equation}\n")

        self.log_text.insert(tk.END, "\nSolutions:\n")
        for x in x_values:
            self.log_text.insert(tk.END, f"x = {x:.2f}: ")
            for i, equation in enumerate(self.equations):
                solution = self.evaluate_equation(equation, x)
                self.log_text.insert(tk.END, f"{equation} = {solution:.2f}, ")
            self.log_text.insert(tk.END, "\n")

    def open_calculator(self):
        calculator_window = tk.Toplevel(self.master)
        calculator_window.title("Calculator")

        formula_entry = tk.Entry(calculator_window, width=30, textvariable=self.calculator_formula)
        formula_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+',
            'x^2', '1/x', '='
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            if button == 'Paste':
                ttk.Button(calculator_window, text=button, command=lambda: self.paste_from_clipboard(formula_entry)).grid(row=row_val, column=col_val, padx=5, pady=5)
            else:
                ttk.Button(calculator_window, text=button, command=lambda b=button: self.update_formula(formula_entry, b)).grid(row=row_val, column=col_val, padx=5, pady=5)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        ttk.Button(calculator_window, text="Done", command=lambda: self.transfer_formula(formula_entry)).grid(row=row_val, column=col_val, padx=5, pady=5)

    def update_formula(self, entry, value):
        current_formula = entry.get()

        if value == 'x^2':
            entry.insert(tk.END, '**2')
        elif value == '1/x':
            entry.insert(tk.END, '1/')
        elif value == 'Paste':
            entry.insert(tk.END, pyperclip.paste())
        else:
            entry.insert(tk.END, str(value))

    def transfer_formula(self, entry):
        formula = entry.get()
        self.equation_entry.insert(tk.END, formula)
        entry.delete(0, tk.END)

    def paste_from_clipboard(self, entry):
        entry.delete(0, tk.END)
        entry.insert(0, pyperclip.paste())

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphPlotter(root)
    root.mainloop()
