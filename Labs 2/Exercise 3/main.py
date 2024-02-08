import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    # Ensure x is a valid value that won't cause errors in the log operations
    if x > 1:
        return np.cos(np.sin(x)/np.cos(x))
    else:
        return None
    
# Generate x and y values, filtering out invalid y values
x = np.linspace(0, 4, 10000)
y = [f(val) for val in x]
x, y = zip(*[(val, f_val) for val, f_val in zip(x, y) if f_val is not None])

plt.plot(x, y)

# Find values of f(x) for specific x values
x_values = [1.56]
for x_value in x_values:
    y_value = f(x_value)
    plt.axvline(x=x_value, color='r', linestyle='--')
    plt.plot(x_value, y_value, 'ro', label=f'f({x_value})={y_value:.2f}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x) = cos(sin(x)/cos(x))')
plt.legend()
plt.grid()

plt.savefig('Labs 2/Exercise 3/f_of_x_cos_sin_x_over_cos_x.png')
plt.show()