"""
The board which tac tac toe is played upon.
"""

import pprint

class Board:

	def __init__(self):
		"""
		Initialize an empty board.
		"""

		self.board = [
						[None, None, None],
						[None, None, None],
						[None, None, None]
		]

	def target_representation(self, weights, positive_board_piece):
		"""
		Return a board value according to the representation, V-hat.

		Notes: the representation assigns a numerical value to each of
			the nine squares. The value is x_i = 1 if the player has a
			piece in square i, x_i = 0 if square i is empty, and 
			x_i = -1 if the opponent has a piece is square i. The x_i
			represents the square value of square i, such that the
			squares are labelled 1, 2, 3, ..., 9 from top left to bottom
			right.

		Arguments:
			weights : the learned numerical weights
			positive_board_piece : the piece that a player moves with,
				either 'X', or 'O'

		Returns:
			the value of the board, according to the weights
		"""

		x = [1]
		for row in self.board:
			for square in row:
				if square is None:
					x.append(0)
				elif square == positive_board_piece:
					x.append(1)
				else:
					x.append(-1)

		return sum([weights[i] * x[i] for i in range(len(x))])

def tests():

	board = Board()

	weights = [0, 1, 1, 1, 1, 10, 1, 1, 1, 1]
	board.board = [
		['X', 'X', 'O'],
		['X', 'O', None],
		[None, None, None]
	]
	print("Should value the middle piece highly: ")
	print("Board: ")
	pprint.pprint(board.board)
	print("'X' score:", board.target_representation(weights, 'X'))
	print("'O' score:", board.target_representation(weights, 'O'))

	weights = [0, 10, 1, 10, 1, 1, 1, 10, 1, 10]
	board.board = [
		['X', 'O', 'X'],
		['O', 'O', None],
		[None, None, None]
	]
	print("Should value the corner pieces highly: ")
	print("Board: ")
	pprint.pprint(board.board)
	print("'X' score:", board.target_representation(weights, 'X'))
	print("'O' score:", board.target_representation(weights, 'O'))

if __name__ == "__main__":
	tests()