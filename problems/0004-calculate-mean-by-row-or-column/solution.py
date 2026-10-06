import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	a_t = np.array(matrix, dtype=float)
	mode = mode.lower()
	if mode == 'row':
	    return np.mean(a_t, axis=1)
	elif mode == 'column':
		return np.mean(a_t, axis=0)
	else:
		raise ValueError('Invalid mode')