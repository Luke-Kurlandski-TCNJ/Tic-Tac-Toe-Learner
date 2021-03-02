"""
The program that runs the tic taco toe learning procedure.
"""

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

def test():
	pass

if __name__ == "__main__":
	main()