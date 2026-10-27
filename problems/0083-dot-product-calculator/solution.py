import numpy as np

def calculate_dot_product(vec1, vec2):
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""
	# Your code here
	# this is one is too easy, i will code it manually 
	#result = np.dot(vec1, vec2)
	result = 0
	for i in range(len(vec1)): 
		# for the dot product to work, both the lenghts of vec1 and vec2 should be the same
		result += vec1[i]*vec2[i] 
	return result

