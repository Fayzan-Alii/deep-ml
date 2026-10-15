import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	
	X_np = np.array(X)
	y_np = np.array(y)

	theta = np.linalg.inv(X_np.T @ X) @ X_np.T @ y_np

	return np.round(theta, decimals=4)