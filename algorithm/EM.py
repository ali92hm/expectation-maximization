"""
Author: Ali Hajimirza (ali@alihm.net)
Copyright Ali Hajimirza, free for use under MIT license.
"""
import numpy as np

# Exponent function for estimating e
exponent_func = np.vectorize(lambda x, std: np.exp((-1.0*x)/(2 * std)))

# Performs the E step give a list of x values, a list of means and a matrix of estimated values 
def E_step(x_list, mean_list, e_matrix):
	# Compute the standard deviation
	std_list = get_std(x_list, mean_list, e_matrix)
	estimated = list()
	for i,std in enumerate(std_list):
		estimated.append(exponent_func(np.square(x_list - mean_list[i]), std))
	# Calculating denominator
	estimated = np.array(estimated).transpose()
	for i, n in enumerate(estimated):
		estimated[i] /= n.sum()
	return estimated

# Performs the M step give a list of x values, a list of means
def M_step(x_list, e_matrix):
	# Calculating numerator
	numerator = np.dot(x_list, e_matrix)
	# Calculating denominator
	denominator = e_matrix.sum(axis=0)
	return np.divide(numerator, denominator)

# Compute the standard deviation
def get_std(x_list, mean_list, e_matrix):
	x_vector = x_list[np.newaxis].transpose()
	var = np.square(mean_list - x_vector) * e_matrix
	return np.sqrt(var.sum(axis=0)/e_matrix.sum(axis=0))

# Computes theta
def get_theta(e_matrix):
	return e_matrix.sum(axis=0) / len(e_matrix)

# Performs E-M for a number of steps
def simulate_E_M(x_list, e_matrix ,steps):
	mean_matrix = list()
	for i in xrange(steps):
		mean_list = M_step(x_list, e_matrix)
		mean_matrix.append(mean_list)
		e_matrix  = E_step(x_list, mean_list, e_matrix)
	return np.array(mean_matrix).transpose()