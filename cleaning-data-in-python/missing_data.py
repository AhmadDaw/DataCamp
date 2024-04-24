import pandas as pd
from datetime import datetime, timedelta

# cleaning missing data

# Create the data
dates = [datetime(2023, 4, 1) + timedelta(days=i) for i in range(10)]
temperature = [20, 22, 24, 21, 23, 25, 22, 24, 26, 23]
co2 = [400, None, 410, 402, 408, 415, 403, None, 420, 406]

data = {
    'Date': dates,
    'Temperature': temperature,
    'CO2': co2
}
# Create the DataFrame
airquality = pd.DataFrame(data)

# Display the DataFrame
print(airquality)
print("===========")

# Return missing values
print(airquality.isna())
print("===========")

# Get summary of missingness
print(airquality.isna().sum())
print("===========")

# Isolate missing and complete values aside
missing = airquality[airquality['CO2'].isna()]
complete = airquality[~airquality['CO2'].isna()]

# Describe complete DataFramee
print(complete.describe())
print("===========")

# Describe missing DataFramee
print(missing.describe())
print("===========")

# Drop missing values
airquality_dropped = airquality.dropna(subset = ['CO2'])
print(airquality_dropped.head())
print("===========")

# Replacing with statistical measures
co2_mean = airquality['CO2'].mean()
airquality_imputed = airquality.fillna({'CO2': co2_mean})
print(airquality_imputed.head())
print("===========")
