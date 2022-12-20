print("Program for employee to calculate bonus:")

print("Hello the pillars of our company!!")
salary = int(input("\nEnter your salary: "))
experience = int(input("How many years have you worked for in our company? "))

if experience > 7:
    bonus = (15 * salary) / 100
    totalSalary = salary + bonus;
    print(f"Thank you for being with us for this long!!\n\nBonus: {bonus}.\nYour total salary would be {totalSalary}.  ")
else:
    print(f"Thank you being with us!\nYour salary would be: {salary}")


