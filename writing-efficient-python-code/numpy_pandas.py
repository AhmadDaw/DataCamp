import pandas as pd
import numpy as np

df=pd.read_csv('baseball_stats.csv')

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)


# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(df['W'].values, df['G'].values)

# Append a new column to baseball_df that stores all win percentages
df['WP'] = win_percs_np

print(df.head())



