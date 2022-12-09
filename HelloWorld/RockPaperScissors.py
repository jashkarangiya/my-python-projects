import random

print("Welcome to the game of Rock, Paper and Scissors!!\n\n")

select = input("What do you want to select?  ")

options = ["rock", "paper", "scissors"]

selectToLower = select.lower()
randomSelections = random.randint(0, 2)

computerSelected = options[randomSelections]

if selectToLower == 'rock' and computerSelected == 'scissors':
    # Rock
    print(""" 
    You selected rock:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

    # Paper
    # Scissors
    print("""
    Computer selected scissors:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

    print("You won!!")

if selectToLower == 'rock' and computerSelected == 'paper':
    # Rock
    print(""" 
    You selected rock:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

    # Paper
    # Scissors
    print("""
    Computer selected paper:
        _______
    ---'    ____)____
             ______)
             _______)   
            _______)
    ---.__________)
    """)

    print("Computer won!!")

if selectToLower == 'scissors' and computerSelected == 'paper':

    print("""
    You selected scissors:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

    print("""
    Computer selected 
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

    print("You won!!")


print("The computer selected: ")
