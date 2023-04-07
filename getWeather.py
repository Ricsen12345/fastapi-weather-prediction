# Load .env file from current directory
from dotenv import load_dotenv
load_dotenv()

# Other libraries
import os
import pandas as pd
import mysql.connector

config = {
  "host": os.getenv("HOST"),
  "user": os.getenv("USERNAME"),
  "passwd": os.getenv("PASSWORD"),
  "db": os.getenv("DATABASE"),
  "ssl_ca": "/etc/ssl/cert.pem"
}

# Create a connection to the database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Get all data from the database
cursor.execute("SELECT * FROM Weather")
data = cursor.fetchall()

datetimeList = []
temperatureList = []
humidityList = []
raindropList = []

print(data)
for dt in data:
  print(dt)

# Prepare data dictionary to convert it to DataFrame
# dataDict = {'DateTime': None,
#             'Temperature': None,
#             'Humidity': None,
#             'Raindrop': None}

# Create dataframe
# df = pd.DataFrame(dataDict)
# df.to_excel()