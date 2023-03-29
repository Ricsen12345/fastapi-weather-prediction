# Load .env file from current directory
from dotenv import load_dotenv
load_dotenv()

# Other libraries
import os
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

# cursor.execute("""
#   INSERT INTO person (name, age)
#   VALUES ('Itchen', 30)
# """)
# cnx.commit()

cursor.execute("""
  SELECT * FROM person
""")

res = cursor.fetchall()
print(res)