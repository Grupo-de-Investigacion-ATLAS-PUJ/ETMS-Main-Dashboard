from influxdb import InfluxDBClient

# Initialize the InfluxDB client
client = InfluxDBClient('localhost', 8086, 'etm', 'etm#123', 'winccoa')

# Define your query
query = "SELECT * FROM EVENT.EVENT"

# Execute the query
result = client.query(query)

# Convert the result into a list of points
points = list(result.get_points())

# Open a text file in write mode
with open('query_results.txt', 'w') as file:
    for point in points:
        file.write(str(point) + '\n')  # Convert each point to a string and write to the file

