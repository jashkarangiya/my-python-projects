# cook your dish here
numberOfLoops = int(input())


for i in range(numberOfLoops):
    temperature = int(input())
    if temperature > 24:
        print("Yes")
    else:
        print("No")