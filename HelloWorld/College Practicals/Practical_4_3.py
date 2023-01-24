def isUpperOrlower(string1):
    i = 0
    countUpper = 0
    countLower = 0
    # tuple1 = string1.split()
    for i in string1:
        if i.isupper() == True:
            countUpper += 1

        elif i.islower() == True:
            countLower += 1
        # print(i.islower())
    print(f"The numbers of uppercase letters is {countUpper} and numbers of lowercase letters is {countLower}")
    return 0

string1 = input("Enter a string: ")
isUpperOrlower(string1)

print("\nAuthor: Jash Karangiya \nID NO. 21DCE042")
