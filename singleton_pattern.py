# -*- coding: utf-8 -*-
# @Author      : BrotherBe
# @Time        : 2019-10-29 17:48
# @Version     : Python 3.6.8
"""
单例模式
单例模式（Singleton Pattern）是 Java 中最简单的设计模式之一。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。

注意：
1、单例类只能有一个实例。
2、单例类必须自己创建自己的唯一实例。
3、单例类必须给所有其他对象提供这一实例。

介绍
意图：保证一个类仅有一个实例，并提供一个访问它的全局访问点。
主要解决：一个全局使用的类频繁地创建与销毁。
何时使用：当您想控制实例数目，节省系统资源的时候。
如何解决：判断系统是否已经有这个单例，如果有则返回，如果没有则创建。
关键代码：构造函数是私有的。

应用实例：
1、一个班级只有一个班主任。
2、Windows 是多进程多线程的，在操作一个文件的时候，就不可避免地出现多个进程或线程同时操作一个文件的现象，所以所有文件的处理必须通过唯一的实例来进行。
3、一些设备管理器常常设计为单例模式，比如一个电脑有两台打印机，在输出的时候就要处理不能两台打印机打印同一个文件。

优点：
1、在内存里只有一个实例，减少了内存的开销，尤其是频繁的创建和销毁实例（比如管理学院首页页面缓存）。
2、避免对资源的多重占用（比如写文件操作）。
缺点：没有接口，不能继承，与单一职责原则冲突，一个类应该只关心内部逻辑，而不关心外面怎么样来实例化。

使用场景：
1、要求生产唯一序列号。
2、WEB 中的计数器，不用每次刷新都在数据库里加一次，用单例先缓存起来。
3、创建的一个对象需要消耗的资源过多，比如 I/O 与数据库的连接等。
"""
import time
from threading import RLock


class SingletonPattern1(type):
    """
    线程，进程都不安全，需加线程锁,
    remind: 建议使用，真单例模式，只会实例化一次。
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_lock'):
            cls._lock = RLock()
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, *kwargs)
        return cls._instances[cls]


class SingletonPattern2(object):
    """
    线程安全，不需加线程锁，进程不安全,
    remind: 不建议使用，非真正意义上的单例（不会重复创建类，但是每次会实例化类）
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
        return cls._instance


class A(SingletonPattern2):
    def __init__(self, a, b):
        self.a = a
        self.b = b


def test_s2():
    s = A(1, 2)
    print(s.a)
    print(s.b)
    s = A(2, 3)
    print(s.a)
    print(s.b)


class NormalClass1(metaclass=SingletonPattern1):
    def __init__(self):
        print(1)
        time.sleep(1)


class NormalClass2(SingletonPattern2):
    def __init__(self):
        print(self)
        time.sleep(1)


def f(i):
    r = NormalClass2()
    print(r)
    print(id(r))


if __name__ == '__main__':
    from concurrent.futures import ThreadPoolExecutor as ThreadPoolExecutor

    # with ThreadPoolExecutor(40) as e:
    #     e.map(f, range(40))
    f(1)
    f(1)