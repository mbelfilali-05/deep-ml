import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X = np.array(X, dtype = float)
	y = np.array(y, dtype = float)
	X_T = np.transpose(X)
	inv = np.linalg.inv(X_T @ X)  # * n'est pas la multiplication matricielle dans numpy, c'est @
	theta = inv @ X_T @ y

	return [round(float(c),4) for c in theta]
