#שני משואת בשני נעלמים רמה בינונית

import sympy as sp
import random
import ast

# Define variables
x, y = sp.symbols('x y')

# Generate coefficients for four types of equations
a, b, c, d, e, f, g, h, i, j, k, l = [random.randint(1, 10)-5 for _ in range(12)]

# Generate four equations in string format to keep brackets
eq1_str = f"{a}*(x{'+' if b >= 0 else ''}{b}) = {c}*(y{'+' if d >= 0 else ''}{d}){'+' if e >= 0 else ''}{e}"
eq2_str = f"{a}*({b}*x{'+' if c >= 0 else ''}{c}) + {d} = (y{'+' if f >= 0 else ''}{f})"
eq3_str = f"{g}*(x{'+' if h >= 0 else ''}{h}) + {i}*(y{'+' if j >= 0 else ''}{j}) = {k}"
eq4_str = f"{g}*({h}*x{'+' if i >= 0 else ''}{i}) + {j}*(y{'+' if k >= 0 else ''}{k}) = {l}"

# Convert string equations to sympy equations
eq1 = sp.parse_expr(eq1_str.replace("=", "-(")+")")
eq2 = sp.parse_expr(eq2_str.replace("=", "-(")+")")
eq3 = sp.parse_expr(eq3_str.replace("=", "-(")+")")
eq4 = sp.parse_expr(eq4_str.replace("=", "-(")+")")

# Randomly select two equations from the list
eqs_str = [eq1_str, eq2_str, eq3_str, eq4_str]
eqs = [eq1, eq2, eq3, eq4]

selected_indices = random.sample(range(4), 2)

# Solve the system of equations
solution = sp.linsolve([eqs[i] for i in selected_indices], (x, y))

if len(solution) == 0:
    print("The system of equations has no solution.")
elif len(solution.free_symbols) > 0:
    print("The system of equations has infinite solutions.")
else:
    print("Solve the following system of equations:")
    print(f" {eqs_str[selected_indices[0]]}")
    print(f" {eqs_str[selected_indices[1]]}")

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
