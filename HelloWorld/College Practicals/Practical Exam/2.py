# 1) Write a Python program to convert a list into a nested dictionary of keys.

# Defining inputOfList() function
def takingInputList(numberOfElements):
    # initializing a empty list
    numList = []
    print("Ahi function ma aave che")
    for i in range(numberOfElements):
        element = int(input())
        numList.append(element)
    return numList

# Taking a user input values
numberOfElements = int(input("Enter the number of elements in the list: "))

# calling takingInputList() function
numList = takingInputList(numberOfElements)
# print(numList)

newDict = present = {}
for keys in numList:
    present[keys] = {}
    present = present[keys]
print(f"Converting list to dictionary: {numList} --> {newDict}")

print("\n\nID No: 21DCE042\nAuthor: Karangiya Jash Ramde")
