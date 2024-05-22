import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


planes=pd.read_csv('')
# Count the number of missing values in each column
print(planes.isna().sum())

# Calculate median plane ticket prices by Airline
airline_prices = planes.groupby("Airline")["Price"].median()

print(airline_prices)

# Convert to a dictionary
prices_dict = airline_prices.to_dict()

# Map the dictionary to missing values of Price by Airline
planes["Price"] = planes["Price"].fillna(planes["Airline"].map(prices_dict))

# Check for missing values
print(planes.isna().sum())
