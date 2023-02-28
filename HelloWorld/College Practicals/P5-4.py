class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks
        
    def __lt__(self, other):
        return self.marks < other.marks

def find_first(s1, s2):
    if s1 < s2:
        print(s2.name, "will be first")
    else:
        print(s1.name, "will be first")

s1 = Student("Student 1", 80)
s2 = Student("Student 2", 90)
find_first(s1, s2)
print("21DCE034 VATSAL JAJADIYA")
