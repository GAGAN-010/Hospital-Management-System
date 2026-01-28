import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="hospital_user",
        password="hospital123",
        database="Mydata"
    )
    print("Connected successfully!")
except mysql.connector.Error as e:
    print("Error:", e)