# 3.1 Take two lists, a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
# 12, 13] and write a program that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of different
# sizes.


list2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list3 = []

if len(list1) > len(list2):
    for number in list1:
        if number in list2:
            list3.append(number)
else:
    for number in list2:
        if number in list1:
            list3.append(number)
print(list3)

print("\nID: 21DCE042\nAuthor: Jash Karnagiya")

# End of the code
