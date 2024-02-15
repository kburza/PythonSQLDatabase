# code based on YT tutorial series:
# https://youtube.com/playlist?list=PLB5jA40tNf3tRMbTpBA0N7lfDZNLZAa9G&si=NmHsIfEhXRapTFDm

import mysql.connector

# CONNECTING DB --------------------------------------------------------------------------------------------------------

# Provide mySQL connector with login data (for mydb obj)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="testdb"
)

# Test to see if mySQL database connected (uncomment)
    # print(mydb)

# CURSOR INIT ----------------------------------------------------------------------------------------------------------

# Initialized database cursor (can now init db commands)
mycursor =  mydb.cursor()

# CREATING DB ----------------------------------------------------------------------------------------------------------

# Use cursor to exec code (like creating the db)
    # mycursor.execute("CREATE DATABASE testdb")

# check if db was created (display dbs):
    # mycursor.execute("SHOW DATABASES")
    # for db in mycursor:
    #     print(db)

# Creating table
    # mycursor.execute("CREATE TABLE students (name VARCHAR(255), age INTEGER(10))")

# Deleting table
    # mycursor.execute("DROP TABLE students")

# Showing created table
    # mycursor.execute("SHOW TABLES")
    # for tb in mycursor:
    #     print(tb)

# Populating the database:

# FUNCTIONS ------------------------------------------------------------------------------------------------------------

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

# QUERIES --------------------------------------------------------------------------------------------------------------

# To run command in SQL and grab data
    # mycursor.execute("SELECT * FROM students")
# grab all rows fetched in result (from SQL code)
# for fetching all entries
    # myresult = mycursor.fetchall()
    # for row in myresult:
    #     print(row)

# for fetching one entry
    # mycursor.execute("SELECT * FROM students")
    # myresult = mycursor.fetchone()
    # for row in myresult:
    #     print(row)

# Search (query) for students aged 17
    # sql="SELECT * FROM students WHERE age = 17"
    # mycursor.execute(sql)
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

# Search (query) for students named Avi
    # sql2 = "SELECT * FROM students WHERE name = 'Avi'"
    # mycursor.execute(sql2)
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

# Select rows where name from students are present where name starts with Mi-(and anything before)
# Where you place 'wildcard' has significance: before (%Mi), after (Mi%), both (%Mi%), etc...
    # sql3 = "SELECT * FROM students WHERE name LIKE 'Mi%'"
    # mycursor.execute(sql3)
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

# more examples:
    # sql4 = "SELECT * FROM students WHERE name LIKE '%ac%'"
    # mycursor.execute(sql4)
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

# passing in args:
    # sql5 = "SELECT * FROM students WHERE name = %s"
# store as tuple
    # mycursor.execute(sql5, ("Bob", ))
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

# UPDATING ENTRIES -----------------------------------------------------------------------------------------------------

# Updates Bob's age to 13 from whatever it was
# Side note: refresh needed in SQL database viewer
    # sql = "UPDATE students SET age = 13 WHERE name = 'Bob'"

    # mycursor.execute(sql)
    # mydb.commit()

# Or straight up just execute straight from cursor
# LIMIT operator: here we just grab the first 5 results form table
    # mycursor.execute("SELECT * FROM students LIMIT 5")
    #
    # myresult = mycursor.fetchall()
    #
    # for result in myresult:
    #     print(result)

# ORDERING QUERIES/RESULTS ---------------------------------------------------------------------------------------------

# Alphabetical order for names
    # sql = "SELECT * FROM students ORDER BY name"
    # mycursor.execute(sql)
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

# Order by number (size lowest to highest)
    # sql2 = "SELECT * FROM students ORDER BY age"
    # mycursor.execute(sql2)
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

# Order by number (size highest to lowest)
    # sql3 = "SELECT * FROM students ORDER BY age DESC"
    # mycursor.execute(sql3)
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

# Alphabetical order for names (flipped)
    # sql4 = "SELECT * FROM students ORDER BY age DESC"
    # mycursor.execute(sql4)
    # myresult = mycursor.fetchall()
    # for result in myresult:
    #     print(result)

# DELETING ENTRIES/TABLES ----------------------------------------------------------------------------------------------

# Insert mike into students table
    # sqlForm = "INSERT INTO students (name, age) VALUES (%s, %s)"
    # Mike = ("Mike", 25)
    # mycursor.execute(sqlForm, Mike)
    # mydb.commit()
#check
    # mycursor.execute("SELECT * FROM students")
    # myresult = mycursor.fetchall()
    # for r in myresult:
    #     print(r)
    # print("")

# Delete mike from students table
    # sql2 = "DELETE FROM students WHERE name = 'Mike'"
    # mycursor.execute(sql2)
    # mydb.commit()
# check
    # mycursor.execute("SELECT * FROM students")
    # myresult = mycursor.fetchall()
    # for r in myresult:
    #     print(r)
    # print("")

# Deleting Table
    # mycursor.execute("CREATE TABLE test_table_for_deletion (name VARCHAR(255), age INTEGER(10))")
    # mydb.commit()
# show
    # mycursor.execute("SHOW TABLES")
    # for r in mycursor:
    #     print(r)
    # print("")

# 'IF EXISTS' is an optional failsafe
    # mycursor.execute("DROP TABLE IF EXISTS test_table_for_deletion")
    # mydb.commit()
# show
    # mycursor.execute("SHOW TABLES")
    # for r in mycursor:
    #     print(r)
    # print("")