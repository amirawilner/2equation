#שני משואות בשני נעלמים רמה קלה


import sympy as sp
import random
import ast

# Define variables
x, y = sp.symbols('x y')

# Generate coefficients for two linear equations ax + by = e and cx + dy = f
a, b, e = [random.randint(1, 10)-5 for _ in range(3)]
c, d, f = [random.randint(1, 10)-5 for _ in range(3)]

# Generate two equations
eq1 = sp.Eq(a*x + b*y, e)
eq2 = sp.Eq(c*x + d*y, f)

# Solve the system of equations
solution = sp.linsolve((eq1,eq2), (x, y))

if len(solution) == 0:
    print("The system of equations has no solution.")
elif len(solution.free_symbols) > 0:
    print("The system of equations has infinite solutions.")
else:
    print("Solve the following system of equations:")
    print(f"{a}*x + {b}*y = {e}")
    print(f"{c}*x + {d}*y = {f}")

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



