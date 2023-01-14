# Program to replace numbers with '@' symbol:

# Author: Jash Karargiya
#Function of replacing numbers with '@'
def replacingNumberWithSymbol(letter):
    i = 0
    # Using for loops to separate elements in list
    for element in letter:
        if element.isdigit() == True:
            letter[i] = '@'
        i+=1

    # Joining the list into a string
    res = ''.join(letter)
    return res

# Taking user input string
string1 = input("Enter a string: ")
# Converting string into list
letter = [x for x in string1]

# Function calling
result = replacingNumberWithSymbol(letter)
print(result)

# End of the code
