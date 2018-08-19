# code derived from:
# https://www.programiz.com/python-programming/examples/add-matrix
import numpy as np

X = np.array(
    [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]])

Y = np.array(
    [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]])

Z = np.zeros((3,3))
for i in range(3):
   for j in range(3):
       Z[i][i] = X[i][j] + Y[i][j]

print(f"Z={Z}")
