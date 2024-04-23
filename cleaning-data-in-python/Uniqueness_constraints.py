import pandas as pd

data = [
    {'first_name': 'John', 'last_name': 'Doe', 'address': '123 Main St', 'height': 175, 'weight': 80},
    {'first_name': 'Jane', 'last_name': 'Doe', 'address': '456 Oak Rd', 'height': 165, 'weight': 60},
    {'first_name': 'Bob', 'last_name': 'Smith', 'address': '789 Elm St', 'height': 180, 'weight': 90},
    {'first_name': 'Alice', 'last_name': 'Johnson', 'address': '321 Pine Rd', 'height': 160, 'weight': 55},
    {'first_name': 'Tom', 'last_name': 'Wilson', 'address': '654 Maple Ln', 'height': 172, 'weight': 75},
    {'first_name': 'Sarah', 'last_name': 'Davis', 'address': '987 Oak St', 'height': 168, 'weight': 62},
    {'first_name': 'Michael', 'last_name': 'Brown', 'address': '246 Elm Rd', 'height': 182, 'weight': 85},
    {'first_name': 'Emily', 'last_name': 'Taylor', 'address': '369 Pine St', 'height': 163, 'weight': 58},
    {'first_name': 'David', 'last_name': 'Anderson', 'address': '753 Maple Rd', 'height': 175, 'weight': 80},
    {'first_name': 'Jessica', 'last_name': 'Thompson', 'address': '159 Oak Ln', 'height': 162, 'weight': 57},
    {'first_name': 'John', 'last_name': 'Doe', 'address': '123 Main St', 'height': 175, 'weight': 80},
    {'first_name': 'Jane', 'last_name': 'Doe', 'address': '456 Oak Rd', 'height': 165, 'weight': 60},
    {'first_name': 'Bob', 'last_name': 'Smith', 'address': '789 Elm St', 'height': 180, 'weight': 90},
    {'first_name': 'Alice', 'last_name': 'Johnson', 'address': '321 Pine Rd', 'height': 160, 'weight': 55},
    {'first_name': 'Tom', 'last_name': 'Wilson', 'address': '654 Maple Ln', 'height': 172, 'weight': 75},
    {'first_name': 'Sarah', 'last_name': 'Davis', 'address': '987 Oak St', 'height': 168, 'weight': 62},
    {'first_name': 'Michael', 'last_name': 'Brown', 'address': '246 Elm Rd', 'height': 182, 'weight': 85},
    {'first_name': 'Emily', 'last_name': 'Taylor', 'address': '369 Pine St', 'height': 163, 'weight': 58},
    {'first_name': 'David', 'last_name': 'Anderson', 'address': '753 Maple Rd', 'height': 175, 'weight': 80},
    {'first_name': 'Jessica', 'last_name': 'Thompson', 'address': '159 Oak Ln', 'height': 162, 'weight': 57}
]

# Create the DataFrame
df = pd.DataFrame(data)
print(df.info())
print('============')
print(df.describe())
print('============')

duplicates = df.duplicated()
print(df[duplicates])
print('============')
# Column names to check for duplication
column_names = ['first_name','last_name','address']
duplicates = df.duplicated(subset = column_names, keep = False)

df[duplicates].sort_values(by = 'first_name')

df.drop_duplicates(inplace = True)
print(df)
print('============')
# Group by column names and produce statistical summaries
column_names = ['first_name','last_name','address']
summaries = {'height': 'max', 'weight': 'mean'}
height_weight = df.groupby(by = column_names).agg(summaries).reset_index()
# Make sure aggregation is done
duplicates = height_weight.duplicated(subset = column_names, keep = False)
height_weight[duplicates].sort_values(by = 'first_name')

print(height_weight)

