# -*- coding:utf-8 -*-
# Author: Evan Mi


class School(object):

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self, stu_obj):
        print('为学员%s办理注册手续' % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self, staff_obj):
        print('雇佣新员工%s' % staff_obj.name)
        self.teachers.append(staff_obj)


class SchoolMember(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):

    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ----  info of Teacher:%s  ----
        Name: %s
        Age: %s
        Sex: %s
        Salary: %s
        Course: %s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print('%s is teaching course [%s]' % (self.name, self.course))


class Student(SchoolMember):

    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        ----  info of Student:%s  ----
        Name: %s
        Age: %s
        Sex: %s
        Stu_id: %s
        Grade: %s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self, amount):
        print('%s has paid tuition for [%s]' % (self.name, amount))


school = School("老男孩IT", "沙河")

t1 = Teacher("Oldboy", 56, "MF", 2000000, "Linux")
t2 = Teacher("Alex", 22, "M", 3000, "Python")

s1 = Student("ChenRonghua", 21, "MF", 1001, "Python")
s2 = Student("徐两位", 21, "F", 1002, "Linux")

t1.tell()
s1.tell()

school.enroll(s1)
school.hire(t1)

print(school.students)
print(school.teachers)

school.teachers[0].teach()

