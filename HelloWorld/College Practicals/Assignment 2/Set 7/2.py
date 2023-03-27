# 7.2 Write a program (function!) that takes a list and returns a new list that contains all the
# elements of the first list minus all the duplicates.

def removeDuplicateFromList(listt):
    return list(set(listt))

def takingInputList(numberOfElements):
    # initializing a empty list
    numList = []
    # print("Ahi function ma aave che")
    print("Enter the elements of list: ")
    for i in range(numberOfElements):
        element = int(input())
        numList.append(element)
    return numList

numberOfElements = int(input("Enter the number of elements in the list: "))
listt = takingInputList(numberOfElements)

# print(f"The given list is: {listt}\n")
result = removeDuplicateFromList(listt)
print(f"After using removeDuplicateFromList() function: {listt} --> {result}")

print("\nID No: 21DCE042\nAuthor: Karangiya Jash Ramde")

