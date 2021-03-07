"""
Serves as an "arena" for playing games between two models.
"""

from copy import deepcopy
import pprint
import random

from board import Board
from model import Model

WIN_VALUE = 100
LOSS_VALUE = -100
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

		# FIXME: incorporate radomization into which player goes first
		#learning_model_goes_first = random.choice([True, False])
		learning_model_goes_first = True

		#print("\nSTART GAME")
		board.print()
		# Perform until the game finishes for learning model first move
		while learning_model_goes_first and not board.game_over():

			# Move the learning model
			board_previous = deepcopy(board)
			board = self.model_learner.make_move(board_previous)
			board.print()

			batch.add(
					(board_previous, 
					self.model_learner.target_function(board))
			)

			# Add the learning model's data to the batch
			game_status = board.game_over()

			if game_status is True:	# Tie game
				batch.add((board, TIE_VALUE))
				learner_won = None
				break
			elif game_status == self.model_learner.piece:	# Won game
				batch.add((board, WIN_VALUE))
				learner_won = True
				break
			else:
				pass

			# Move the non-learner
			board = self.model_static.make_move(board)
			game_status = board.game_over()
			board.print()

			if game_status is True:	# Tie game
				batch.add((board_previous, TIE_VALUE))
				learner_won = None
				break
			elif game_status == self.model_static.piece:	# Lost game
				batch.add((board, LOSS_VALUE))
				learner_won = False
				break
			else:
				pass

		# Adjust the learning model's parameter's
		self.model_learner.gradient_descent(batch)
		
		return learner_won

def main():
	print("Do Nothing.")

if __name__ == "__main__":
	main()
