# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

count_of_t = int(lower_case_name1.count('t')) + int(lower_case_name2.count('t'))
count_of_r = int(lower_case_name1.count('r')) + int(lower_case_name2.count('r'))
count_of_u = int(lower_case_name1.count('u')) + int(lower_case_name2.count('u'))
count_of_e = int(lower_case_name1.count('e')) + int(lower_case_name2.count('e'))

count_of_l = int(lower_case_name1.count('l')) + int(lower_case_name2.count('l'))
count_of_o = int(lower_case_name1.count('o')) + int(lower_case_name2.count('o'))
count_of_v = int(lower_case_name1.count('v')) + int(lower_case_name2.count('v'))
# count_of_e = int(lower_case_name1.count('e')) + int(lower_case_name2.count('e'))

score1 = count_of_t + count_of_r + count_of_u + count_of_e
score2 = count_of_l + count_of_o + count_of_v + count_of_e

score = str(score1) + str(score2)
score_as_int = int(score)
# print(score)

if score_as_int <= 10 or score_as_int > 90:
    print(f"Your score is {score_as_int}, you go together like coke and mentos.")
elif score_as_int>=40 and score_as_int<=50:
    print(f"Your score is {score_as_int}, you are alright together.")
else:
    print(f"Your score is {score_as_int}.")
