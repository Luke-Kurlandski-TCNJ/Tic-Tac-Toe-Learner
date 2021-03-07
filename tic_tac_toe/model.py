"""
ML Model that plays tic tac toe.
"""

from copy import deepcopy
import random

from board import Board

class Model:
	"""
	ML Model that plays tic tac toe.
	"""

	def __init__(self, piece):
		"""
		Initialize an unlearned model.

		Arguments:
			piece : the model's piece, either an 'X' or an 'O'
		"""

		self.piece = piece
		self.initialize_random_weights()

	def initialize_random_weights(self):
		"""
		Initially assign random values to the model's weights.
		"""

		self.weights = [random.random() for i in range(Board.number_of_features())]

	def initialize_weights(self, weights):
		"""
		Assign weights.

		Arguments:
			weights : list : weights to use for this model
		"""

		self.weights = weights

	def target_function(self, board):
		"""
		Return the value of a board according to target representation.

		Arguments:
			board : Board : the board to compute a score for

		Returns:
			value : float : the value for the board state
		"""

		x = board.target_representation(self.piece)
		value = sum([self.weights[i] * x[i] for i in range(len(x))])
		return value
	
	def gradient_descent(self, batch, n=.01):
		"""
		Adjust model's learned weights based on Least Mean Squares cost.

		Arguments:
			batch : iterable : batch of (Board, score) training examples
			n : float : learning rate
		"""
		
		# Iterate through batch
		for i in batch:
			board_state = i[0]
			score = i[1]

			# List of feature values
			x = board_state.target_representation(self.piece)

			# Compute approximation
			approximation = self.target_function(board_state)

			# Adjust weights based upon error
			for i in range(len(self.weights)):
				self.weights[i] = self.weights[i] + n * (score - approximation) * x[i]

	def make_move(self, board, randomize=False):
		"""
		Will decide where to move based upon the target function.

		Arguments:
			board : Board : a Board object representing current board
			randomize : bool : if True, model will make a random move
				50% of the time

		Returns:
			next_board : Board :a board object representing the next 
				best move
		"""

		if None not in sum(board.board, []):
			raise ValueError("Cannot make_move because game is over.")

		# list of ((row, col), score) tuples which tracks optimal move
		scores = []
		for i, row in enumerate(board.board):
			for j, square in enumerate(row):
				if square is None:
					board.board[i][j] = self.piece
					scores.append(((i, j), self.target_function(board)))
					board.board[i][j] = None

		# If randomize flag is set, sometimes make a random move
		if randomize:
			if random.choice([True, False]):	
				row, col = random.randint(0, 2), random.randint(0, 2)
			else:								
				row, col = max(scores, key = lambda i : i[1])[0]
		else:
			row, col = max(scores, key = lambda i : i[1])[0]
		
		# Get best move, and return a deepcopy of the board
		next_board = Board()
		next_board.board = deepcopy(board.board)
		next_board.board[row][col] = self.piece
		return next_board

def main():
	print("Do Nothing.")

if __name__ == "__main__":
	main()

		


