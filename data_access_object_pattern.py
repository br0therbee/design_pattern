# -*- coding: utf-8 -*-
# @Author      : BrotherBe
# @Time        : 2020-05-26 15:03
# @Version     : Python 3.6.8
"""
数据访问对象模式
数据访问对象模式（Data Access Object Pattern）或 DAO 模式用于把低级的数据访问 API 或操作从高级的业务服务中分离出来。以下是数据访问对象模式的参与者。
数据访问对象接口（Data Access Object Interface） - 该接口定义了在一个模型对象上要执行的标准操作。
数据访问对象实体类（Data Access Object concrete class） - 该类实现了上述的接口。该类负责从数据源获取数据，数据源可以是数据库，也可以是 xml，或者是其他的存储机制。
模型对象/数值对象（Model Object/Value Object） - 该对象是简单的 POJO，包含了 get/set 方法来存储通过使用 DAO 类检索到的数据。

实现
我们将创建一个作为模型对象或数值对象的 Student 对象。StudentDao 是数据访问对象接口。StudentDaoImpl 是实现了数据访问对象接口的实体类。DaoPatternDemo，我们的演示类使用 StudentDao 来演示数据访问对象模式的用法。
"""
import abc


class Student(object):
    def __init__(self, name, roll_no):
        self._name = name
        self._roll_no = roll_no

    @property
    def roll_no(self):
        return self._roll_no

    @roll_no.setter
    def roll_no(self, roll_no):
        self._roll_no = roll_no

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class BaseStudentDao(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_students(self):
        """获取所有学生数据"""

    @abc.abstractmethod
    def get_student(self, roll_no: int):
        """获取单个学生数据"""

    @abc.abstractmethod
    def update_student(self, student: Student):
        """更新学生数据"""

    @abc.abstractmethod
    def delete_student(self, student: Student):
        """删除学生数据"""


class StudentDao(BaseStudentDao):
    def __init__(self):
        self.students = [
            Student("Robert", 0),
            Student("John", 1)
        ]

    def delete_student(self, student: Student):
        self.students.remove(student)
        print(f"Student: \n\tRoll no: {student.roll_no}, deleted from database!")

    def get_students(self):
        return self.students

    def get_student(self, roll_no: int):
        return self.students[roll_no]

    def update_student(self, student: Student):
        self.students[student.roll_no].name = student.name
        print(f"Student: \n\tRoll no: {student.roll_no}, updated in the database!")


if __name__ == '__main__':
    student_dao = StudentDao()
    for s in student_dao.get_students():
        print(f"Student: \n\tRoll no: {s.roll_no}\n\tName: {s.name}")

    s = student_dao.get_students()[0]
    s.name = "Michael"
    student_dao.update_student(s)
    student_dao.get_student(0)
    print(f"Student: \n\tRoll no: {s.roll_no}\n\tName: {s.name}")
