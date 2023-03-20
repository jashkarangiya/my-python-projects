import mysql.connector

conn= mysql.connector.connect(
    host= "localhost",
    user = "21DCE042 Jash",
    password= "Jash@1265##",
    database = "LeviAckerman"
)

print(conn)

mycursor = conn.cursor()

# Database Created
mycursor.execute("CREATE DATABASE LeviAckerman")

# Table created
mycursor.execute("CREATE TABLE employee(emp_id int, emp_name varchar(20), salary decimal(15,2))")

#Insert Query
mycursor.execute("INSERT INTO employee values(69, 'Levi Ackerman', 42000)")
mycursor.execute("INSERT INTO eDmployee values(70, 'Mikasa Ackerman', 69000)")

records = mycursor.fetchall()

# For printing data from db
for record in records:
    print(record)


# Update query:
mycursor.execute("UPDATE employee SET emp_name = 'Jash Karangiya' WHERE emp_id = 69")

records = mycursor.fetchall()

# For printing data from db
for record in records:
    print(record)

# Select Operations
mycursor.execute("SELECT * FROM employee")
records = mycursor.fetchall()

# For printing data from db
for record in records:
    print(record)

# Delete query:
mycursor.execute("DELETE FROM employee where emp_id=69")

records = mycursor.fetchall()

# For printing data from db
for record in records:
    print(record)

conn.commit()
