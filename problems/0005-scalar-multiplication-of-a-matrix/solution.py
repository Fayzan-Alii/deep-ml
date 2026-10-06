import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	matrix_mul = np.array(matrix)
	return (scalar * matrix_mul).tolist()