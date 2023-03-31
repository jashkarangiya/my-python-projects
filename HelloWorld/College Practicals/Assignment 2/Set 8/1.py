# 8.1 Write a program (using functions!) that asks the user for a long string function.
# Containing multiple words. Print back to the user the same string, except with the words in
# backwards order. For example, say I type the string: My name is Michele Then I would see
# the string: Michele is name My shown back to me.

def printingBackwardString(string):
    list1 = string.split()
    # print(list1)

    list1 = list(reversed(list1))
    # print(list1)

    string= ' '.join(list1)
    # print(string)
    return string


string = input("Enter a string: ")
result = printingBackwardString(string)
print(f"\nString : {string}. \nReversed String: {result}")
print(f"\nThe string is '{string}' is now converted to '{result}'.")