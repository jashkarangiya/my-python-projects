# 10.1 Given a .txt file that has a list of a bunch of names, count how many of each name there
# are in the file, and print out the results to the screen.

from collections import Counter

with open('./names', 'r') as file:
    names = file.read().splitlines()

name_counts = Counter(names)

for name, count in name_counts.items():
    print(f"{name}: {count}")
print("\nID No: 21DCE042\nAuthor: Karangiya Jash Ramde")