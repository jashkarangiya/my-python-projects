# 5.1 Write a program to generate a random number between 1 and 9 (including 1 and 9). Ask
# the user to guess the number, then tell them whether they guessed too low, too high, or exactly
# right. (Hint: remember to use the user input lessons from the very first practical)

import random

numbers = [1,2,3,4,5,6,7,8,9]
randomNumber = random.choice(numbers)

userGuess = int(input("Guess the number: "))

if userGuess > randomNumber:
    print("Too high!")
elif userGuess < randomNumber:
    print("Too low!")
else:
    print("You guessed the exact number.")
print("ID No: 21DCE042\nAuthor: Karangiya Jash Ramde")