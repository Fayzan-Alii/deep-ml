import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    a_np = np.array(a)
    b_np = np.array(b)

    if a_np.shape[1] != b_np.shape[0]:
        return -1
        
    c = np.matmul(a_np, b_np)

    return c.tolist()