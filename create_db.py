import mysql.connector

my = mysql.connector.connect

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "mutahabe",
    )

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE puppies")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)