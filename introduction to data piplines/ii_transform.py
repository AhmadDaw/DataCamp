import pandas as pd 


# using function
def extract(file):
    raw_data=pd.read_parquet(file)
    
    # Print the head of the DataFrame
    print(raw_data.head())
    
    # Return the extracted DataFrame
    return raw_data
    
# Extract data from the sales_data.parquet path
raw_sales_data = extract("sales_data.parquet")

def transform(raw_data):
  	# Only keep rows with `Quantity Ordered` greater than 1
    clean_data = raw_data.loc[raw_data["Quantity Ordered"]>1, :]
    
    # Only keep columns "Order Date", "Quantity Ordered", and "Purchase Address"
    clean_data = raw_data.loc[ :,["Order Date", "Quantity Ordered", "Purchase Address"]]
    
    # Return the filtered DataFrame
    return clean_data
    
clean_sales_data=transform(raw_sales_data)
