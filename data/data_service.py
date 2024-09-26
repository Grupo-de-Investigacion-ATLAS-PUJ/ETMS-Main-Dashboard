# /data/data_service.py

import pandas as pd
from influxdb import InfluxDBClient
from config import credentials

# InfluxDB client setup using credentials
client = InfluxDBClient(
    host=credentials.INFLUXDB_HOST,
    port=credentials.INFLUXDB_PORT,
    username=credentials.INFLUXDB_USER,
    password=credentials.INFLUXDB_PASSWORD,
    database=credentials.INFLUXDB_DATABASE
)

def query_data():
    query = "SELECT * FROM EVENT.EVENT WHERE variabletype='FwElmbAi' AND time > now() - 7d"
    result = client.query(query)
    
    # Convert the result to a pandas DataFrame
    df = pd.DataFrame(list(result.get_points()))
    
    # Handle missing or non-existent data
    if df.empty:
        return pd.DataFrame(columns=['time', 'original_value_float'])
    
    return df[['time', 'original_value_float']]

