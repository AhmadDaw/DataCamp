import pandas as pd

# Create a DataFrame with 10 records
data = {
    'name': ['John Doe', 'Jane Smith', 'Mike Johnson', 'Sara Williams', 'Tom Brown', 'Emma Davis', 'James Wilson', 'Laura Taylor', 'David Anderson', 'Olivia Green'],
    'birthday': ['1990-01-01', '1985-05-05', '1992-12-12', '1988-07-07', '1993-03-13', '1995-09-25', '1991-02-02', '1989-06-16', '1987-11-11', '1996-04-24'],
    'marriage_status': ['married ', 'unmarried', 'Married ', 'Unmarried', 'Married', 'Unmarried', ' Unmarried', ' married', ' Married', 'married']
}

df = pd.DataFrame(data)

# count values within one column (Series)
print(df['marriage_status'].value_counts())

# count values within one column in dataframe
df_group=df.groupby('marriage_status').count()
print(df_group)

# Capitalize or Lowercase
df['marriage_status'] = df['marriage_status'].str.upper()
print(df['marriage_status'].value_counts())
df['marriage_status'] = df['marriage_status'].str.lower()
print(df['marriage_status'].value_counts())

# remove spaces
df['marriage_status'] = df['marriage_status'].str.strip()
print(df['marriage_status'].value_counts())


# Create mapping dictionary and replace values
mapping = {'married':'1', 'unmarried':'0'}
df['marriage_status'] = df['marriage_status'].replace(mapping)
print(df['marriage_status'].unique())

