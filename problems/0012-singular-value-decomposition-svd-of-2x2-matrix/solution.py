import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    At = A.transpose()
    B = At @ A

    p, q, r = B[0][0], B[0][1], B[1][1]

    theta = 0.5 * np.arctan2(2*q, p - r)

    c = np.cos(theta)
    s = np.sin(theta)

    V = np.array([[c, -s], [s, c]])
    C = A @ V

    col1 = C[:, 0]
    col2 = C[:, 1]

    len1 = np.linalg.norm(col1)
    len2 = np.linalg.norm(col2)

    S = np.array([len1, len2])

    u1 = col1 / len1
    u2 = col2 / len2

    U = np.column_stack((u1, u2))

    Vt = V.transpose()

    return (U, S, Vt)