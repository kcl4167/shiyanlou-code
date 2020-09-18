#!/usr/bin/env python3
import sys
from collections import Counter
class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        return o


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year, grade):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.grade = grade

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        common = Counter(self.grade).most_common(4)
        ps = 0
        fl = 0
        for item in common:
            if item[0] != 'D':
                ps += item[1]
            else:
                fl += item[1]
        print("Pass: {}, Fail: {}".format(ps, fl))



class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers, grade):
        Person.__init__(self, name)
        self.papers = papers
        self.grade = grade

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        sl = []
        common = Counter(self.grade).most_common(4)
        for i, j in common:
            sl.append("{} : {}".format(i, j))
        print(', '.join(sl))


person1 = Person('Sachin')
if sys.argv[1] == "student":
    student1 = Student('Kushal', 'CSE', 2005, sys.argv[2])
    student1.get_grade()
else:
    teacher1 = Teacher('Prashad', ['C', 'C++'], sys.argv[2])
    teacher1.get_grade()

"""
print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
"""
