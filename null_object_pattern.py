# -*- coding: utf-8 -*-
# @Author      : BrotherBe
# @Time        : 2020-05-25 14:27
# @Version     : Python 3.6.8
"""
空对象模式
在空对象模式（Null Object Pattern）中，一个空对象取代 NULL 对象实例的检查。Null 对象不是检查空值，而是反应一个不做任何动作的关系。这样的 Null 对象也可以在数据不可用的时候提供默认的行为。
在空对象模式中，我们创建一个指定各种要执行的操作的抽象类和扩展该类的实体类，还创建一个未对该类做任何实现的空对象类，该空对象类将无缝地使用在需要检查空值的地方。

实现
我们将创建一个定义操作（在这里，是客户的名称）的 AbstractCustomer 抽象类，和扩展了 AbstractCustomer 类的实体类。工厂类 CustomerFactory 基于客户传递的名字来返回 RealCustomer 或 NullCustomer 对象。
NullPatternDemo，我们的演示类使用 CustomerFactory 来演示空对象模式的用法。
"""
import abc


class BaseCustomer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_null(self):
        """是否为空"""

    @abc.abstractmethod
    def name(self):
        """名称"""


class RealCustomer(BaseCustomer):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def is_null(self):
        return False


class NullCustomer(BaseCustomer):
    @property
    def name(self):
        return "Not Available in Customer Database"

    def is_null(self):
        return True


class CustomerFactory(object):
    names = {"Rob", "Joe", "Julie"}

    @classmethod
    def get_customer(cls, customer_name):
        for name in cls.names:
            if name == customer_name:
                return RealCustomer(name)
        return NullCustomer()


if __name__ == '__main__':
    c1 = CustomerFactory.get_customer("Rob")
    c2 = CustomerFactory.get_customer("Bob")
    c3 = CustomerFactory.get_customer("Julie")
    c4 = CustomerFactory.get_customer("Laura")
    print("Customers")
    print(c1.name)
    print(c2.name)
    print(c3.name)
    print(c4.name)
