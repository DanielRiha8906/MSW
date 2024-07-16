import scipy.integrate as integrate
import time

#Python
def f(x):
    return (x**2 - x + 4) / 4

start = time.time()

result = 0.0
x = 0
b = 2
dx = 0.0001

while x < b:
    result += dx * (f(x) + f(x + dx)) / 2
    x += dx

end = time.time()
print(f"Vysledek Python: {result}")
print(f"Doba trvani Python: {(end - start)}")

##################################################
#Scipy
start_time = time.time()
result, error = integrate.quad(lambda x: (x**2 - x + 4) / 4, 0, 2)
end_time = time.time()

print(f"Vysledek Scipy: {result}")
print(f"Doba trvani Scipy: {(end_time - start_time)}")

print(f"Rozdíl Scipy vs Python: {(end_time - start_time) - (end - start)}")
