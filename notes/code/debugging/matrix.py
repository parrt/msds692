import numpy as np

X = np.array(
    [[1, 8, 3],
     [4, 2, 6],
     [13, 8, 1]])

Y = np.array(
    [[4, 8, 4],
     [8, 2, 4],
     [5, 1, 10]])

Z = np.zeros((3,3))
for i in range(3):
   for j in range(3):
       Z[i][i] = X[i][j] + Y[i][j]

print(f"Z={Z}")
