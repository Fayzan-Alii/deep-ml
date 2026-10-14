def determinant_4x4(matrix: list[list[int|float]]) -> float:
	if len(matrix) == 2:
		return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

	det = 0

	for col in range(len(matrix)):

		minor = []

		for row in matrix[1:]:
			new_row = row[:col] + row[col + 1:]
			minor.append(new_row)

		sign = (-1) ** col

		det += sign * matrix[0][col] * determinant_4x4(minor)

	return det