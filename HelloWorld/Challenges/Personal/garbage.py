# cook your dish here
numberOfTestCases = int(input())

for i in range(numberOfTestCases):
    numberOfBooks = int(input())
    listt = []
    list2 = []
    for x in range(0,1):
        arrOfElements = input()
        listt = arrOfElements.split()

    for elements in listt:
        list2.append(int(elements))

    multiply= 0
    multiply = list2[0] * list2[1]

    if list2[0] <= 8:
        if multiply <= 500:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
