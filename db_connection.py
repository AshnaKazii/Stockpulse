import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",     
    database="stockpulse"
)

cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
print(cursor.fetchone())
