def removing_alphabets_and_numbers(stringArray):
    for element in stringArray:
        if element.isalpha() == True or element.isdigit() == True:
            print(i)
            stringArray.pop(i)
    string1 = ''.join(stringArray)
    print(string1)
    return string1



string1 = input("Enter a string: ")
stringArray = string1.split();

result = removing_alphabets_and_numbers(stringArray)
print(result)