class Employee:
    count = 0

    def __init__(self, name, des, salary):
        self.name = name
        self.des = des
        self.salary = salary
        Employee.count = Employee.count + 1

    def displaycount(self):
        print("Employee count : ", self.count)


    def empdisplay(self):
        print("Name : ", self.name)
        print("Des of Employee ", self.des)
        print("Salary : ", self.salary)
        print("Raised Salary : ", self.salary + (self.salary * 0.0104))


e1 = Employee("Jash", "CEO", 100)
e2 = Employee("Levi", "CTO", 10000)
e1.displaycount()
e1.empdisplay()
e2.empdisplay()
print("\nAuthor: Jash Karangiya\nID NO. 21DCE042")
