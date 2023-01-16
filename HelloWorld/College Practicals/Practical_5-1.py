
# Multiple Inheritnance:
# class Person:
#     def personInfo(self, name, case):
#         print("Hello from Person Class")
#         print(f"Name: {name}")
#         print(f"Case: {case}")
# class Employee:
#     def employeeInfo(self, companyName, employeeID):
#         print("Hello Boiss from Employee class")
#         print(f"Company Name: {companyName} \nEmployee ID: {employeeID}")
# class Jash(Person, Employee):
#     def jashInfo(self, fname, lname):
#         print("Hello from Jash")
#         print(f"First Name: {fname} \nLast Name: {lname}")
#
# jash1 = Jash()
# jash1.personInfo("Jash", "69")
# jash1.employeeInfo("Riot Games", "420")
# jash1.jashInfo("Jash", "Karangiya")


# Multiple Inheritance:
class Person:
    def personInfo(self, name, case):
        print("Hello from Person Class")
        print(f"Name: {name}")
        print(f"Case: {case}")
class Employee(Person):
    def employeeInfo(self, companyName, employeeID):
        print("\nHello Boiss from Employee class")
        print(f"Company Name: {companyName} \nEmployee ID: {employeeID}")
class Jash(Person):
    def jashInfo(self, fname, lname):
        print("\nHello from Jash")
        print(f"First Name: {fname} \nLast Name: {lname}")
class HelloWorld(Person):
    def HelloInfo(self, word, word2):
        print("\nHello from Hello World")
        print(f"Word: {word} \nWord2: {word2}")

jash1 = Jash()
emp1 = Employee()
hello1 = HelloWorld()

jash1.personInfo("Jash", "69")
jash1.jashInfo("Jash", "Karangiya")

emp1.employeeInfo("Riot Games", "420")
emp1.personInfo("Ketul", "690")

hello1.HelloInfo("Hello", "World")
hello1.personInfo("Ayush", "52")



# Hierarchical Inheritance:
# class Person:
#     def personInfo(self, name, case):
#         print("Hello from Person Class")
#         print(f"Name: {name}")
#         print(f"Case: {case}")
# class Employee(Person):
#     def employeeInfo(self, companyName, employeeID):
#         print("\nHello Boiss from Employee class")
#         print(f"Company Name: {companyName} \nEmployee ID: {employeeID}")
# class Jash(Employee):
#     def jashInfo(self, fname, lname):
#         print("\nHello from Jash")
#         print(f"First Name: {fname} \nLast Name: {lname}")
#
# jash1 = Jash()
# jash1.personInfo("Jash", "69")
# jash1.employeeInfo("Riot Games", "420")
# jash1.jashInfo("Jash", "Karangiya")


# Single Inheritance:
