def sqaureFunction(x):
    return x*x;

inter = int(input("Enter a number: "))
inter2 = 16

#Dynamical value:
result = sqaureFunction(inter)
print(f'Square: {result}')


print(f"\nThe value is {inter2}")

#static value:
result = sqaureFunction(inter2)
print(f'Square: {result}')
