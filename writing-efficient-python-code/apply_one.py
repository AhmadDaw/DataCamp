import pandas as pd
import numpy as np

df=pd.read_csv('baseball_stats.csv')
pit_df=df[["RS" , "RA" ,  "W" , "Playoffs"]]

# Gather sum of all columns
stat_totals = pit_df.apply(sum, axis=0)
print(stat_totals)

# Gather total runs scored in all games per year
total_runs_scored = pit_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored)

def text_playoffs(num_playoffs): 
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No' 
    
# Convert numeric playoffs to text by applying text_playoffs()
textual_playoffs = pit_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)


# Display the first five rows of the DataFrame
print(df.head())

# Create a win percentage Series 
win_percs = df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to df
df['WP'] = win_percs
print(df, '\n')

# Display df where WP is greater than 0.50
print(df[df['WP'] >= 0.50])
