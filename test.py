import mysql.connector

# Provide mySQL connector with login data (for mydb obj)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="testdb"
)

# Test to see if mySQL database connected (uncomment)
# print(mydb)

# Initialized database cursor (can now init db commands)
mycursor =  mydb.cursor()

# Use cursor to exec code (like creating the db)
# mycursor.execute("CREATE DATABASE testdb")

# check if db was created:
# mycursor.execute("SHOW DATABASES")
#
# for db in mycursor:
#     print(db)

# Creating table
# mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# Deleting table
# mycursor.execute("DROP TABLE students")

# Showing created table
# mycursor.execute("SHOW TABLES")
#
# for tb in mycursor:
#     print(tb)

# Populating the database:

# Function to save sql commands
# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# Data for sql function (tuples)

# single
# student1 = ("Rachel", 22)

# tuples
# students = [("Bob", 12),
#             ("Amanda", 32),
#             ("Jacob", 21),
#             ("Avi", 28),
#             ("Michelle", 17),]

# execute command

# single:
# mycursor.execute(sqlFormula, student1)

# many:
# mycursor.executemany(sqlFormula, students)

# Saves changes in db
# mydb.commit()

# To run command in SQL and grab data
mycursor.execute("SELECT * FROM students")
# grab all rows fetched in result (from SQL code)
# for fetching all entries
myresult = mycursor.fetchall()

for row in myresult:
    print(row)

# for fetching one entry
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchone()

for row in myresult:
    print(row)