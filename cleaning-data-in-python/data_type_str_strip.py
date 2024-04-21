import pandas as pd
import random

# Create sample data
sales_order_ids = [f'SO{i:04}' for i in range(1, 11)]
revenues = [f'${random.randint(100, 1000)}' for _ in range(len(sales_order_ids))]
quantities = [random.randint(1, 100) for _ in range(len(sales_order_ids))]
marriage_stats = [random.choice([1, 2, 3]) for _ in range(len(sales_order_ids))]

# Create the DataFrame
df_sales = pd.DataFrame({
    'SalesOrderID': sales_order_ids,
    'Revenue': revenues,
    'Quantity': quantities,
    'marriage_stat': marriage_stats
})

print(df_sales.head())

# column datatypes
df_sales.dtypes

# missing values
df_sales.info()

# remove $ sign from the column
df_sales['Revenue']=df_sales['Revenue'].str.strip('$')

# convert to int
df_sales['Revenue']=df_sales['Revenue'].astype('int')

# verify the column type (if it is true will pass othwise will raise assertion error)
assert df_sales['Revenue'].dtype=='int'

# convert to int
df_sales['marriage_stat']=df_sales['marriage_stat'].astype('category')

# describe
df_sales.describe()

print(df_sales.head())
