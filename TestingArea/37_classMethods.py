class Student:

    count = 0
    total = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total += gpa

    def get_info(self):
        return f"{self.name} -> {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}!"

    @classmethod
    def get_ave_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {round(cls.total/cls.count, 2)}"


student1 = Student("Spongebob", 2.5)
student2 = Student("Patrick", 3)
student3 = Student("Spongebob", 4)

print(Student.get_count())
print(Student.get_ave_gpa())

