# -*- coding: utf-8 -*-
# @Author      : BrotherBe
# @Time        : 2019-10-31 15:13
# @Version     : Python 3.6.8
"""
建造者模式
建造者模式（Builder Pattern）使用多个简单的对象一步一步构建成一个复杂的对象。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
一个 Builder 类会一步一步构造最终的对象。该 Builder 类是独立于其他对象的。

介绍
意图：将一个复杂的构建与其表示相分离，使得同样的构建过程可以创建不同的表示。
主要解决：主要解决在软件系统中，有时候面临着"一个复杂对象"的创建工作，其通常由各个部分的子对象用一定的算法构成；由于需求的变化，这个复杂对象的各个部分经常面临着剧烈的变化，但是将它们组合在一起的算法却相对稳定。
何时使用：一些基本部件不会变，而其组合经常变化的时候。
如何解决：将变与不变分离开。
关键代码：建造者：创建和提供实例，导演：管理建造出来的实例的依赖关系。
应用实例： 1、去肯德基，汉堡、可乐、薯条、炸鸡翅等是不变的，而其组合是经常变化的，生成出所谓的"套餐"。 2、JAVA 中的 StringBuilder。
优点： 1、建造者独立，易扩展。 2、便于控制细节风险。
缺点： 1、产品必须有共同点，范围有限制。 2、如内部变化复杂，会有很多的建造类。
使用场景： 1、需要生成的对象具有复杂的内部结构。 2、需要生成的对象内部属性本身相互依赖。
注意事项：与工厂模式的区别是：建造者模式更加关注与零件装配的顺序。
"""
import abc
from enum import Enum
import time

STEP_DELAY = 3  # 考虑到这是示例，单位为秒


class PizzaProgress(Enum):
    queued = 1
    preparation = 2
    baking = 3
    ready = 4


class PizzaDough(Enum):
    thin = 1
    thick = 2


class PizzaSauce(Enum):
    tomato = 1
    creme_fraiche = 2


class PizzaTopping(Enum):
    mozzarella = 1
    double_mozzarella = 2
    bacon = 3
    ham = 4
    mushrooms = 5
    red_onion = 6
    oregano = 7


class Pizza(object):
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough: PizzaDough):
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))


class Cook(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def prepare_dough(self):
        """准备面团"""

    @abc.abstractmethod
    def add_sauce(self):
        """加酱"""

    @abc.abstractmethod
    def add_topping(self):
        """添加佐料"""

    @abc.abstractmethod
    def bake(self):
        """烘烤"""


class MargaritaBuilder(Cook):
    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5  # 考虑是示例，单位为秒

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarrella, oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class CreamyBaconBuilder(Cook):
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7  # 考虑是示例，单位为秒

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print('adding the creme fraiche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the creme fraiche sauce')

    def add_topping(self):
        print('adding the topping (mozzarella, bacon, ham, mushrooms, red onion,oregano) to your creamy bacon')
        self.pizza.topping.append([t for t in
                                   (PizzaTopping.mozzarella, PizzaTopping.bacon,
                                    PizzaTopping.ham, PizzaTopping.mushrooms,
                                    PizzaTopping.red_onion, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella, bacon, ham, mushrooms, red onion,oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder: Cook):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self) -> Pizza:
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input('What pizza would you like, [m]argarita or [c]reamy bacon?')
        builder = builders[pizza_style.lower()]()
    except KeyError:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return False, None
    return True, builder


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print('Enjoy your {}!'.format(pizza))


if __name__ == '__main__':
    main()
