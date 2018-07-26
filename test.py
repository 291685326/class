class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def act(self):
        print(self.name, self.age, self.sex)


stu1 = Student('hellokitte', 2, 'nan')
stu1.act()