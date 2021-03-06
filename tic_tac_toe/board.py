"""
The board which tac tac toe is played upon.
"""

import pprint

# Number of features in target representation.
NUM_FEATURES = 10

class Board:
	"""
	The board which tac tac toe is played upon.
	"""

	def __init__(self):
		"""
		Initialize an empty board.
		"""

		self.board = [
						[None, None, None],
						[None, None, None],
						[None, None, None]
		]

	def game_over(self):
		"""
		Determine whether or not the game is over.

		Returns:
			False : indicates the game is not over
			True : indicates the game is over and has ended in a draw
			'X' : indicates the 'X' player has won
			'O' : indicates the 'O' player has won
		"""

		# Check rows.
		for row in self.board:
			s1, s2, s3 = row[0], row[1], row[2]
			if s1 == s2 and s1 == s3 and not None in [s1, s2, s3]:
				return s1
		
		# Check columns.
		board_transposed = map(list, zip(*self.board))
		for row in board_transposed:
			s1, s2, s3 = row[0], row[1], row[2]
			if s1 == s2 and s1 == s3 and not None in [s1, s2, s3]:
				return s1

		# Check diagonals.
		s1, s2, s3 = self.board[0][0], self.board[1][1], self.board[2][2]
		if s1 == s2 and s1 == s3 and not None in [s1, s2, s3]:
			return s1
		s1, s2, s3 = self.board[0][2], self.board[1][1], self.board[2][0]
		if s1 == s2 and s1 == s3 and not None in [s1, s2, s3]:
			return s1

		# If reached this point, neither player has won.
		board_flattened = sum(self.board, [])
		if None in board_flattened:
			return False
		else:
			return True
		
	@staticmethod
	def number_of_features():
		"""
		Return the number of features in the target representation.
		"""

		return NUM_FEATURES

	def target_representation(self, positive_board_piece):
		"""
		Return the features, x_0, x_1,...x_10 for the current board.

		Notes: the representation assigns a numerical value to each of
			the nine squares. The value is x_i = 1 if the player has a
			piece in square i, x_i = 0 if square i is empty, and 
			x_i = -1 if the opponent has a piece is square i. The x_i
			represents the square value of square i, such that the
			squares are labelled 1, 2, 3, ..., 9 from top left to bottom
			right.

		Arguments:
			positive_board_piece : the piece that a player moves with,
				either 'X', or 'O'

		Returns:
			list of feature values
		"""

		x = []
		x.append(1)
		for row in self.board:
			for square in row:
				if square is None:
					x.append(0)
				elif square == positive_board_piece:
					x.append(1)
				else:
					x.append(-1)

		return x

def main():
	pass

if __name__ == "__main__":
	main()
