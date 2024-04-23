import pandas as pd

# this code can be used to find the difference in categorical values between two dfs

# Create a DataFrame with 10 records
data = {
    'name': ['John Doe', 'Jane Smith', 'Mike Johnson', 'Sara Williams', 'Tom Brown', 'Emma Davis', 'James Wilson', 'Laura Taylor', 'David Anderson', 'Olivia Green'],
    'birthday': ['1990-01-01', '1985-05-05', '1992-12-12', '1988-07-07', '1993-03-13', '1995-09-25', '1991-02-02', '1989-06-16', '1987-11-11', '1996-04-24'],
    'blood_type': ['A', 'B', 'AB', 'O', 'A+', 'B+', 'AB+', 'O+', 'Z', 'B-']
}

df = pd.DataFrame(data)

# Create a DataFrame with only the blood_type column and only the correct blood types
true_blood_types = ['A', 'B', 'AB', 'O', 'A+', 'B+', 'AB+', 'O+', 'B-']
categories = pd.DataFrame(true_blood_types, columns=['blood_type'])

print(df)
print('============')
print(categories)
print('============')

# Print unique values of blood_type column in df
print('blood type: ', df['blood_type'].unique()) 
print('============')

# find the difference in categorical values between two dfs 
inconsistent_categories = set(df['blood_type']).difference(categories['blood_type'])
print(inconsistent_categories)
print('============')

# Get and print rows with inconsistent categories
inconsistent_rows = df['blood_type'].isin(inconsistent_categories)
print(df[inconsistent_rows])
print('============')

# Dropping inconsistent categories
inconsistent_categories = set(df['blood_type']).difference(categories['blood_type'])
inconsistent_rows = df['blood_type'].isin(inconsistent_categories)
inconsistent_data = df[inconsistent_rows]
# Drop inconsistent categories and get consistent data only
consistent_data = df[~inconsistent_rows]

print(consistent_data)
