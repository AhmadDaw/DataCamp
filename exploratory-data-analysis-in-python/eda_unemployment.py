import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('unemployment.csv')

print(df.head())
print(df.info())
print(df.describe())
print(df.value_counts("continent"))

# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(data=df, x="2021", binwidth=1)
plt.show()
