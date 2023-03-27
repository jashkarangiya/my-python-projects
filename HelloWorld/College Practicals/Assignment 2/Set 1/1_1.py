# Create a program that asks the user to enter their name and their age. Print out a message
# that tells them the year they will turn 100 years old.

# Defining a fuction for the program
def YearsTill100(years):
    return (100 - years)

# Taking a user input
age = int(input("Enter your age: "))

# Checking the conditions
if age < 100:
    # Function call
    result = YearsTill100(age)
    print(f"You'll be 100 years old after {result} years")
else:
    print("You are already above 100!!")

# End of the code