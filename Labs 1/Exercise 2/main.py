import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

"""
Solve these systems of nonlinear equations graphically:
    A) x+y=1
       y=x^2
    B) x^2+y^2=9
       y=x^2+3x+1
    C) y=log_2(x+4)
       y=3-x
"""

# Initial the equations
x, y = sp.symbols('x y')

class System:
    def __init__(self, equations):
        self.equations = equations
        print('self.equations:', self.equations)
        self.y_solutions = [sp.solve(equation, y, dict=True) for equation in equations]
        print('self.y_solutions:', self.y_solutions)
        self.solutions = sp.solve(equations, x, y, dict=True)
        print('self.solutions:', self.solutions)
        

systems = [
    System([sp.Eq(x + y, 1), sp.Eq(y, x**2)]),
    System([sp.Eq(x**2 + y**2, 9), sp.Eq(y, x**2 + 3*x + 1)]),
    System([sp.Eq(y, sp.log(x + 4, 2)), sp.Eq(y, 3 - x)])
]

"""for system in systems:
    print(system.solutions)"""

# Generate x values
x_values = np.linspace(-5, 5, 100)

# Set up the plot (2x2 grid)
fig, axs = plt.subplots(1, 3, figsize=(10, 5))
axs_flat = axs.flatten()
line_colours = ['orange', 'cornflowerblue']

# Plot the equations
for i in range(len(systems)):
    system = systems[i]
    axs_flat[i].set_title(f'System {chr(65 + i)}')
    
    
    # Generate y values for each y_solution
    for j, y_solution in enumerate(system.y_solutions):
        for k in range(len(y_solution)):
            y_values = sp.lambdify(x, y_solution[k][y])(x_values)
            axs_flat[i].plot(x_values, y_values, label=f'y={y_solution[k][y]}', color=line_colours[j])
            
    # Plot the solutions
    solution_counter = 1
    for solution in system.solutions:
        try:
            if len(system.solutions) == 1:
                to_label = f'Solution: ({solution[x]}, {solution[y]})'
                axs_flat[i].plot(solution[x], solution[y], 'ro', label=to_label)
            else:
                to_label = f'Solution {solution_counter}: ({solution[x].evalf()}, {solution[y].evalf()})'
                axs_flat[i].plot(solution[x], solution[y], 'ro', label=to_label)
                axs_flat[i].text(solution[x], solution[y], f'{solution_counter}', fontsize=12, color='black')
                solution_counter += 1
        except TypeError:
            pass
        
    axs_flat[i].legend(loc='upper left')
        
            
plt.show()
