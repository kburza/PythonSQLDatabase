import mysql.connector

# Provide mySQL connector with login data (for mydb obj)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password"
)

# Test to see if mySQL database connected (uncomment)
# print(mydb)

# Initialized database cursor (can now init db commands)
mycursor =  mydb.cursor()

# Use cursor to exec code (like creating the db)
# mycursor.execute("CREATE DATABASE testdb")

# check if db was created:
mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)