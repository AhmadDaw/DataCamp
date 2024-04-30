import pandas as pd

pit_df=pd.read_csv('baseball_stats.csv')


# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in pit_df.itertuples():
  print(row)
  i = row.Index
  year = row.Year
  wins = row.W
  
  # Check if rangers made Playoffs (1 means yes; 0 means no)
  if row.Playoffs == 1:
    print(i, year, wins)

run_diffs = []

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

# Loop over the DataFrame and calculate each row's run differential
for row in pit_df.itertuples():
    
    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    run_diffs.append(run_diff)

# Append new column
pit_df['RD'] = run_diffs
print(pit_df['RD'].max())
