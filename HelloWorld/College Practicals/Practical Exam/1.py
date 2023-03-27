# 2) Write a Python class which has two methods get_String and
# print_String. get_String accept a string from the user and
# print_String print the string in upper case.


# Defining a class String in which I woul dwrite all the string function
class String:
    # Defining getString() function:
    def getString(self):
        string1 = input("Enter a String: ")
        return string1

    # Defining printString()
    def printString(self, string1):
        print(f"User input string in upper case: {string1.upper()}")
        return 0

# getString function call:
resultString = String.getString(0)

#printString function call:
String.printString(0,resultString)


print("ID No: 21DCE042\nAuthor: Karangiya Jash Ramde")
