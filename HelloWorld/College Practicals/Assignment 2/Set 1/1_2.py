# 1.2 Write a program to ask the user for a number. Print out an appropriate message to the user
# depending on whether the number is even or odd. Hint: how does an even/odd number react
# differently when divided by 2?

# Function to define whether the number is odd or even
def oddOrEven(number):
    return (number % 2)

# Taking a user input number
number = int(input("Enter a number: "))

# Calling oddEvenNumber function
result = oddOrEven(number)

# checking the number:
if result == 1:
    print(f"{number} is odd.")
else:
    print(f"{number} is even.")
print("\nID: 21DCE042\nAuthor: Jash Karnagiya")

# End of the code