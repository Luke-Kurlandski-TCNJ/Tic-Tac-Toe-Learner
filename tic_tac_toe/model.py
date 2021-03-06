"""
ML Model that plays tic tac toe.
"""

from copy import deepcopy

import random

from tic_tac_toe.board import Board

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
			value : the value for the board state
		"""

		x = board.target_representation(self.piece)
		value = sum([self.weights[i] * x[i] for i in range(len(x))])
		return value
	
	def gradient_descent(self, batch, n=.01):
		"""
		Adjust model's learned weights based on Least Mean Squares cost.

		Arguments:
			batch : batch of (Board, score) training examples
			n : learning rate
		"""
		
		# iterate through batch
		for i in batch:
			board_state = i[0]
			score = i[1]
			x = board_state.target_representation(self.piece) # List of representation values

			# Compute approximation
			approximation = self.target_function(board_state)

			# iterate through weights and rep values
			for i in range(len(self.weights)):
				self.weights[i] = self.weights[i] + n * (score - approximation) * x[i]

	def make_move(self,board):
		"""
		Will decide where to move based upon the target function.

		Possibly use minimax algorithm.

		Major Issue: If player is worse if they make a move, this algo will fail 

		Originally make multiple deep copies and then evaluate and then set board = deep copy but this didnt seem right 
		"""

		scores_list= []

		#iterate through board and find scores of each possible move
		for i in rows: 
			for j in columns: 
				if board.board[i][j] is not None:
					#fill spot if available 
					board.board[i][j] = 'X'
					val = target_function(board)
					# list of scores based on each move 
					scores_list.append(val)
					board.board[i][j] = None
				else: 
					val = target_function(board)
					scores_list.append(val)

		#Find Board with max value
		max_score = max(scores_list)
		best_choice = scores_list.index(max_score)

		#in place of making multiple deep copies just find list score with max value
		row_index = best_choice/3
		col_index = best_choice%3

		#returns board index with X for best move
		board.board[row_index][col_index] = 'X'

		return board 


