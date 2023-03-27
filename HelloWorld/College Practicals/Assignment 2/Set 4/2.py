# 4.2 Write a program to make a two-player Rock-Paper-Scissors game. (Hint: Ask for player
# plays (using input), compare them, print out a message of congratulations to the winner, and
# ask if the players want to start a new game)
# Rules: Rock beats scissors, Scissors beats paper, Paper beats rock

import random
import os


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
    # answer = int(input("Press 1 if you want to restart"))
    # if answer == 1:
    #     break


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
    # answer = int(input("Press 1 if you want to restart"))
    # if answer == 1:
    #     break


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


if selectToLower == 'scissors' and computerSelected == 'rock':

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
     Computer selected rock:
         _______
     ---'   ____)
           (_____)
           (_____)
           (____)
     ---.__(___)
     """)
    print("Computer won!!")

if selectToLower == 'paper' and computerSelected == 'rock':

    print("""
    You selected paper:
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

    print(""" 
     Computer selected rock:
         _______
     ---'   ____)
           (_____)
           (_____)
           (____)
     ---.__(___)
     """)

    print("You won!!")

if selectToLower == 'paper' and computerSelected == 'scissors':


    print("""
    You selected paper:
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

    print("""
    Computer selected scissors:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

    print("Computer won!!")

if selectToLower == 'rock' and computerSelected =='rock':

    print(""" 
    You selected rock:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

    print(""" 
     Computer selected rock:
         _______
     ---'   ____)
           (_____)
           (_____)
           (____)
     ---.__(___)
     """)
    print("Draw")

if selectToLower == 'scissors' and computerSelected =='scissors':

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
    Computer selected scissors:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
    print("Draw")
    # answer = int(input("Press 1 if you want to restart"))
    # if answer == 1:
    #     break

if selectToLower == 'scissors' and computerSelected =='scissors':

    print("""
    You selected paper:
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

    print("""
    Computer selected paper:
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

print("Draw")





