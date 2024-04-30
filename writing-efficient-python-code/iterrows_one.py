import pandas as pd

pit_df=pd.read_csv('baseball_stats.csv')

# Iterate over pit_df and print each index variable, row, and row type
for i,row in pit_df.iterrows():
    print(i)
    print(row)
    print(type(row))

# Print the row and type of each row
for row_tuple in pit_df.iterrows():
    print(row_tuple)
    print(type(row_tuple))

# Create an empty list to store run differentials
run_diffs = []

def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in pit_df.iterrows():
    runs_scored = row['RS']
    runs_allowed = row['RA']
    
    # Use the provided function to calculate run_diff for each row
    run_diff = calc_run_diff(runs_scored, runs_allowed)
    
    # Append each run differential to the output list
    run_diffs.append(run_diff)

pit_df['RD'] = run_diffs
print(pit_df)
