import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('unemployment.csv')


print(df.dtypes)

# Update the data type of the 2019 column to a float
df["2019"] = df["2019"].astype(float)
# Print the dtypes to check your work
print(df.dtypes)

# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~df["continent"].isin(["Oceania"])

# Print unemployment without records related to countries in Oceania
print(df[not_oceania])

# Print the minimum and maximum unemployment rates during 2021
print(df['2021'].min(), df['2021'].max())

# Create a boxplot of 2021 unemployment rates, broken down by continent
sns.boxplot(data=df, x="2021", y="continent")
plt.show()
