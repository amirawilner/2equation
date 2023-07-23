#שני משואות בשני נעלמים רמה קשה

import sympy as sp
import random
import ast

# Define variables
x, y = sp.symbols('x y')

# Generate coefficients for five types of equations
a, b, c, d, e, f, g, h, i, j, k, l, m, n = [random.randint(1, 10)-5 for _ in range(14)]

# Generate five equations in string format to keep brackets
eq1_str = f"({a}*x{'+' if b >= 0 else ''}{b})/x + ({c}*y{'+' if d >= 0 else ''}{d})/y - {e}"
eq2_str = f"{f}*((x{'+' if g >= 0 else ''}{g})/x) + {h}*((y{'+' if i >= 0 else ''}{i})/y) - {j}"
eq3_str = f"(x{'+' if k >= 0 else ''}{k})/{a}*x + (y{'+' if l >= 0 else ''}{l})/{c}*y - {m}"
eq4_str = f"({a}*x{'+' if b >= 0 else ''}{b})/x - ({c}*y{'+' if d >= 0 else ''}{d})/y"
eq5_str = f"({f}*x{'+' if g >= 0 else ''}{g})/x{'+' if h >= 0 else ''}{h} - ({i}*y{'+' if j >= 0 else ''}{j})/y"

# Convert string equations to sympy equations
eq1 = sp.sympify(eq1_str)
eq2 = sp.sympify(eq2_str)
eq3 = sp.sympify(eq3_str)
eq4 = sp.sympify(eq4_str)
eq5 = sp.sympify(eq5_str)

# Randomly select two equations from the list
eqs_str = [eq1_str, eq2_str, eq3_str, eq4_str, eq5_str]
eqs = [eq1, eq2, eq3, eq4, eq5]

selected_indices = random.sample(range(5), 2)

# Solve the system of equations
solution = sp.solve([eqs[i] for i in selected_indices], (x, y))

print("Solve the following system of equations:")
print(f"Equation 1: {eqs_str[selected_indices[0]]} = 0")
print(f"Equation 2: {eqs_str[selected_indices[1]]} = 0")

if solution == []:
    print("The system of equations has no solution.")
elif len(solution) > 1:
    print("The system of equations has multiple solutions:")
    for idx, sol in enumerate(solution):
        correct_solution = (round(float(sol[x]), 2), round(float(sol[y]), 2))
        print(f"Solution {idx+1}: {correct_solution}")
else:
    user_solution = ast.literal_eval(input("Enter the solution in the form (x, y): "))

    # Convert sympy Floats to Python floats and round to 2 decimal places
    correct_solution = (round(float(solution[x]), 2), round(float(solution[y]), 2))

    # Compare the user's solution to the correct solution
    if round(float(solution[x]), 2) == round(float(user_solution[0]), 2) and round(float(solution[y]), 2) == round(float(user_solution[1]), 2):
        print("Correct!")
    else:
        print("Incorrect.")
        
    print(f"The correct solution is {correct_solution}")






