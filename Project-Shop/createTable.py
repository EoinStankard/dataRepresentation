import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database="projectShop"
)
mycursor = mydb.cursor()
sqlShop="CREATE TABLE shop (id INT AUTO_INCREMENT PRIMARY KEY,product VARCHAR(255), price DOUBLE)"
sqlCustomer="CREATE TABLE customer (id INT AUTO_INCREMENT PRIMARY KEY, product VARCHAR(255), quantity INT,price VARCHAR(255))"
mycursor.execute(sqlShop)
mycursor.execute(sqlCustomer)