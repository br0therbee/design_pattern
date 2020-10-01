# -*- coding: utf-8 -*-
# @Author      : BrotherBe
# @Time        : 2020-05-26 14:06
# @Version     : Python 3.6.8
"""
MVC 模式
MVC 模式代表 Model-View-Controller（模型-视图-控制器） 模式。这种模式用于应用程序的分层开发。
Model（模型） - 模型代表一个存取数据的对象或 JAVA POJO。它也可以带有逻辑，在数据变化时更新控制器。
View（视图） - 视图代表模型包含的数据的可视化。
Controller（控制器） - 控制器作用于模型和视图上。它控制数据流向模型对象，并在数据变化时更新视图。它使视图与模型分离开。

实现
我们将创建一个作为模型的 Student 对象。StudentView 是一个把学生详细信息输出到控制台的视图类，StudentController 是负责存储数据到 Student 对象中的控制器类，并相应地更新视图 StudentView。
MVCPatternDemo，我们的演示类使用 StudentController 来演示 MVC 模式的用法。
"""


class StudentModel(object):
    _roll_no = None
    _name = None

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


class StudentView(object):
    @staticmethod
    def details(name, roll_no):
        print("Student: ")
        print(f"\tName: {name}")
        print(f"\tRoll no: {roll_no}")


class StudentController(object):
    def __init__(self, model: StudentModel, view: StudentView):
        self.model = model
        self.view = view

    @property
    def name(self):
        return self.model.name

    @name.setter
    def name(self, name):
        self.model.name = name

    @property
    def roll_no(self):
        return self.model.roll_no

    @roll_no.setter
    def roll_no(self, roll_no):
        self.model.roll_no = roll_no

    def update_view(self):
        self.view.details(self.model.name, self.model.roll_no)


if __name__ == '__main__':
    def retrieve_student():
        student = StudentModel()
        student.name = "Robert"
        student.roll_no = "10"
        return student


    smodel = retrieve_student()
    sview = StudentView()
    controller = StudentController(smodel, sview)
    controller.update_view()
    controller.name = "John"
    controller.update_view()
