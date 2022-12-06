print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


answer1 = input('You are at a crossroad. Where do you want to go? Type "left" or "right" \n')
answer1_as_lower= answer1.lower()

if answer1_as_lower =="left":
    answer2 = input("You've come to a lake. There is an island in the middle of the lake" + 'Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    answer2_as_lower = answer2.lower()
    if answer2_as_lower == "wait":
        answer3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
        answer3_as_lower = answer3.lower()
        if  answer3_as_lower == "yellow":
            print("You found the treasure! You Win!")
        elif answer3_as_lower == "red":
            print("It's a room full of fire. Game Over")
        elif answer3_as_lower == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    elif answer2_as_lower == "swin":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You chose the wrong option. Game Over.")
elif answer1_as_lower == "right":
    print("You fell into a hole. Game Over.")

print("\nThank you for playing! You can play again.")


