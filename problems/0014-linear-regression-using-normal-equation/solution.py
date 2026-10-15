import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	
	X_np = np.array(X, dtype=float)
	y_np = np.array(y, dtype=float)

	theta = np.linalg.inv(X_np.T @ X) @ X_np.T @ y_np

	return np.round(theta, decimals=4).tolist()