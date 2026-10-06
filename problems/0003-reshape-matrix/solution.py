import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a_rows = len(a)
	a_cols = len(a[0]) if a_rows > 0 else 0

	if a_rows * a_cols != new_shape[0] * new_shape[1]:
		return []
	else:
		flattened_list = []
		for i in range(a_rows):
			for j in range(a_cols):
				flattened_list.append(a[i][j])
		#print(flattened_list)
		reshaped_matrix = np.zeros(new_shape, dtype = int)
		#print(reshaped_matrix.shape)
		counter = 0
		for i in range(new_shape[0]):
			for j in range(new_shape[1]):
				reshaped_matrix[i][j] = flattened_list[counter]
				counter += 1
 
	return reshaped_matrix.tolist()