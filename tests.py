"""
Test all aspects of the application.
"""

import pprint
import unittest

from tic_tac_toe.board import Board

class BoardTest(unittest.TestCase):
	def test_target_representation(self):	
		
		board = Board()
		board.board = [
			['X', 'X', 'O'],
			['X', 'O', None],
			[None, None, None]
		]

		x_X = board.target_representation('X')
		x_O = board.target_representation('O')

		expected_output_X = [1, 1, 1, -1, 1, -1, 0, 0, 0, 0]
		expected_output_O = [1, -1, -1, 1, -1, 1, 0, 0, 0, 0]

		assert x_X == expected_output_X
		assert x_O == expected_output_O

	def test_game_over_not_over(self):
		
		board = Board()
		board.board = [
			['X', 'X', 'O'],
			['X', 'O', None],
			[None, None, None]
		]
		assert board.game_over() is False

	def test_game_over_draw(self):

		board = Board()
		board.board = [
			['X', 'X', 'O'],
			['O', 'O', 'X'],
			['X', 'O', 'O']
		]
		assert board.game_over() is True

	def test_game_over_X_wins(self):
		
		board = Board()
		board.board = [
			['X', 'X', 'X'],
			['O', 'O', 'X'],
			['X', 'O', 'O']
		]
		assert board.game_over() == 'X'

	def test_game_over_O_wins(self):
		
		board = Board()
		board.board = [
			['X', 'X', 'O'],
			['O', 'O', 'O'],
			['X', 'O', 'X']
		]
		assert board.game_over() == 'O'

if __name__ == '__main__':
	unittest.main()