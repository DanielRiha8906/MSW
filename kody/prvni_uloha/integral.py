import scipy.integrate as integrate
from time import process_time

# Python
start = process_time()
result = integrate.quad(lambda x: (x**2-x+4)/4, 0, 2)
end = process_time()

print(f"Výpočet integrace je: {result[0]}\nDoba trvání výpočtu: {(end - start)}")

##################################################

# Scipy 

def f(x):
    return (x**2-x+4)/4

start_time = process_time()

result = 0.0
x = 0
b = 2
dx = 0.0001

while x < b:
    result += dx * (f(x) + f((x+dx)))/2
    x += dx

end_time = process_time()

print(f"Výpočet integrace je: {result}\nDoba trvání výpočtu: {(end_time - start_time)}")

print(f"Rozdíl Scipy vs Python: {(end_time - start_time) - (end - start)}")