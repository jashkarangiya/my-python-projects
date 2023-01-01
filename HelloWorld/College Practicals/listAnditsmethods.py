print("================Program to learn list and its method================\n")

list = [1, 2, 4, 0, 5, 6]

#Appending element to the list
list.append(10)
print(f"Appending element: {list}")

#Applying extend function to the list
list2 = [11, 13, 15]
list.extend(list2)
print(f"Extended list: {list}")

#Applying remove function to the list:
list.remove(10)
print(f"After applying remove function: {list}")

#Applying reverse function to the list:
list.reverse()
print(f"After applying reverse function: {list}")

#Arranging list in ascending order:
list.sort()
print(f"List sorted in Ascending order: {list}")

#Arranging list in decending order:
list.sort(reverse=True)
print(f"List sorted in Decending order: {list}")

print("\nAuthor: Jash Karangiya \nID NO. 21DCE042")