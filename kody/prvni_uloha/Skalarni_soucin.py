import numpy as np
import time
# Python

start = time.time()

result = 0
a = (3, 9, 5)
b = (8, 7, 4)

for i in range(len(a)):
    result += a[i]*b[i]

end = time.time()
print(f"Vysledek python: {result}")
print(f"Doba trvani python: {(end - start)}")
###################################


# Numpy

start_time = time.time()

a = np.array([3, 9, 5])
b = np.array([8, 7, 4])

result = sum(a*b)

end_time = time.time()
print(f"Vysledek numpy: {result}")
print(f"Doba trvani numpy: {(end_time - start_time)}")
print(f"Rozdíl Numpy vs Python : {(end_time - start) - (end - start)}")