"""
The program that runs the tic taco toe learning procedure.
"""

from tic_tac_toe.model import Model
from tic_tac_toe.game_player import GamePlayer

def main():

	# number games to play per cycle
	GAMES_PER_CYCLE = 100

	# Checks if performance has stabalizes once per cycle
	THRESHOLD = .1

	# list of tuples such that the i'th element of record contains
		# (num games won, num games lost, num games tied) after playing
		# i games
	records = []

	model_learner = Model('X')
	model_static = Model('O')

	game = GamePlayer(model_learner, model_static)

	while True:

		# Play games and tack wins, loss, ties
		for i in range(GAMES_PER_CYCLE):
			prev = records[-1]
			game_status = game.play_game()
			if game_status is True:		# win
				next_record = (prev[0] + 1, prev[1], prev[2])
			elif game_status is False:	# loss
				next_record = (prev[0], prev[1] + 1, prev[2])
			elif game_status is None:	# tie
				next_record = (prev[0], prev[1], prev[2] + 1)
			else:
				print("ERROR")
			records.append(next_record)

		# If the model has not improved above threshold, stop learning
		current_win_loss = records[-1][0] / records[-1][2]
		previous_win_loss = records[-1 * GAMES_PER_CYCLE][0] / records[-1 * GAMES_PER_CYCLE][2]
		if current_win_loss - previous_win_loss < THRESHOLD:
			break
	
	df = pd.DataFrame(
		data=records, 
		columns=["# Wins", "# Losses", "# Ties"]
	)
	df.to_csv('records.csv')

if __name__ == "__main__":
	main()
