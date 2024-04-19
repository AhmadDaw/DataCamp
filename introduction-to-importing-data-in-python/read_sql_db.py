from sqlalchemy import create_engine
import pandas as pd

# create engine to connect and query the database 
engine = create_engine('sqlite:///Chinook.sqlite')

# create connection to the database
con = engine.connect()

# execute a query
rs = con.execute("SELECT * FROM Album")

# create a dataframe from query
df = pd.DataFrame(rs.fetchall())

# add columns names
df.columns = rs.keys()

# print df head()
print(df.head())

# close database connection
con.close()
