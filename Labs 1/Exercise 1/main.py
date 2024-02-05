import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

"""
Solve a system of linear equations graphically:
    2x+2y=1
    3x-2y=0
"""

# Numerical solution finder function (data1 and data2 are x, y values for the two equations)
def find_solution(data1, data2, threshold=0.1):
    def distance(x1, y1, x2, y2):
        return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    closest = { # Closest solutions in the form (x, y)
                "position": (0, 0),
                "distance": 1000
                } 
    
    # Find all solutions within the threshold
    for i in range(len(data1)):
        for j in range(len(data2)):
            temp_distance = distance(data1[i][0], data1[i][1], data2[j][0], data2[j][1])
            if temp_distance < threshold and temp_distance < closest["distance"]:
                closest["position"] = (data1[i][0], data1[i][1])
                closest["distance"] = distance(data1[i][0], data1[i][1], data2[j][0], data2[j][1])
    
    return closest["position"]



# Define the equations (in sympy)
x, y = sp.symbols('x y')
equation1 = sp.Eq(2*x + 2*y, 1)
equation2 = sp.Eq(3*x - 2*y, 0)

# Rearrange the equations for y
y1 = sp.solve(equation1, y)
y2 = sp.solve(equation2, y)
print(y1, y2)

# Solve the equations
solution = sp.solve((equation1, equation2), (x, y))
print(solution)

# Generate x values
x_values = np.linspace(-10, 10, 1000)

# Generate y values with the functions y1 and y2
y1_values = sp.lambdify(x, y1[0])(x_values)
y2_values = sp.lambdify(x, y2[0])(x_values)

# Plot the equations
plt.plot(x_values, y1_values, label='Equation 1: 2x+2y=1')
plt.plot(x_values, y2_values, label='Equation 2: 3x-2y=0')

# Plot the solution (from direct solution)
solution_text = f'Direct solution: ({solution[x]}, {solution[y]})'
plt.plot(solution[x], solution[y], 'ro', label=solution_text)

# Plot the solution (from numerical solution finder)
data1 = np.array([x_values, y1_values]).T
data2 = np.array([x_values, y2_values]).T
solution = find_solution(data1, data2)
solution_text = f'Numerical solution: ({round(solution[0], 3)}, {round(solution[1], 3)}) 3s.f.'
plt.plot(solution[0], solution[1], 'bo', label=solution_text, markersize=4)

# Add labels and legend
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='lower left')

plt.title('Graphical solution of a system of linear equations')

# Show the plot
plt.show()
