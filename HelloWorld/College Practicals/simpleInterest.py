print("This is a program to calculate simple interest")

#Taking inputs from the users
principleAmount = int(input("\nEnter a amount: ₹ "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter number of years: "))

#Formula to find simple interest
simpleI = (principleAmount * rate * time ) / 100

print(f"\nSimple Interest: {simpleI}")

print("\nAuthor: Jash Karangiya \nID NO. 21DCE042")