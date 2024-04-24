import pandas as pd
from datetime import date
import datetime as dt

# Cross field validation: The use of multiple fields in a dataset to sanity check data integrity 

# Create the data
data = {
    'flight_number': ['AA123', 'UA456', 'DL789', 'BA321', 'JL654', 'SQ987'],
    'economy_class': [150, 200, 180, 160, 190, 220],
    'business_class': [30, 40, 35, 25, 45, 50],
    'first_class': [10, 15, 12, 8, 18, 20],
    'total_passengers': [180, 255, 120, 193, 255, 295],
}
# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

sum_classes = df[['economy_class', 'business_class', 'first_class']].sum(axis = 1)
passenger_equ = sum_classes == df['total_passengers']
# Find and filter out rows with inconsistent passenger totals
inconsistent_pass = df[~passenger_equ]
consistent_pass = df[passenger_equ]

print("=========== inconsistent pass ===========")
print(inconsistent_pass)

print("=========== consistent pass ===========")
print(consistent_pass)
print("===========")


# Create the data
data = {
    'user_id': ['user1', 'user2', 'user3', 'user4', 'user5', 'user6'],
    'Age': [27, 34, 43, 20, 28, 37],
    'Birthday': [date(1997, 5, 15), date(1990, 8, 22), date(1981, 3, 10), date(2003, 11, 5), date(1994, 6, 30), date(1987, 9, 1)]
}

# Create the DataFrame
users = pd.DataFrame(data)

# Display the DataFrame
print(users)

# Convert to datetime and get today's date
users['Birthday'] = pd.to_datetime(users['Birthday'])
today = dt.date.today()
# For each row in the Birthday column, calculate year difference
age_manual = today.year - users['Birthday'].dt.year
# Find instances where ages match
age_equ = age_manual == users['Age']
# Find and filter out rows with inconsistent age
inconsistent_age = users[~age_equ]
consistent_age = users[age_equ]

print("=========== inconsistent age ===========")
print(inconsistent_age)

print("=========== consistent age ===========")
print(consistent_age)
print("===========")


