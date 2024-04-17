def load(clean_data):
	# Write the data to a CSV file without the index column
	return clean_data.to_csv("transformed_sales_data.csv", index=False)