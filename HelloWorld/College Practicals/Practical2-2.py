print("==============Program to learn list of list==============")

List1 = [1, 2, 3, 4, ['python', 'java', 'c++', [10,20,30]], 5, 6, 7, ['apple', 'banana', 'orange']]

#Getting specific words from list of list:
print(f'Getting the word "pyhon" from list of list: \n-{List1[4][0]}')
print(f'Getting the word "orange" from list of list: \n-{List1[8][2]}')

#Printing List1 without using loops

print(f"Printing List1 without using loops: \n{List1 * 5}")
print("\nAuthor: Jash Karangiya \nID NO. 21DCE042")