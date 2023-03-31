# 9.2 Write a function that takes an ordered list of numbers (a list where the elements are in
# order from smallest to largest) and another number. The function decides whether or not the
# given number is inside the list and returns (then prints) an appropriate Boolean.

def numberPresent(listt, number):
    if number in listt:
        return True
    else:
        return False

# Defining inputOfList() function
def takingInputList(numberOfElements):
    # initializing a empty list
    numList = []
    # print("Ahi function ma aave che")
    for i in range(numberOfElements):
        element = int(input())
        numList.append(element)
    return numList

# Taking a user input values
numberOfElements = int(input("Enter the number of elements in the list: "))


listt = takingInputList(numberOfElements)

number = int(input("Enter a number to check: "))

result = numberPresent(listt, number)

if result == True:
    print("The Number is present in the list.")
else:
    print("The Number is not present in the list.")

