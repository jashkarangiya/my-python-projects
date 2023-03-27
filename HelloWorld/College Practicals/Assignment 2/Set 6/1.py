# 6.1 Write a program using a function to check whether the number is prime or not. (A prime
# number is a number that has no divisors.)

def divisor(number):
    divisorList = []
    for i in range(1, number+1):
        if number % i == 0:
            divisorList.append(i)
    return divisorList

number = int(input("Enter a number: "))
result = divisor(number)
if len(result) > 2:
    print("The given number is not prime!!")
else:
    print("The given number is prime")