"""
Test all aspects of the application.

Run from command line using 
	> cd Tic-Tac-Toe-Learner
	> python tests.py
"""

import random
import pprint
import unittest
import sys

from board import Board
from model import Model
from game_player import GamePlayer
from main import main

def generate_random_board():

	def X_or_O():
		return random.choice(['X', 'O'])

	board = Board()
	board.board = [
		[X_or_O(), X_or_O(), X_or_O()],
		[X_or_O(), X_or_O(), X_or_O()],
		[X_or_O(), X_or_O(), X_or_O()]
	]

	return board

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
			['X', None, 'X'],
			['O', 'X', 'O']
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

	def test_game_over_by_row(self):

		board = Board()
		board.board = [
			['X', 'X', 'X'],
			['O', 'O', 'X'],
			['X', 'O', 'O']
		]
		assert board.game_over() == 'X'

	def test_game_over_by_col(self):

		board = Board()
		board.board = [
			['O', 'X', 'O'],
			['X', 'X', 'O'],
			['O', 'X', 'X']
		]
		assert board.game_over() == 'X'

	def test_game_over_by_diagonal(self):
		
		board = Board()
		board.board = [
			['O', 'O', 'X'],
			['X', 'X', 'O'],
			['X', 'O', 'X']
		]
		assert board.game_over() == 'X'

class ModelTest(unittest.TestCase):

	def test___init__(self):

		model = Model('X')
		assert model.piece == 'X'

		model = Model('O')
		assert model.piece == 'O'

	def test_initialize_random_weights(self):

		model = Model('X')
		model.initialize_random_weights()

		assert len(model.weights) == Board.number_of_features()

	def test_initialize_optimal_weights(self):

		model = Model('X')
		model.initialize_optimal_weights()

		assert len(model.weights) == Board.number_of_features()

	def test_target_function(self):

		board = Board()
		board.board = [
			['X', 'X', 'O'],
			['O', 'O', 'O'],
			['X', 'O', 'X']
		]

		model = Model('X')

		prediction = model.target_function(board)
		assert isinstance(prediction, float)

		prediction = model.target_function(board)
		assert isinstance(prediction, float)

	def test_gradient_descent(self):

		model = Model('X')

		batch_size = 10

		boards = [generate_random_board() for i in range(batch_size)]

		batch = {
			(board, model.target_function(board)) for board in boards
		}

		board_to_win = Board()
		board_to_win.board = [
			['O', 'X', 'O'],
			['O', 'X', 'O'],
			['X', None, 'X']
		]
		board_to_lose = Board()
		board_to_win.board = [
			['O', 'X', 'O'],
			['O', 'X', 'X'],
			[None, 'O', 'X']
		]

		batch.add((board_to_win, 1))
		batch.add((board_to_win, -1))

		old_weights = [w for w in model.weights]

		model.gradient_descent(batch)

		same = [old == new for old, new in zip(old_weights, model.weights)]

		if all(same):
			assert False
		else:
			assert True

	def test_make_move(self):

		board = Board()
		board.board = [
			['X', 'X', 'O'],
			['O', 'O', 'O'],
			['X', 'O', None]
		]

		model = Model('X')
		next_board = model.make_move(board)

		assert isinstance(next_board, Board)

		different_boards = False
		for row_old, row_new in zip(board.board, next_board.board):
			for square_old, square_new in zip(row_old, row_new):
				if square_old != square_new:
					different_boards = True

		assert different_boards is True

class GamePlayerTest(unittest.TestCase):

	def test___init__(self):
		
		g = GamePlayer(Model('X'), Model('O'))

		assert isinstance(g.model_learner, Model)
		assert isinstance(g.model_static, Model)

	def test_play_game(self):
		
		g = GamePlayer(Model('X'), Model('O'))
		status = g.play_game()

		assert isinstance(status, bool)

class mainTest(unittest.TestCase):

	def test_main(self):
		main()

if __name__ == '__main__':
	unittest.main()