"""
The program that runs the tic taco toe learning procedure.
"""

import csv

from model import Model
from game_player import GamePlayer

def main():

	# number games to play per cycle
	GAMES_PER_CYCLE = 100

	# Number of games to play
	MAX_GAMES = 1000

	# list of tuples such that the i'th element of record contains
		# (num games won, num games lost, num games tied) after playing
		# i games
	records = [(0,0,0)]

	model_learner = Model('X')
	model_static = Model('O')

	model_static.initialize_weights([.5, .7, .3, .7, .3, .7, .3])

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

		#print("Played", len(records), "games, record", records[-1])

		# Temp
		if len(records) > MAX_GAMES:
			break
	
	# Write records to csv file
	with open(str(MAX_GAMES) + '_records.csv','w') as out:
		csv_out = csv.writer(out)
		csv_out.writerow(['# Wins','# Losses', '# Ties'])
		for row in records:
			csv_out.writerow(row)

if __name__ == "__main__":
	main()
