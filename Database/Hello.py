import mysql.connector

conn= mysql.connector.connect(
    host= "localhost",
    user = "21DCE042 Jash",
    password= "Jash@1265##",
    database = "Levi"
)

print(conn)

mycursor = conn.cursor()
# mycursor.execute("CREATE DATABASE Levi")
# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE employee(emp_id int, emp_name varchar(20), salary decimal(15,2))")

# sql = "INSERT INTO employee values(69, 'Levi Ackerman', 42000)"


# Update query:
sql = "UPDATE employee SET emp_name = 'Levi' WHERE emp_id = 69"

# Delete query:
# sql = "DELETE FROM employee where emp_id=69"



mycursor.execute(sql)

conn.commit()
