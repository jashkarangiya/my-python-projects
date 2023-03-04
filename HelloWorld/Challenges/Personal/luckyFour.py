import math
def countingFour(number):
    count = 0

    for i in range(0, len(str(number))):
        div = 0
        div = math.floor(number % 10)
        if div == 4:
            count += 1
        number = math.floor(number / 10)
    return count


numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    number = int(input())

    counts = countingFour(number)
    print(counts)