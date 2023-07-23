#שני משואות בשני נעלמים רמה בינונית

import sympy as sp
import random
import ast

# Define variables
x, y = sp.symbols('x y')

# Generate coefficients for two types of equations
a, b, c, d, e, f, g, h, i = [random.randint(1, 10)-5 for _ in range(9)]

# Generate two equations in string format to keep brackets
eq1_str = f"{a}*(x{'+' if b >= 0 else ''}{b}) + {c}*(y{'+' if d >= 0 else ''}{d}) = {e}"
eq2_str = f"{f}*({g}*x{'+' if h >= 0 else ''}{h}) + {i}*(y{'+' if a >= 0 else ''}{a}) = {b}"

# Convert string equations to sympy equations
eq1 = sp.parse_expr(eq1_str.replace("=", "-(")+")")
eq2 = sp.parse_expr(eq2_str.replace("=", "-(")+")")

# List of equations
eqs = [eq1, eq2]

# Solve the system of equations
solution = sp.linsolve(eqs, (x, y))

if len(solution) == 0:
    print("The system of equations has no solution.")
elif len(solution.free_symbols) > 0:
    print("The system of equations has infinite solutions.")
else:
    print("Solve the following system of equations:")
    print(f"Equation 1: {eq1_str}")
    print(f"Equation 2: {eq2_str}")

    user_solution = ast.literal_eval(input("Enter the solution in the form (x,y): "))

    # Convert solution to list to access elements
    solution_list = list(solution)

    # Convert sympy Floats to Python floats and round to 2 decimal places
    correct_solution = (round(float(solution_list[0][0]), 2), round(float(solution_list[0][1]), 2))

    # Compare the user's solution to the correct solution
    if round(float(solution_list[0][0]), 2) == round(float(user_solution[0]), 2) and round(float(solution_list[0][1]), 2) == round(float(user_solution[1]), 2):
        print("Correct!")
    else:
        print("Incorrect.")
        
    print(f"The correct solution is {correct_solution}")



