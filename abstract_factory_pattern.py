# -*- coding: utf-8 -*-
# @Author      : BrotherBe
# @Time        : 2019-10-30 12:19
# @Version     : Python 3.6.8
"""
抽象工厂模式
抽象工厂模式（Abstract Factory Pattern）是围绕一个超级工厂创建其他工厂。该超级工厂又称为其他工厂的工厂。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。
在抽象工厂模式中，接口是负责创建一个相关对象的工厂，不需要显式指定它们的类。每个生成的工厂都能按照工厂模式提供对象。

介绍
意图：提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。
主要解决：主要解决接口选择的问题。
何时使用：系统的产品有多于一个的产品族，而系统只消费其中某一族的产品。
如何解决：在一个产品族里面，定义多个产品。
关键代码：在一个工厂里聚合多个同类产品。
应用实例：工作了，为了参加一些聚会，肯定有两套或多套衣服吧，比如说有商务装（成套，一系列具体产品）、时尚装（成套，一系列具体产品），甚至对于一个家庭来说，可能有商务女装、商务男装、时尚女装、时尚男装，这些也都是成套的，即一系列具体产品。假设一种情况（现实中是不存在的，要不然，没法进入共产主义了，但有利于说明抽象工厂模式），在您的家中，某一个衣柜（具体工厂）只能存放某一种这样的衣服（成套，一系列具体产品），每次拿这种成套的衣服时也自然要从这个衣柜中取出了。用 OOP 的思想去理解，所有的衣柜（具体工厂）都是衣柜类的（抽象工厂）某一个，而每一件成套的衣服又包括具体的上衣（某一具体产品），裤子（某一具体产品），这些具体的上衣其实也都是上衣（抽象产品），具体的裤子也都是裤子（另一个抽象产品）。
优点：当一个产品族中的多个对象被设计成一起工作时，它能保证客户端始终只使用同一个产品族中的对象。
缺点：产品族扩展非常困难，要增加一个系列的某一产品，既要在抽象的 Creator 里加代码，又要在具体的里面加代码。
使用场景： 1、QQ 换皮肤，一整套一起换。 2、生成不同操作系统的程序。
注意事项：产品族难扩展，产品等级易扩展。
"""
import abc
import typing


class BaseInteractor(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @abc.abstractmethod
    def interact_with(self, obstacle):
        """交互"""


class BaseObstacle(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def action(self):
        """动作"""


class BaseWorld(metaclass=abc.ABCMeta):
    def __init__(self, name):
        print(self)
        self.player_name = name

    @abc.abstractmethod
    def make_character(self) -> BaseInteractor:
        """制作角色"""

    @abc.abstractmethod
    def make_obstacle(self) -> BaseObstacle:
        """制作障碍物"""


class Frog(BaseInteractor):

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))


class Bug(BaseObstacle):
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld(BaseWorld):

    def __str__(self):
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard(BaseInteractor):

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))


class Ork(BaseObstacle):
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld(BaseWorld):

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    def __init__(self, factory: BaseWorld):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name) -> typing.Tuple[bool, int]:
    age = input('Welcome {}. How old are you? '.format(name))
    try:
        age = int(age)
    except ValueError:
        print("Age {} is invalid, please try again...".format(age))
        return False, age
    return True, age


def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
