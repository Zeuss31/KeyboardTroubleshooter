# Nova AI Generated Code
# Idea: Matematik problemi çözücü
# Generated: 2025-06-18T20:00:14.380331

Here is a simple Python code that solves math problems. This code uses the `math` module for mathematical operations and the `sympy` library for symbolic math.

**Code:**
```python
import math
from sympy import symbols, Eq, solve

# Define the variables
x = symbols('x')

# Define the math problem
problem = "2x + 5 = 11"

# Solve the problem
eq = Eq(eval(problem.replace('x', str(x))), 11)
solution = solve(eq, x)

# Print the solution
print("The solution is:", solution[0])
```
**Explanation:**

This code defines two variables: `x` and `problem`. The `problem` variable is a string that represents the math problem, which is "2x + 5 = 11".

The code uses the `sympy` library to define the equation using the `Eq` function, and then solves the equation using the `solve` function. The solution is stored in the `solution` variable.

Finally, the code prints the solution using the `print` function.

**How to use:**

To use this code, simply run it and replace the `problem` variable with the math problem you want to solve. For example, if you want to solve the problem "x + 3 = 7", you would replace the `problem` variable with the string "x + 3 = 7".

Note that this