import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	A_np = np.array(A, dtype=np.float64)
	T_np = np.array(T, dtype=np.float64)
	S_np = np.array(S, dtype=np.float64)
	
	det_T = np.linalg.det(T_np)
	det_S = np.linalg.det(S_np)

	if det_S == 0 or det_T == 0:
		return -1

	T_inverse = np.linalg.inv(T_np)

	result = T_inverse @ A_np @ S_np

	return result.round(decimals=3)