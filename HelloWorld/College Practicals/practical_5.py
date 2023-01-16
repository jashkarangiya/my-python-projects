class helloWorld:
    firstname = "Jash"
    print(type(firstname))
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Jash(helloWorld):
        # print(self.firstname)
    def noobi(self, lname):
        print(self.lastname)


fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

h1 = Jash(fname, lname)
# h2 = Jash(fname, ln)
h1.noobi(lname)
print(f"First Name: {h1.firstname} \nLast Name: {h1.lastname}")