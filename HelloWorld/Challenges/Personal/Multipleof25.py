print("Program to check multiple of any number:")


number2 = int(input("\nNumber to check multiple of: "))
number = int(input(f"Number to check if it a multiple of {number2}: "))

if number2 % number == 0:
    print(f"\nMultiple of {number2}")
else:
    print(f"\nNot a mutliple of {number2}")