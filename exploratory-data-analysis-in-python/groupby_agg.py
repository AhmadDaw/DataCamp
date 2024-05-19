import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('unemployment.csv')

# Print the mean and standard deviation 
print(df.mean())
print(df.std())

# Print the mean and standard,'std deviation of rates by year
print(df.agg(['mean','std']))

# Print yearly mean and standard deviation grouped by continent
print(df.groupby('continent').agg(['mean','std']))

continent_summary = df.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021 = ('2021','mean'),
    # Create the std_rate_2021 column
    std_rate_2021 = ('2021','std'),
)
print(continent_summary)

# Create a bar plot of continents and their average unemployment
sns.barplot(data=df, x="continent", y='2021')
plt.show()

