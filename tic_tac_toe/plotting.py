import pandas as pd 

df = pd.read_csv('../experiments/records1.csv')

df['% Wins'] = df['# Wins'] / df.index
df['% Loss'] = df['# Losses'] / df.index
df['% Ties'] = df['# Ties'] / df.index

ax = df.plot(y='% Wins', kind='line', title='% games won (y axis) vs # games played (x axis)')
ax.figure.savefig('% Wins.png')
ax.figure.savefig('% Wins.pdf')

ax = df.plot(y='% Loss', kind='line', title='% games lost (y axis) vs # games played (x axis)')
ax.figure.savefig('% Loss.png')
ax.figure.savefig('% Loss.pdf')

ax = df.plot(y='% Ties', kind='line', title='% games tied (y axis) vs # games played (x axis)')
ax.figure.savefig('% Ties.png')
ax.figure.savefig('% Ties.pdf')