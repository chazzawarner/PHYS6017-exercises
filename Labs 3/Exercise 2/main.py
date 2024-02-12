import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return (0.001 * x**2) + (1000 * x) - (0.001)

# Setup plots
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

# GRAPHICAL GUESS PLOT
# Plot the function for the graphical guess
x = np.linspace(-1e10, 1e10, 1000)
y = f(x)
axs[0].plot(x, y)

# Plot graphical guess of roots
axs[0].plot(0, 0, 'ro', label="A) Root guess at (0,0)") # root at x = 0

# Add labels and title
axs[0].set_xlabel('x')
axs[0].set_ylabel('f(x)')
axs[0].grid()
axs[0].legend()
axs[0].set_title("A) Graphical root guess")

# QUADRATIC FORMULA PLOT
# Find the roots using the quadratic formula
def quadratic_formula(a, b, c):
    x1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

x1, x2 = quadratic_formula(0.001, 1000, -0.001)

# Plot the roots from the quadratic formula
axs[1].plot(x1, 0, 'bo', label=f"Root guess using b+ at ({x1}, 0)")
axs[1].plot(x2, 0, 'go', label=f"Root guess using b- at ({x2}, 0)")

# Plot the function
plot_limits = [np.average([x1, x2]) - abs(x1 - x2), np.average([x1, x2]) + abs(x1 - x2)]
x = np.linspace(plot_limits[0], plot_limits[1], 1000)
y = f(x)
axs[1].plot(x, y)

# Add labels and title
axs[1].set_xlabel('x')
axs[1].set_ylabel('f(x)')
axs[1].grid()
axs[1].legend()
axs[1].set_title("B) Quadratic formula root guess")

# ALTERED QUADRATIC FORMULA PLOT
# Find the roots using the altered quadratic formula
def alt_quadratic_formula(a, b, c):
    x1 = (-2*c) / (b + np.sqrt(b**2 - 4*a*c))
    x2 = (-2*c) / (b - np.sqrt(b**2 - 4*a*c))
    return x1, x2

x1, x2 = alt_quadratic_formula(0.001, 1000, -0.001)

# Plot the roots from the altered quadratic formula
axs[2].plot(x1, 0, 'bo', label=f"Root guess using b+ at ({x1}, 0)")
axs[2].plot(x2, 0, 'go', label=f"Root guess using b- at ({x2}, 0)")

# Plot the function
plot_limits = [np.average([x1, x2]) - abs(x1 - x2), np.average([x1, x2]) + abs(x1 - x2)]
x = np.linspace(plot_limits[0], plot_limits[1], 1000)
y = f(x)
axs[2].plot(x, y)

# Add labels and title
axs[2].set_xlabel('x')
axs[2].set_ylabel('f(x)')
axs[2].grid()
axs[2].legend()
axs[2].set_title("C) Altered quadratic formula root guess")

plt.tight_layout()
plt.savefig("Labs 3/Exercise 2/quadratic_roots.png")
plt.show()
