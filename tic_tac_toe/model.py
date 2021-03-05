"""
ML Model that plays tic tac toe.
"""

import random

from board import Board

class Model:
	"""
	ML Model that plays tic tac toe.
	"""

	def __init__(self):
		"""
		Initialize an unlearned model.
		"""

		self.initialize_random_weights()

	def initialize_random_weights(self):
		"""
		Initially assign random values to the model's weights.
		"""

		self.weigths = list(
			np.random.random_sample(size = Board.number_of_features())
		)

	def initialize_optimal_weights(self):
		"""
		Assign weights according to the optimally learned weights.
		"""

		# FIXME: once we determine which weights are good, implement
		self.weights = [None] * Board.number_of_features()

	def target_function(self, board):
		"""
		Return the value of a board according to target representation.

		Arguments:
			board : the board to compute a score for

		Returns:
			value : the value for the board
		"""

		x = board.target_representation()
		value = sum([self.weights[i] * x[i] for i in range(len(x))])
		return value
	
	def gradient_descent(self, batch, n = .1):
		"""
		Algorithm Bloodgood described in class to adjust model's params.

		batch - Set of states and score
		"""
		# iterate through batch
		for i in batch:
			board_state = i[0]
			score = i[1]
			x = board_state.target_representation() # List of representation values

			# Compute approximation
			approximation = self.target_function(board_state)

			# iterate through weights and rep values
			for weight, rep_value in zip(self.weights, x):

				weight = weight + n * (score - approximation) * rep_value
		pass

	def make_move(board):
		"""
		Will decide where to move based upon the target function.

		Possibly use minimax algorithm.
		"""

		pass