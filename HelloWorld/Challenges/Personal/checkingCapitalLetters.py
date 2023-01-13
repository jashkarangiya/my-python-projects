def capital_indexes(inputString):
    i = 0
    arr = []
    for i in range(len(inputString)):
        if inputString[i].isupper():
            arr.append(i)
        i += 1
    print(arr)
    return arr


inputStringg = input("Enter a string: ")
capital_indexes(inputStringg)