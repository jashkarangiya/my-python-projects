def sumOfList(lst):
    sum = 0
    for number in lst:
        sum += number
    return sum

lst = []

num = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, num):
    ele = int(input())
    lst.append(ele)  # adding the element
print(lst)
result = sumOfList(lst)
print(f"Sum of lsit: {result}")