import numpy as np
import time

#Python
start = time.time()

result = [[10, 476, 346], [23, 675, 22], [35, 1356, 42]]

for i in range(len(result)):
    for j in range(len(result[0])):
        result[i][j] = result[i][j]*25

end = time.time()

print(f"Vysledek Python: {result}")
print(f"Doba trvani Python: {(end - start)}")


######################################
#Numpy
start_time = time.time()

matrix = [[10, 476, 346], [23, 675, 22], [35, 1356, 42]]
result = np.array(matrix)*25
end_time = time.time()

print(f"Vysledek Numpy: {result}")
print(f"Doba trvani Numpy: {(end_time - start_time)}")
print(f"Rozdil Numpy vs Python: {(end_time - start_time) - (end - start)}")