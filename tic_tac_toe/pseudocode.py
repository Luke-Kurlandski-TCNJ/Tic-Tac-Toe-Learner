"""

"""

class Model:

	def __init__(self):
		pass

	def gradient_descent(self, batch):
		"""
		Algorithm Bloodgood described in class to adjust model's params.
		"""

		pass

	def make_move(board):
		"""
		Will decide where to move based upon the target function.
		"""

		pass

class Board:

	def __init__(self):
		pass

	def target_representation(self, board):
		"""
		An abstraction for representing a given board's value.
		"""

		return board_value

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

def main():

	GAMES = 10					# number games to play per cycle
	THRESHOLD = .1				# stabalizing performance

	proportion = 0				# proportion games won
	proportions = []			# tracking proportions

	model_learner = Model()
	model_static = Model()
	game = GamePlayer(model_learner, model_static)

	while True:

		# Play games and calculate the proportion of wins
		for i in range(GAMES):
			if game.play_game(model_learner, model_static) is True:
				proportion += 1
		proportion /= GAMES
		proportions.append(proportion)

		# If there are two proportions
		if len(proportions) > 2:
			difference = proportions[1] - proportions[0]
			# Stop playing games if model's performance stops improving
			if difference < THRESHOLD or difference > -1 * THRESHOLD:
				break
			# No need to maintain this data structure
			proportions = []