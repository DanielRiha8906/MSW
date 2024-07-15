from math import factorial
import time
# python

start = time.time()
n = 453
result = 1

for i in range(1, n+1):
    result = result * i 
end = time.time()
result = str(result)

print(f"Vysledek python: {result[:10]}" )
print(f"Doba pythonu: {(end - start)}\n")
#################################

# math 
result = 0
start_time = time.time()
result = factorial(453)
end_time = time.time()
result = str(result)

print(f"Vysledek math: {result[:10]}")
print(f"Doba knihovny math: {(end_time - start_time)}")
print(f"Rozdíl math vs python: {(end_time - start_time) - (end - start)}")