import mysql.connector

#coonect to the database server
try:
    conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='indigo1'
)
    mycursor=conn.cursor()
    print('Connection established')

except:
    print('Connection error')


#create a database server
#mycursor.execute("CREATE DATABASE indigo1")
#conn.commit()

#To create a table
#airport -> airport_id|code\name

# mycursor.execute("""
# CREATE TABLE airport(
#    airport_id INTEGER PRIMARY KEY,
#    code VARCHAR(10) NOT NULL,
#    city VARCHAR(50) NOT NULL,
#    name VARCHAR(255) NOT NULL
      
# )



# """)
# conn.commit()

#Insert data to the table

# mycursor.execute("""
# INSERT INTO airport VALUES
# (1,'DEL','New Delhi','IGIA'),
# (2,'CCU','Kolkata','NSCA'),
# (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()

#search/Retrive
mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
data=mycursor.fetchall()
print(data)

# for i in data:
#     print(i[3])

#update
# mycursor.execute("""
# UPDATE airport
# SET name='BOMBAY'
# WHERE airport_id=3

# """)
# conn.commit()

# mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
# data=mycursor.fetchall()
# print(data)


#delete
# mycursor.execute("DELETE FROM airport WHERE airport_id=3")
# conn.commit()

# mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
# data=mycursor.fetchall()
# print(data)