import pandas as pd
import random
import datetime
import missingno as msno
import matplotlib.pyplot as plt

# Generate sample data
cust_ids = [f'cust_{i}' for i in range(1, 11)]
ages = [40,20,50,21,60,45,30,60,55,34]
acct_amounts = [round(random.uniform(1000, 10000), 2) for _ in range(10)]
inv_amounts = [1000,None,2000,None,3000,5000,3500,8000,6000,4200]
account_opened = [datetime.datetime(random.randint(2010, 2020), random.randint(1, 12), random.randint(1, 28)) for _ in range(10)]
last_transaction = [account_opened[i] + datetime.timedelta(days=random.randint(30, 365)) for i in range(10)]
make = ['online' if random.random() < 0.6 else 'in-person' for _ in range(10)]

# Create the DataFrame
banking = pd.DataFrame({
    'cust_id': cust_ids,
    'age': ages,
    'acct_amount': acct_amounts,
    'inv_amount': inv_amounts,
    'account_opened': account_opened,
    'last_transaction': last_transaction,
    'make': make
})

print(banking)

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by='age')
msno.matrix(banking_sorted)
plt.show()

# missing values are yound investors
