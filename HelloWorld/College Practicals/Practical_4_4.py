def squareOfList(list1):

    list2 = []
    for i in list1:
        result = sqaureFunction(i)
        list2.append(result)

    return list2

def sqaureFunction(x):
    return x*x;

list1 = [2, 3, 4]
result2 = squareOfList(list1)
print(f"The sqaure of {list1} is {result2}")

print("\nAuthor: Jash Karangiya \nID NO. 21DCE042")