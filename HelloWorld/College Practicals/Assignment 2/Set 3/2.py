# 3.2 Write a program by asking the user for a string and print out whether this string is a
# palindrome or not. (A palindrome is a string that reads the same forwards and backward.)

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

    # def checkPalindrome(self, string1, string2):
    #     for i in range(1, len(string1), -1):


# getString function call:
resultString = String.getString(0)

#printString function call:
String.printString(0,resultString)


print("ID No: 21DCE042\nAuthor: Karangiya Jash Ramde")
