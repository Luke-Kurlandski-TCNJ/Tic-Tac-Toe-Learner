"""
Serves as an "arena" for playing games between two models.
"""

from copy import deepcopy
import random

from tic_tac_toe.board import Board
from tic_tac_toe.model import Model

WIN_VALUE = 1
LOSS_VALUE = -1
TIE_VALUE = 0

class GamePlayer:
	"""
	Serves as an "arena" for playing games between two models.
	"""

	def __init__(self, model_learner, model_static):
		"""
		Handle playing multiple games between two models.

		Arguments:
			model_learner : the learning model
			model_static : the non-learning model
		"""

		self.model_learner = model_learner
		self.model_static = model_static

	def play_game(self):
		"""
		Play a single game between the two models.

		Return 
			learner_won : True if the learner wins, False if he loses,
				and None if there is a tie.
		"""

		# Set up the game
		board = Board()
		batch = set()
		learner_won = None
		learning_model_goes_first = random.choice([True, False])

		# Perform until the game finishes for learning model first move
		while learning_model_goes_first and not board.game_over():

			# Move the learning model
			board_previous = deepcopy(board)
			board = self.model_learner.make_move(board_previous)

			# Add the learning model's data to the batch
			game_status = board.game_over()
			print("model_learner moves")
			print("game_status", game_status)
			if game_status is False:
				batch.add(
					(board_previous, 
					self.model_learner.target_function(board_previous))
				)
			elif game_status is True:
				batch.add((board_previous, TIE_VALUE))
				learner_won = None
				break
			elif game_status == self.model_learner.piece:
				batch.add((board_previous, WIN_VALUE))
				learner_won = True
				break
			elif game_status == self.model_static.piece:
				batch.add((board_previous, LOSS_VALUE))
				learner_won = False
				break
			else:
				raise ValueError("board.game_over() bad return")
			
			# FIXME: train model_learner on model_static's moves?

			# Move the non-learner
			board = self.model_static.make_move(board)
			game_status = board.game_over()
			print("model_static moves")
			print("game_status", game_status)
			if game_status is False:
				pass
			elif game_status is True:
				learner_won = None
				break
			elif game_status == self.model_learner.piece:
				learner_won = True
				break
			elif game_status == self.model_static.piece:
				learner_won = False
				break
			else:
				raise ValueError("board.game_over() bad return")


		# Perform until the game finishes for static model first move
		while not learning_model_goes_first and not board.game_over():
			
			# FIXME: train model_learner on model_static's moves?

			# Move the non-learner
			board = self.model_static.make_move(board)
			game_status = board.game_over()
			print("model_static moves")
			print("game_status", game_status)
			if game_status is False:
				pass
			elif game_status is True:
				learner_won = None
				break
			elif game_status == self.model_learner.piece:
				learner_won = True
				break
			elif game_status == self.model_static.piece:
				learner_won = False
				break
			else:
				raise ValueError("board.game_over() bad return")

			# Move the learning model
			board_previous = deepcopy(board)
			board = self.model_learner.make_move(board_previous)

			# Add the learning model's data to the batch
			game_status = board.game_over()
			print("model_learner moves")
			print("game_status", game_status)
			if game_status is False:
				batch.add(
					(board_previous, 
					self.model_learner.target_function(board_previous))
				)
			elif game_status is True:
				batch.add((board_previous, TIE_VALUE))
				learner_won = None
				break
			elif game_status == self.model_learner.piece:
				batch.add((board_previous, WIN_VALUE))
				learner_won = True
				break
			elif game_status == self.model_static.piece:
				batch.add((board_previous, LOSS_VALUE))
				learner_won = False
				break
			else:
				raise ValueError("board.game_over() bad return")
		
		print("Game over. Perform gradient descent.")
		# Adjust the learning model's parameter's
		self.model_learner.gradient_decent(batch)

		return learner_won

if __name__ == "__main__":
	tests()
