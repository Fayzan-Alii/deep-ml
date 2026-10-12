import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:

    unknowns = np.zeros(A.shape[1])
    updated = np.zeros(A.shape[1])
    for i in range(n):
        unknowns = updated.copy()
        updated.fill(0)
        for j in range(A.shape[0]):
            for k in range(A.shape[1]):
                if k != j:
                    updated[j] += -(A[j][k] * unknowns[k])
            updated[j] += b[j]
            updated[j] = updated[j] / A[j][j]

    return updated.round(decimals=4).tolist()