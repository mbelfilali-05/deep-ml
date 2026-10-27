def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	rows = len(a)
	col = len(a[0])
	result = []

	if col == len(b):
		for i in range((rows)):
			calcul = 0
			for j in range(col):
				calcul += a[i][j] * b[j]
			result.append(calcul)
		return result
	else:
		return -1
		
	