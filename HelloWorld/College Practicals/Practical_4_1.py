def get_grade(sgpa):
  if sgpa >= 9:
    return "A+"
  elif sgpa >= 8:
    return "A"
  elif sgpa >= 7:
    return "B"
  elif sgpa >= 6:
    return "C"
  elif sgpa >= 5:
    return "D"
  else:
    return "F"
# Read the student's SGPA from the user
sgpa = float(input("Enter the student's SGPA: "))
# Get the corresponding grade
grade = get_grade(sgpa)
# Print the grade
print(f"The student's grade is: {grade}")
print("\nAuthor: Jash Karangiya \nID NO. 21DCE042")
