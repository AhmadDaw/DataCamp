import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv('divorce.csv',parse_dates=['divorce_date', 'dob_man', 'dob_woman',  'marriage_date'])
print(divorce.dtypes)

sns.heatmap(divorce.corr(), annot=True)
plt.show()

# Create the scatterplot
sns.scatterplot(data=divorce,x='marriage_duration',y='num_kids')
plt.show()

# Create a pairplot for income_woman and marriage_duration
sns.pairplot(data=divorce,vars=["income_woman",'marriage_duration'])
plt.show()
