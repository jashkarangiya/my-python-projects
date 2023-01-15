#Program to find sum and average of the given string

# Function to find Sum of numbers in a string
def sumOfNumberInString(letter):
    sum = 0
    for elements in letter:
        sum += int(elements)
    return sum

# Function to find Average of numbers in a string
def avgOfNumberInString(lengthOfLetter, sum):
    avg = 0
    avg = float(sum / len(letter))

    return avg

# Taking input from user
string1 = input("Enter any numbers: ")
# Converting string into list
letter = [x for x in string1]


lengthOfLetter = len(letter)

# Calling the functions
resultOfSum = sumOfNumberInString(letter)
resultOfAvg = avgOfNumberInString(lengthOfLetter, resultOfSum)

# Printing the final result
print(f"\nSum of numbers in given string is: {resultOfSum}")
print(f"Average of numbers in given string is: {resultOfAvg}")

# End of code

# Author: Jash Karangiya