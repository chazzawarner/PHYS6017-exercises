import numpy as np
from matplotlib import pyplot as plt

# Define the function
def f(x, n):
    n = int(n)
    #return np.sum([(1/((2 * i) + 1)**2) * np.cos(((2 * i) - 1) * x) for i in range(n)])
    return np.array([np.sum([(1/((2 * i) + 1)**2) * np.cos(((2 * i) - 1) * x_val) for i in range(n)]) for x_val in x])

# Define residuals function
def R(x, n):
    residuals = np.zeros(len(x))
    for j in range(1, n+1):
        residuals += f(x, j + 1) - f(x, j)
    return np.array(residuals)

# Generate x and y values
x = np.linspace(0, 4*np.pi, 10000)
n_value = 25
y = R(x, n_value)

# Plot the residuals
plt.plot(x, y)

plt.xlabel('x')
plt.ylabel('R(x)')
plt.title(r'$R(x) = f(x, n+1) - f(x, n)$')
plt.grid()

#plt.savefig('Labs 2/Exercise 4/residuals_of_f_of_x_sum_1_over_2i_plus_1_squared_times_cos_2i_minus_1_x.png')
plt.show()