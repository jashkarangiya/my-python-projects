# 6.2 Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
# makes a new list of only the first and last elements of the given list. For practice, write this
# code inside a function.


def printFirstAndLastElementOfList(list1):
    list2 = []
    list2.append(list1[0])
    list2.append(list1[-1])
    return list2


list1 = [5, 10, 15, 20, 25, 30, 35, 40, 45]
result = printFirstAndLastElementOfList(list1)
print(f"First and last elements of the given list are: {result}")