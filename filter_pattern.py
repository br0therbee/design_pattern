# -*- coding: utf-8 -*-
# @Author      : BrotherBe
# @Time        : 2020-05-20 17:02
# @Version     : Python 3.6.8
"""
过滤器模式
过滤器模式（Filter Pattern）或标准模式（Criteria Pattern）是一种设计模式，这种模式允许开发人员使用不同的标准来过滤一组对象，通过逻辑运算以解耦的方式把它们连接起来。这种类型的设计模式属于结构型模式，它结合多个标准来获得单一标准。

实现
我们将创建一个 Person 对象、Criteria 接口和实现了该接口的实体类，来过滤 Person 对象的列表。CriteriaPatternDemo，我们的演示类使用 Criteria 对象，基于各种标准和它们的结合来过滤 Person 对象的列表。
"""
import abc

import typing


class Person(object):
    def __init__(self, name: str, gender: str, marital_status: str):
        self._name = name
        self._gender = gender
        self._marital_status = marital_status

    @property
    def name(self):
        return self._name

    @property
    def gender(self):
        return self._gender

    @property
    def marital_status(self):
        return self._marital_status

    def __str__(self):
        return f'Person: [Name: {self.name}, Gender: {self.gender}, Marital Status: {self.marital_status}]'


class Criteria(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def meet(self, persons: typing.List[Person]) -> typing.List[Person]:
        """符合标准"""


class CriteriaMale(Criteria):
    def meet(self, persons: typing.List[Person]):
        male_persons = []
        for person in persons:
            if person.gender == 'Male':
                male_persons.append(person)
        return male_persons


class CriteriaFemale(Criteria):
    def meet(self, persons: typing.List[Person]):
        female_persons = []
        for person in persons:
            if person.gender == 'Female':
                female_persons.append(person)
        return female_persons


class CriteriaSingle(Criteria):
    def meet(self, persons: typing.List[Person]):
        single_persons = []
        for person in persons:
            if person.marital_status == 'Single':
                single_persons.append(person)
        return single_persons


class AndCriteria(Criteria):
    def __init__(self, criteria: Criteria, other_criteria: Criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def meet(self, persons: typing.List[Person]):
        first_criteria_persons = self.criteria.meet(persons)
        return self.other_criteria.meet(first_criteria_persons)


class OrCriteria(Criteria):
    def __init__(self, criteria: Criteria, other_criteria: Criteria):
        self.criteria = criteria
        self.other_criteria = other_criteria

    def meet(self, persons: typing.List[Person]):
        first_criteria_persons = self.criteria.meet(persons)
        other_criteria_persons = self.other_criteria.meet(persons)
        for person in other_criteria_persons:
            if person not in first_criteria_persons:
                first_criteria_persons.append(person)
        return first_criteria_persons


if __name__ == '__main__':
    def print_persons(persons):
        prints = []
        for person in persons:
            prints.append(str(person))
        prints = '\n' + '\n'.join(prints) + '\n'
        return prints


    person_list = [
        Person("Robert", "Male", "Single"),
        Person("John", "Male", "Married"),
        Person("Laura", "Female", "Married"),
        Person("Diana", "Female", "Single"),
        Person("Mike", "Male", "Single"),
        Person("Bobby", "Male", "Single")
    ]
    males = CriteriaMale()
    females = CriteriaFemale()
    singles = CriteriaSingle()
    single_males = AndCriteria(singles, males)
    single_or_females = OrCriteria(singles, females)
    print(f'Males: {print_persons(males.meet(person_list))}')
    print(f'Females: {print_persons(females.meet(person_list))}')
    print(f'Singles: {print_persons(singles.meet(person_list))}')
    print(f'Single Males: {print_persons(single_males.meet(person_list))}')
    print(f'Single Or Females: {print_persons(single_or_females.meet(person_list))}')
