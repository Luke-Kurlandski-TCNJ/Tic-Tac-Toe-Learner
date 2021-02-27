"""

"""

class GamePlayer:

	def __init__(self, model_learner, model_static):
		pass

	def play_game(self):

		# Set up the game
		board = blank_board()
		batch = set()					# will be used for training
		learner_won = None

		# Perform until the game finishes
		while learner_won is None:

			# Move the learning model
			board_previous = board
			board = self.model_learner.make_move(board_previous)

			# Add the learning model's data to the batch
			training_example = (board_previous, board.target_function())
			batch.add(training_example)

			# Anybody win?
			if game_over(board):
				learner_won = True
				break

			# Move the non-learner, do not learn
			board = self.model_static.make_move(board)

			# Anybody win?
			if game_over(board):
				learner_won = False
				break

		# Adjust the learning model's parameter's
		self.model_learner.gradient_decent(batch)

		return learner_won