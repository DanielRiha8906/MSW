import numpy as np
import random
import math
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

function_1 = lambda x: x**3 - 2*x**2 + 4*x - 2
function_2 = lambda x: -np.sin(2*x) + np.cos(2*x) + x
function_3 = lambda x: np.log(x**3) - 1

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

plt.figure(figsize=(14, 16))

functions = ['Cubic', 'Linear', 'Nearest']
interpolated_points = [cubic, linear, nearest]

for i in range(3):
    for j in range(3):
        plt.subplot(3, 3, 3*i + j + 1)
        plt.plot(x_points, point_list[i], 'o', label=f'Function {i+1} Data Points')
        plt.plot(x_new, interpolated_points[j][i], '-', label=f'Function {i+1} {functions[j]} Interpolation')
        plt.title(f'Function {i+1} - {functions[j]}')
        plt.legend()

plt.tight_layout()
plt.show()
