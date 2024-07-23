import numpy as np
from numpy import cos, sin, log
import matplotlib.pyplot as plt
from scipy.misc import derivative

function_1 = lambda x : x**3 - 2*x**2 + 4*x -2
function_2 = lambda x : -sin(2*x) + cos(2*x) + x
function_3 = lambda x : log(x**3) -1


def open_method(function, point, accuracy=0.00001):
    repetitions = 0
    while abs(function(point)) > accuracy:
        root = point - (function(point) / derivative(function, point))
        point = root
        repetitions += 1
    root = point
    print(f"Počet opakování: {repetitions}")
    return root


def solution(function, min, max, root, name):
    print(f"Kořen pro funkci je {root}")
    print(f"Funkční hodnota v tomto bodě je {function(root)}")
    plt.plot(np.linspace(min, max), function(np.linspace(min, max)), "r")
    plt.plot(root, function(root), "bo")
    plt.title(name)
    plt.show()


solution(function_1, 0.1, 10, open_method(function_1, 2), "x**3 - 2*x**2 + 4*x -2")
solution(function_2, 0.1, 10, open_method(function_2, 0.1), "-sin(2*x) + cos(2*x) + x")
solution(function_3, 0.1, 10, open_method(function_3, 2), "log(x**3) -1")