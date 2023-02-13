#Step 1
import random
word_list = ["camel", "hello", "apple"]

wordSelected = random.choice(word_list).lower()
print(wordSelected)


# print(letterGuessed)
list = []
for letters in wordSelected:
    list.append("_")

i = 0
for letters in wordSelected:
    letterGuessed = input("Enter a letter: ").lower()

    if letters == letterGuessed:
        list[i] = letters
        print(list)
    else:
        print("noob")
    i += 1
