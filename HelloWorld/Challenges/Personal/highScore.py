# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

n = len(student_scores)


for i in range(n):
  for j in range(0, n - i - 1):
    if student_scores[j] > student_scores[j + 1]:
      student_scores[j], student_scores[j + 1] = student_scores[j + 1], student_scores[j]


print(f"The highest score in the class is: {student_scores[-1]}")

# Or we can go with:
#
# # student_scores =[100, 89, 82, 85, 69, 10]
# #
# #
# # highest_scores = 0
# # for scores in student_scores:
# #     if scores > highest_scores:
# #         highest_scores =scores
# # print(highest_scores)
