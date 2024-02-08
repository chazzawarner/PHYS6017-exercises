import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Define the function
def f(x, n):
    n = int(n)
    return np.sum([(1/((2 * i) + 1)**2) * np.cos(((2 * i) - 1) * x) for i in range(n)])

# Generate x and y values
x = np.linspace(0, 4*np.pi, 10000)
n_values = np.linspace(1, 10, 5)
y_values = []
for n in n_values:
    y_values.append([f(val, n) for val in x])

# Define colours to lerp between
color1 = 'red'
color2 = 'lime'
colors = [color1, color2]
cmap = LinearSegmentedColormap.from_list('my_cmap', colors)

# Plot the function
for i, y in enumerate(y_values):
    # Select a color from the colormap based on n
    color = cmap(i / (len(y_values)-1))
    
    plt.plot(x, y, color=color)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'$f(x) = \sum \left(\frac{1}{(2i+1)^2} \cdot \cos((2i-1)x)\right)$')
plt.grid()

plt.savefig('Labs 2/Exercise 4/f_of_x_sum_1_over_2i_plus_1_squared_times_cos_2i_minus_1_x.png')
plt.show()