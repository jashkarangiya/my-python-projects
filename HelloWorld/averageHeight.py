
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

height = 0;
for i in range(0, len(student_heights)):
  height += student_heights[i];

averageHeight = round(int(height / len(student_heights)))

print(averageHeight)
