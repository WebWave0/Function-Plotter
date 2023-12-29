Function Plotter
Overview
The Function Plotter is a Python script that provides a graphical user interface (GUI) for plotting mathematical functions and equations. It allows users to input algebraic expressions, evaluate them, and visualize the corresponding graphs.

Features
Equation Input: Users can input mathematical equations in a dedicated entry field. Common functions such as sin(x), cos(x), and x^2 are supported, along with standard arithmetic operators.

Graph Plotting: The script generates interactive plots of entered equations, allowing users to visualize the behavior of multiple functions simultaneously.

Calculator Integration: The script includes a calculator feature, accessible through a separate window. This calculator allows users to build mathematical expressions interactively, including operations like addition, subtraction, multiplication, division, square root, and squaring.

Clipboard Support: Users can paste mathematical expressions directly from the clipboard into the equation entry fields.

Log Display: The script provides a scrollable text area for displaying a log of actions, including equation additions, graph plotting, and solutions.

Usage
Equation Input:

Enter mathematical equations into the dedicated entry field.
Click the "Add Equation" button to add equations to the plotting list.
Graph Plotting:

Click the "Plot Graph" button to generate a plot of the entered equations.
The resulting graph will be displayed with labeled curves for each equation.
Calculator:

Click the "Calculator" button to open the calculator window.
Use the calculator to build mathematical expressions.
Click the "Done" button to transfer the expression to the main equation entry field.
Clipboard Support:

In the calculator window, use the "Paste" button to insert the content of the clipboard into the calculator's entry field.
Log Display:

The log area provides information about the actions performed, including equation additions, graph plotting, and solutions.
Requirements
Python 3.x
Required Python packages: tkinter, matplotlib, numpy, simpleeval, pyperclip
How to Run
Install the required Python packages using the following command:

pip install tkinter matplotlib numpy simpleeval pyperclip
Run the script using Python:

python function_plotter.py
The GUI window will appear, allowing users to interact with the Function Plotter.