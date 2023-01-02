#Defining lengthFunction()
def lengthString(string1):
    i = 0
    for i in range(len(string1)):
        i += 1
    return i



string1 = input("Enter any string: ")
result = lengthString(string1) #Calling
print(f'The length of {string1} is: {result}')

string1 = input("Enter any string: ")
result = lengthString(string1)

print(f'The length of {string1} is: {result}')

