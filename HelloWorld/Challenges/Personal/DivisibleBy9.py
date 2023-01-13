print("This is a program to check if the last digit of four number is divisible by 9 or not\n")

digit = int(input('Enter a number: '))
remainder = digit % 10;
print(remainder)

if remainder % 9 == 0:
    print("Divisible by 9")
else:
    print("Not divisible by 9")
