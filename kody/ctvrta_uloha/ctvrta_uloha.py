import numpy as np
import random
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

function_1 = lambda x: x**3 - 2*x**2 + 4*x - 2
function_2 = lambda x: -np.sin(2*x) + np.cos(2*x) + x
function_3 = lambda x: np.log(x**3) - 1

original_functions = [function_1, function_2, function_3]
point_list = [[], [], []]

for i in range(1, 101):
    oscillation = lambda: random.uniform(-0.2, 0.2)
    point_list[0].append(function_1(i) + oscillation())
    point_list[1].append(function_2(i) + oscillation())
    point_list[2].append(function_3(i) + oscillation())

x_points = np.arange(1, 101)
x_new = np.linspace(1, 100, 400)

cubic = [[], [], []]
linear = [[], [], []]
nearest = [[], [], []]

for i in range(3):
    interp_func_1 = interp1d(x_points, point_list[i], kind='cubic')
    interp_func_2 = interp1d(x_points, point_list[i], kind='linear')
    interp_func_3 = interp1d(x_points, point_list[i], kind='nearest')    
    cubic[i] = interp_func_1(x_new)
    linear[i] = interp_func_2(x_new)
    nearest[i] = interp_func_3(x_new)

def mse(true_values, interpolated_values):
    return np.mean((true_values - interpolated_values)**2)

true_values = [[], [], []]
for i in range(3):
    true_values[i] = original_functions[i](x_new)

mse_cubic = [mse(true_values[i], cubic[i]) for i in range(3)]
mse_linear = [mse(true_values[i], linear[i]) for i in range(3)]
mse_nearest = [mse(true_values[i], nearest[i]) for i in range(3)]

for i in range(3):
    print(f"Function {i+1} MSE:")
    print(f"  Cubic: {mse_cubic[i]}")
    print(f"  Linear: {mse_linear[i]}")
    print(f"  Nearest: {mse_nearest[i]}")
    print()

plt.figure(figsize=(14, 16))

interpolation_methods = ['Cubic', 'Linear', 'Nearest']
interpolated_points = [cubic, linear, nearest]

for i in range(3):
    for j in range(3):
        plt.subplot(3, 3, 3*i + j + 1)
        plt.plot(x_points, point_list[i], 'o', label=f'Function {i+1} Data Points')
        plt.plot(x_new, interpolated_points[j][i], '-', label=f'Function {i+1} {interpolation_methods[j]} Interpolation')
        plt.title(f'Function {i+1} - {interpolation_methods[j]}')
        plt.legend()

plt.tight_layout()
plt.show()
