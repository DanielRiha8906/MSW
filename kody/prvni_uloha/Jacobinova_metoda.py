

import numpy as np
import time 


# Python
def jacobi_method(A, b, x0, tolerance=1e-10, max_iterations=1000):
    n = len(A)
    x = x0.copy()
    x_new = x0.copy()

    for iteration in range(max_iterations):
        for i in range(n):
            sum_Ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_Ax) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new

        x = x_new.copy()

    raise ValueError("Jacobi method did not converge within the maximum number of iterations")

A = [
    [10, -1,  2, 0, 0],
    [-1, 11, -1, 3, 0],
    [ 2, -1, 10,-1, 0],
    [ 0,  3, -1, 8,-1],
    [ 0,  0,  0,-1, 5]
]
b = [6, 25, -11, 15, 10]
x0 = [0, 0, 0, 0, 0]

start = time.time()
solution = jacobi_method(A, b, x0)
end = time.time()

print("Čistý python")
print("Řešení:")
for i, x_i in enumerate(solution):
    print(f"x{i} = {x_i:.6f}")
print("Rychlost řešení:", end - start)

print("Python s numpy")

##############################################

# Numpy

def jacobi_method(A, b, x0=None, tolerance=1e-10, max_iterations=1000):
    n = len(A)
    if x0 is None:
        x0 = np.zeros(n)
    x = x0.copy()
    x_new = x0.copy()

    for iteration in range(max_iterations):
        for i in range(n):
            sum_Ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_Ax) / A[i][i]
        if np.allclose(x, x_new, atol=tolerance):
            return x_new

        x = x_new.copy()

    raise ValueError("Jacobi method did not converge within the maximum number of iterations")

A = np.array([
    [10, -1,  2, 0, 0],
    [-1, 11, -1, 3, 0],
    [ 2, -1, 10,-1, 0],
    [ 0,  3, -1, 8,-1],
    [ 0,  0,  0,-1, 5]
])
b = np.array([6, 25, -11, 15, 10])
x0 = np.zeros(len(b))

start_time = time.time()
solution = jacobi_method(A, b, x0)
end_time = time.time()

print("Řešení:")
for i, x_i in enumerate(solution):
    print(f"x{i} = {x_i:.6f}")
print("Rychlost řešení:", end_time - start_time)

print("Rozdíl Numpy vs python: ", (end_time - start_time) - (end - start))