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
mycursor.execute('show tables')
for x in mycursor:
    print(x)


    # insert values in database
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")


# select from a table

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)