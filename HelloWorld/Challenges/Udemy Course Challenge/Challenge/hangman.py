#Step 1
import random
word_list = ["camel", "hello", "apple"]

wordSelected = random.choice(word_list).lower()
# print(wordSelected)


# print(letterGuessed)
list = []
for letters in wordSelected:
    i = 0
    list.append("_")
    letterGuessed = input("Enter a letter: ").lower()

    if letters == letterGuessed:
        list[i] = letters
    else:
        print("noob")
    i += 1

print(list)



# for letters in wordSelected:
#     if letters == letterGuessed:
#         print("True")
#     else:
#         print("False")












