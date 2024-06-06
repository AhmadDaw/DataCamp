import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv('divorce.csv',parse_dates=['divorce_date', 'dob_man', 'dob_woman',  'marriage_date'])
print(divorce.dtypes)

divorce["marriage_year"]=divorce['marriage_date'].dt.year
divorce["man_age_marriage"] = divorce["marriage_year"] - divorce["dob_man"].dt.year
divorce["woman_age_marriage"] = divorce["marriage_year"] - divorce["dob_woman"].dt.year


# Create the scatter plot
sns.scatterplot(data=divorce,x='woman_age_marriage',y='income_woman',hue='education_woman')
plt.show()

# Create the KDE plot
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0)
plt.show()

# Create the KDE plot
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0,cumulative=True)
plt.show()


