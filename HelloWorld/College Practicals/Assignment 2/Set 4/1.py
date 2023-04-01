# 4.1 Write one line of Python that takes list a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] and makes a
# new list that has only the even elements of this list in it.

def onlyEvenList(listt):
    evenList = []
    for number in listt:
        if number % 2 == 0:
            evenList.append(number)
    return evenList

listt = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
result = onlyEvenList(listt)
print(f"This list contains only even numbers. \nList: {result}")
print("ID No: 21DCE042\nAuthor: Karangiya Jash Ramde")