import numpy as np
from scipy import linalg as la

matrix = np.random.randint(0, 10, 25).reshape(5, 5)
print("Our matrix: {}".format(matrix))
e_vals , e_vecs = la.eig(matrix)
print("Eingenvalues: {}".format(e_vals))
print("Eingenvectors: {}".format(e_vecs))