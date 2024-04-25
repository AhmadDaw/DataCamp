import pandas as pd
import random
import datetime

# the code impute missing values in acct_amount column with avg(acct_amount)*5 

# Generate sample data 
cust_ids = [f'cust_{i}' for i in range(1, 11)]
ages = [40,20,50,21,60,45,30,60,55,34]
acct_amounts = [1000,None,2000,None,3000,5000,3500,8000,6000,4200]
inv_amounts = [round(random.uniform(1000, 10000), 2) for _ in range(10)]
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

print(banking.head())

# Print number of missing values
print(banking.isna().sum())

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['acct_amount']

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna(banking['acct_amount'].mean() * 5)

print(banking_imputed.head())

# Print number of missing values
print(banking_imputed.isna().sum())
