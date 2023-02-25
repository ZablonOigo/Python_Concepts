import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password=''

)
#create database
mycursor =mydb.cursor()
mycursor.execute('create database my_database')

#check if database exists
mycursor.execute('show database')
for x in mycursor:
    print(x)


#create a table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#check if table exists
my.execute('show tables')
for x in mycursor:
    print(x)