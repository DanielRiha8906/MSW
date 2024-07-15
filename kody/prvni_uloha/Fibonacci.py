import math
import time

# Standardni Python - rekurzivní způsob počítání fibonacciho posloupnosti
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 35  # Pro vyšší hodnoty je standardní Python velmi pomalý

start = time.time()
result = fibonacci(n)
end = time.time()
print("Standard Python:", end - start)


#############

# math

start_time = time.time()
fact = math.factorial(n)
end_time = time.time()

print("Math:", end_time - start_time)

print("Rozdíl Math vs Python: ", (end_time - start_time) - (end - start))