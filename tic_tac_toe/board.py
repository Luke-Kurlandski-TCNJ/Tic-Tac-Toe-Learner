"""
The board which tac tac toe is played upon.
"""

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

	weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

	board = Board()
	board.board[0][0] = 'X'
	board.board[1][0] = 'X'
	board.board[2][0] = 'O'

	print(board.target_representation(weights, 'X'))
	print(board.target_representation(weights, 'O'))

	board.board[0][1] = 'O'
	board.board[1][1] = 'O'
	board.board[2][1] = 'O'

	print(board.target_representation(weights, 'X'))
	print(board.target_representation(weights, 'O'))

if __name__ == "__main__":
	tests()