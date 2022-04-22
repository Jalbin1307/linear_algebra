import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

v = np.array([[1],
              [2],
              [3]])

w = np.array([1, 2, 3])

B = np.array([[1, 2, 3],
              [4, 5, 6]])

print("A =", A)
print("A.shape =", A.shape)

print("v =", v)
print("v.shape =", v.shape)

print("w =", w)
print("w.shape =", w.shape)     # (3,) == (1,3)

print("B =", B)
print("B.shape =", B.shape)