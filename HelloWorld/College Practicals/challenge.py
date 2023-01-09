list1 = [1, 2, 3, 4, 6]

print(list1)
list2 = []
for element in list1:
    if element % 2 != 0:
        list2.append(element)
print(list2)

# Using comprehension method:

# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
#
#
# list_using_comp = [var for var in input_list if var % 2 == 0]
#
# print("Output List using list comprehensions:",
# 							list_using_comp)
