import numpy as np

def add(A, B):
    C = np.zeros((3,3))
    for i in range(3):
       for j in range(3):
           C[i][j] = A[i][j] + B[i][j]

    return A

X = np.array(
    [[1, 8, 3],
     [4, 2, 6],
     [13, 8, 1]])

Y = np.array(
    [[4, 8, 4],
     [8, 2, 4],
     [5, 1, 10]])

Z = add(X,Y)
print(f"Z={Z}")
