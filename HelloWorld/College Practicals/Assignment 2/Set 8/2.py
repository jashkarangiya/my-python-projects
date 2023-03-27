# 8.2 Write a password generator in Python. Be creative with how you generate passwords -
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a
# new password. Include your run-time code in a main method.

import random
import string

list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '`~']

print("Welcome to the PyPassword Generator!\n")

letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like? "))
numbers = int(input("How many number would you like? "))


# Easy password:
# i = 0
# password = ''
# for letter in range(1, letters+1):
#
#     random1 = random.choice(list_letters)
#     # print(random1)
#     password = password + random1
#
# for letter in range(1, symbols+1):
#
#     random2 = random.choice(list_symbols)
#     password = password + random2
#
# for letter in range(1, numbers+1):
#
#     random3 = random.choice(list_numbers)
#     password = password + random3
#
# print(f"Your password is: {password}")

# result = ''.join((random.choice(password)) for x in range(len(password)))
# print(" Password: ", result)
# # print("Hello")



# Hard Password:
i = 0
passwordlist = []
for letter in range(1, letters+1):

    random1 = random.choice(list_letters)
    # print(random1)
    passwordlist += random1

for letter in range(1, symbols+1):

    random2 = random.choice(list_symbols)
    passwordlist += random2

for letter in range(1, numbers+1):

    random3 = random.choice(list_numbers)
    passwordlist += random3

# print(passwordlist)
random.shuffle(passwordlist)
# print(passwordlist)

password = ''
for char in passwordlist:
    password += char

print(f"Your password is: {password}")