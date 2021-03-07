"""
The board which tac tac toe is played upon.
"""

import pprint

# Number of features in target representation.
NUM_FEATURES = 7

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

		row  = 3
		column = 3
		
		Fill_Counter = 0
		
		for x in range(row):
			for y in range(column):
				if self.board[x][y] != None:
					Fill_Counter += 1
				if self.Right_Check(x) == 'X' or self.Down_Check(y) == 'X' or self.Diagonal_Left(x, y) == 'X' or self.Diagonal_Right(x,y) == 'X':
					return 'X'
				if self.Right_Check(x) == 'O' or self.Down_Check(y) == 'O' or self.Diagonal_Left(1, 3) == 'O' or self.Diagonal_Right(x,y) == 'O':
					return 'O'
			if Fill_Counter == 9:
				return True
		return False
	
	def Right_Check(self, x):
		"""Associated with game_over."""
		
		x_count = 0
		o_count = 0
		for i in range(3):
			if self.board[x][i] == 'X':
				x_count += 1
				if x_count == 3:
					return 'X'
			if self.board[x][i] == 'O':
				o_count += 1
				if o_count == 3:
					return 'O'
		return False
	
	def Down_Check(self, y):
		"""Associated with game_over."""

		x_count = 0
		o_count = 0
		for i in range(3):
			if self.board[i][y] == 'X':
				x_count += 1
				if x_count == 3:
					return 'X'
			if self.board[i][y] == 'O':
				o_count += 1
				if o_count == 3:
					return 'O'
		return False

	def Diagonal_Left(self, x, y):
		"""Associated with game_over."""

		x_count = 0
		o_count = 0
		for i in range(3):
			if self.board[i][3 - 1 - i] == 'X':
				x_count += 1
				if x_count == 3:
					return 'X'
			if self.board[i][3 - 1 - i] == 'O':
				o_count += 1
				if o_count == 3:
					return 'O'
						
		return False
	
	def Diagonal_Right(self, x, y):
		"""Associated with game_over."""

		x_count = 0
		o_count = 0
		for i in range(3):
			if self.board[i][i] == 'X':
				x_count += 1
				if x_count == 3:
					return 'X'
			if self.board[i][i] == 'O':
				o_count += 1
				if o_count == 3:
					return 'O'
		return False
		
	@staticmethod
	def number_of_features():
		"""
		Return the number of features in the target representation.

		Returns:
			NUM_FEATURES : int : number of features in current target
				representation
		"""

		return NUM_FEATURES

	def target_representation(self, positive_board_piece):
		"""
		Return the features, x_0, x_1, ..., x_6 for the current board.

		Notes:
			x_0 = 1
			x_1 = # my pieces in corners
			x_2 = # opponent pieces in corners
			x_3 = # my pieces in center
			x_4 = # opponent pieces in center
			x_5 = # my pieces in side-center
			x_6 = # opponent pieces in side-center

		Arguments:
			positive_board_piece : str : the piece that a player moves 
				with, either 'X', or 'O'

		Returns:
			list : feature representation of a board
		"""

		corners = [self.board[0][0], self.board[0][2], self.board[2][0], self.board[2][2]]
		center = self.board[1][1]
		side_center = [self.board[0][1], self.board[1][0], self.board[2][1], self.board[1][2]]

		x_0, x_1, x_2, x_3, x_4, x_5, x_6 = 1, 0, 0, 0, 0, 0, 0

		for p in corners:
			if p == positive_board_piece:
				x_1 += 1
			elif p is None:
				pass
			else:
				x_2 += 1

		if center == positive_board_piece:
			x_3 += 1
		elif center is None:
			pass
		else:
			x_4 += 1

		for p in side_center:
			if p == positive_board_piece:
				x_5 += 1
			elif p is None:
				pass
			else:
				x_6 += 1

		return [x_0, x_1, x_2, x_3, x_4, x_5, x_6]

	def target_representation_2(self, positive_board_piece):
		"""
		Return the features, x_0, x_1,...x_10 for the current board.

		This representation is not in current use.

		Notes: the representation assigns a numerical value to each of
			the nine squares. The value is x_i = 1 if the player has a
			piece in square i, x_i = 0 if square i is empty, and 
			x_i = -1 if the opponent has a piece is square i. The x_i
			represents the square value of square i, such that the
			squares are labelled 1, 2, 3, ..., 9 from top left to bottom
			right.

		Arguments:
			positive_board_piece : str : the piece that a player moves 
				with, either 'X', or 'O'

		Returns:
			list : feature representation of a board
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

	def print(self):
		"""
		Helper method to print the board in a nice manner.
		"""

		for x in self.board:
			print(*x, sep=' ')
		print()

def main():
	print("Do Nothing.")

if __name__ == "__main__":
	main()
  
