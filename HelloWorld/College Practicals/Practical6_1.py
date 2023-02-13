class student:
    def _init_(self, rollno, name):
        self.rollno = rollno
        self.name = name


class exam(student):
    def _init_(self, rollno, name, *marks):
        super()._init_(rollno, name)
        self.marks = marks


class result(exam):
    def _init_(self, rollno, name, *marks):
        super()._init_(rollno, name, marks)
        self.total = sum(marks)


# rs = result(101, "ketul", 23, 34, 56, 78, 90, 11)
print(f"student's marks{rs.total}")

