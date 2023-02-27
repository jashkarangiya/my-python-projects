class Emp:
    def __init__(self, name,salary):
        self.name=name
        self.salary=salary
    def displayEmployee(self):
        print("Name: ", self.name ,"\nSalary: ", self.salary)

emp1=Emp("Jash Karangiya", 20000)
emp2=Emp("Levi Ackerman", 50000)
emp1.displayEmployee()
emp2.displayEmployee()

print("\nAuthor: Jash Karangiya\nID NO. 21DCE042")
