"""
Serves as an "arena" for playing games between two models.
"""

from copy import deepcopy

from board import Board
from model import Model

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

		# Perform until the game finishes
		while not board.game_over():

			# Move the learning model
			board_previous = deepcopy(board)
			board = self.model_learner.make_move(board_previous)

			# Add the learning model's data to the batch
			game_status = board.game_over()
			if game_status is False:
				batch.add((board_previous, board.target_function()))
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
			
			# FIXME: is the non-learner not going to learn? Why would we
				# do this? Anybody understand.

			# Move the non-learner
			board = self.model_static.make_move(board)
			game_status = board.game_over()
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

		# Adjust the learning model's parameter's
		self.model_learner.gradient_decent(batch)

		return learner_won

def tests():
	pass

if __name__ == "__main__":
	tests()