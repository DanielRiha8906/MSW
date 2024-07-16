import numpy as np
from numpy import cos, sin, log
import matplotlib.pyplot as plt

function_1 = lambda x : x**3 - 2*x**2 + 4*x -2
function_2 = lambda x : -sin(2*x) + cos(2*x) + x
function_3 = lambda x : log(x**3) -1

def closed_method (function, min0, max0, accuracy=0.001):
    repetition = 0
    min, max = min0, max0
    while abs(max-min) > accuracy:
        root = (max+min)/2
        if function(min)*function(max) < 0:
            max = root
        else:
            min = root
        repetition += 1
    print(f"Počet opakování: {repetition}")
    return root
def solution(function, min, max, root, name):
    print(f"Kořen pro funkci je {root}")
    print(f"Funkční hodnota v bodě je {function(root)}")
    
    x_vals = np.linspace(min, max, 100)
    y_vals = function(x_vals)

    plt.plot(x_vals, y_vals, 'r-', label='Function')
    plt.plot(root, function(root), 'bo', label='Root')
    plt.title(name)
    plt.legend()
    plt.grid(True)
    plt.show()
    input("Zmáčkněte prosím enter pro další funkci")

solution(function_1, 0.1, 10, closed_method(function_1, 0.1, 5), "x**3 - 2*x**2 + 4*x -2")
input("Zmáčkněte prosím enter pro další funkci")
solution(function_2, 0.1, 10, closed_method(function_2, 0.1, 5), "-sin(2*x) + cos(2*x) + x")
input("Zmáčkněte prosím enter pro další funkci")
solution(function_3, 0.1, 10, closed_method(function_3, 0.1, 5), "log(x**3) -1")