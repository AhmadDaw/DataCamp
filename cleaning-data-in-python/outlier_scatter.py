import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

# Create a range of dates
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 1, 10)
dates = pd.date_range(start_date, end_date)

# Generate random temperatures
temperatures = [20,30,25,23,62,32,19,63,27,31]

# Create the DataFrame
df = pd.DataFrame({
    "Date": dates,
    "Temperature": temperatures
})

print(df)

plt.figure(1)
# Create scatter plot
plt.scatter(x = 'Date', y = 'Temperature', data = df)
# Create title, xlabel and ylabel
plt.title('Temperature in Celsius March 2019 - NYC')
plt.xlabel('Dates')
plt.ylabel('Temperature in Celsius')


temp_fah = df.loc[df['Temperature'] > 40, 'Temperature']
temp_cels = (temp_fah - 32) * (5/9)
df.loc[df['Temperature'] > 40, 'Temperature'] = temp_cels
# Assert conversion is correct
assert df['Temperature'].max() < 40

plt.figure(2)
# Create scatter plot
plt.scatter(x = 'Date', y = 'Temperature', data = df)
# Create title, xlabel and ylabel
plt.title('Temperature in Celsius March 2019 - NYC')
plt.xlabel('Dates')
plt.ylabel('Temperature in Celsius')

# Display all the figures
plt.show()
