"""
The program that runs the tic taco toe learning procedure.
"""

import csv
import matplotlib.pyplot as plt
import pandas as pd

from model import Model
from game_player import GamePlayer

def generate_graphs(records_csv):
	# Takes wins, loesses, and ties in CSV format
	df = pd.read_csv(records_csv)

	# Creates % Won column
	df["% Won"] =  df['# Wins'] / (df['# Losses'] + df['# Ties'] + df['# Wins'])
	
	# Creates % Won plot
	win_plot = df.plot(title='Tic-Tac-Toe Model % Win', y='% Won')
	win_plot.set_xlabel('# of Games Played')
	win_plot.set_ylabel('% of Games Won')
	win_plot.figure.savefig('%_games_won.pdf')

	# Creates % Loss column
	df["% Loss"] =  df['# Losses'] / (df['# Losses'] + df['# Ties'] + df['# Wins'])

	# Creates % Loss plot
	loss_plot = df.plot(title='Tic-Tac-Toe Model % Loss', y='% Loss')
	loss_plot.set_xlabel('# of Games Played')
	loss_plot.set_ylabel('% of Games Loss')
	loss_plot.figure.savefig('%_games_loss.pdf')

	# Creates % Tie column
	df["% Tie"] =  df['# Ties'] / (df['# Losses'] + df['# Ties'] + df['# Wins'])

	# Creates % Tie plot
	tie_plot = df.plot(title='Tic-Tac-Toe Model % Tie', y='% Tie')
	tie_plot.set_xlabel('# Games Played')
	tie_plot.set_ylabel('% of Games Tied')
	tie_plot.figure.savefig('%_games_tie.pdf')

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
	
	# [bias term, my corners, opp corners, my center center, opp center center, my side-center, opp side-center]
	model_static.initialize_weights([0, .75, -.75, -.25, .25, .5, -.5])

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

	# Creates graph of performence
	generate_graphs(str(MAX_GAMES) + '_records.csv')

if __name__ == "__main__":
	main()
