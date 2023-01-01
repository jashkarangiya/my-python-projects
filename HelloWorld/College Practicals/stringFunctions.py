print("==============Program to learn Slice Function==============\n")

name = input("Enter a string: ")
print(f"String: {name}")
string = "Jash"

#Reversing a string:
revString = name[::-1]
print(f"Reversed string: {revString}")

#Replacing a string with other string:
replace = string.replace("Jash", "Pari")
print(f"Replacing Jash with Pari: {string} --> {replace}")

#Merging two strings:
tuple = ("Jash", "is", "also", "known", "as", "BlackPanther")
merge = " ".join(tuple)
print(f"Merging two string: {merge}")

#Finding character in string:
print(f"Finding 'a' in string - 'Jash': {string.find('a')}")

#Spliting string into multiple words:
exampleString = "Hello! How are you?"
print(f"Spliting string into multiple values: {exampleString.split()}")

print("\nAuthor: Jash Karangiya \nID NO. 21DCE042")