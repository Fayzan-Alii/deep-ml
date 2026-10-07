import math
import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	trace = matrix[0][0] + matrix[1][1]
	determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

	# For quadratic formula
	a = 1
	b = - trace
	c = determinant

	root1 = (- b + math.sqrt((b ** 2) - 4 * (a) * (c))) / (2 * (a))
	root2 = (- b - math.sqrt((b ** 2) - 4 * (a) * (c))) / (2 * (a))

	eigenvalues = np.array([root1, root2], dtype=float)

	return np.sort(eigenvalues)[::-1]