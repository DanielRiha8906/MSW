import numpy as np
import time
# Python cyklus

start = time.time()

vysledek = 0
a = (3, 9, 5)
b = (8, 7, 4)

for i in range(len(a)):
    vysledek += a[i]*b[i]

end = time.time()

print(f"Skalární součin je {vysledek}\nDoba trvání výpočtu: {(end - start)}")

###################################


# Numpy

start_time = time.time()

a = np.array([3, 9, 5])
b = np.array([8, 7, 4])

vysledek = sum(a*b)

end_time = time.time()

print(f"Numpy výpočet je: {vysledek}\nDoba trvání výpočtu: {(end_time - start)}")

print(f"Rozdíl Numpy vs Python : {(end_time - start) - (end - start)}")