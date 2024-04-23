import pandas as pd
import numpy as np
import random

# Generate 15 random full names
full_names = ['John Doe', 'Jane Smith', 'Michael Johnson', 'Emily Davis', 'David Lee',
              'Sarah Wilson', 'Christopher Brown', 'Olivia Taylor', 'Daniel Anderson',
              'Sophia Martinez', 'William Hernandez', 'Isabella Gonzalez', 'Matthew Diaz',
              'Ava Ramirez', 'Jacob Flores']

# Generate 15 random phone numbers in the format 00x-xxx-xxx-xxxx
phone_numbers = []
for _ in range(15):
    area_code = f"{random.randint(0, 9)}"
    prefix_f = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    prefix = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    line_number = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    phone_number = f"+{area_code}-{prefix_f}-{prefix}-{line_number}"
    phone_numbers.append(phone_number)

# Create the Pandas DataFrame
df = pd.DataFrame({'Full Name': full_names, 'Phone Number': phone_numbers})

# Display the DataFrame
print(df)

# replace + with 00 and replace - with nothing
df['Phone Number']=df['Phone Number'].str.replace('+','00')
df['Phone Number']=df['Phone Number'].str.replace('-','')
print(df)

# Replace phone numbers with lower than 10 digits to NaN
digits=df['Phone Number'].str.len()
df.loc[digits <10,"Phone Number"] = np.nan
print(df)

# Find length of each row in Phone number column
sanity_check = df['Phone Number'].str.len()
# Assert minmum phone number length is 10
assert sanity_check.min() >= 10
# Assert all numbers do not have "+" or "-"
# assert df['Phone Number'].str.contains("+|-").any() == False
