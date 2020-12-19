import mysql.connector

db = mysql.connector.connect(
	user="root",
	password="root",
	host="localhost"
)

cursor=db.cursor()
cursor.execute("CREATE DATABASE projectShop")