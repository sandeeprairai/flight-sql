import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('flights_cleaned.csv')

# Change username , password host port and database according to your configuration
engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/indigo1')

chunk_size = 1000
num_chunks = len(df) // chunk_size + 1

for i in range(num_chunks):
    start = i * chunk_size
    end = (i + 1) * chunk_size
    chunk_df = df.iloc[start:end]

    # Append the chunk to the MySQL database
    chunk_df.to_sql('flights1', con=engine, if_exists='append', index=False)



