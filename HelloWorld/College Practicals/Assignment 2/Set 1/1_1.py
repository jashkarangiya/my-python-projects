# Create a program that asks the user to enter their name and their age. Print out a message
# that tells them the year they will turn 100 years old.

import datetime

# Defining a fuction for the program
def YearsTill100(years):
    return (100 - years)

# Taking a user input
age = int(input("Enter your age: "))

# Checking the conditions
if age < 100:
    # Function call
    today = datetime.date.today()
    year = today.year
    result = YearsTill100(age)
    print(f"You'll be 100 years old in the year {year+ result}")
else:
    print("You are already above 100!!")

print("\nID: 21DCE042\nAuthor: Jash Karnagiya")

# End of the code