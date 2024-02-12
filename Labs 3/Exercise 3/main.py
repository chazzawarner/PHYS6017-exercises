import numpy as np
from matplotlib import pyplot as plt

# Define recurrance relation
def recurr(x_0, x_1, iters):
    def x_n_plus_1(x_n, x_n_minus_1):
        return ((13/3) * x_n) - ((4/3) * x_n_minus_1)
    
    Y = [x_0, x_1]
    
    while len(Y) < iters:
        Y.append(x_n_plus_1(Y[-1], Y[-2]))
    
    return Y

iters = 50 # Find first 50 values
Y = np.array(recurr(1, 1/3, iters)) # x_0 = 1, x_1 = 1/3

#print(result)
#print(len(result))

# Define evaluated function
def eval_recurr(n):
    return 3**(-n)

# Find x_n for each iteration
Y_dash = np.array([eval_recurr(n) for n in range(1, iters+1)])

#print(results_eval)
#print(len(results_eval))

x = np.linspace(0, iters, iters)
plt.plot(x, (Y - Y_dash))
plt.yscale('log')
plt.xscale('log')
plt.show()


