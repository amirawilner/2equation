#שני משואות בשני נעלמים רמה קשה
import sympy as sp
import random
import ast

# Define variables
x, y = sp.symbols('x y')

# Generate coefficients for three types of equations
a, b, c, d, e, f, g, h, i, j, k, l = [random.randint(1, 10)-5 for _ in range(12)]

# Generate three equations in string format to keep brackets
eq1_str = f"({a}*x{'+' if b >= 0 else ''}{b})/{c}{'+' if d >= 0 else ''}{d} = ({e}*y{'+' if f >= 0 else ''}{f})/{g}"
eq2_str = f"({a}*x{'+' if b >= 0 else ''}{b})/{c} = ({e}*y{'+' if f >= 0 else ''}{f})/{g}"
eq3_str = f"({h}*x{'+' if i >= 0 else ''}{i})/{j}{'+' if k >= 0 else ''}({k}*y{'+' if l >= 0 else ''}{l})/{g} = {d}"

# Convert string equations to sympy equations
eq1 = sp.parse_expr(eq1_str.replace("=", "-(")+")")
eq2 = sp.parse_expr(eq2_str.replace("=", "-(")+")")
eq3 = sp.parse_expr(eq3_str.replace("=", "-(")+")")

# Randomly select two equations from the list
eqs_str = [eq1_str, eq2_str, eq3_str]
eqs = [eq1, eq2, eq3]

selected_indices = random.sample(range(3), 2)

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
