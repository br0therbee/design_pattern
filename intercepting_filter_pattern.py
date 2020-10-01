# -*- coding: utf-8 -*-
# @Author      : BrotherBe
# @Time        : 2020-05-26 16:20
# @Version     : Python 3.6.8
"""
拦截过滤器模式
拦截过滤器模式（Intercepting Filter Pattern）用于对应用程序的请求或响应做一些预处理/后处理。定义过滤器，并在把请求传给实际目标应用程序之前应用在请求上。过滤器可以做认证/授权/记录日志，或者跟踪请求，然后把请求传给相应的处理程序。以下是这种设计模式的实体。
过滤器（Filter） - 过滤器在请求处理程序执行请求之前或之后，执行某些任务。
过滤器链（Filter Chain） - 过滤器链带有多个过滤器，并在 Target 上按照定义的顺序执行这些过滤器。
Target - Target 对象是请求处理程序。
过滤管理器（Filter Manager） - 过滤管理器管理过滤器和过滤器链。
客户端（Client） - Client 是向 Target 对象发送请求的对象。

实现
我们将创建 FilterChain、FilterManager、Target、Client 作为表示实体的各种对象。AuthenticationFilter 和 DebugFilter 表示实体过滤器。
InterceptingFilterDemo，我们的演示类使用 Client 来演示拦截过滤器设计模式。
"""
import abc
import typing


class Filter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, request: str):
        """执行"""


class AuthenticationFilter(Filter):
    def execute(self, request: str):
        print(f"Authenticating request: {request}")


class DebugFilter(Filter):
    def execute(self, request: str):
        print(f"Debug request: {request}")


class Target(object):
    @staticmethod
    def execute(request: str):
        print(f"Executing request: {request}")


class FilterChain(object):
    filters: typing.List[Filter] = []
    target = None

    def add_filter(self, filters: Filter):
        self.filters.append(filters)

    def execute(self, request: str):
        for f in self.filters:
            f.execute(request)
        self.target.execute(request)

    def set_target(self, target: Target):
        self.target = target


class FilterManager(object):
    def __init__(self, target: Target):
        self.filter_chain = FilterChain()
        self.filter_chain.set_target(target)

    def set_filter(self, filters: Filter):
        self.filter_chain.add_filter(filters)

    def filter_request(self, request: str):
        self.filter_chain.execute(request)


class Client(object):
    filter_manager = None

    def set_filter_manager(self, filter_manager: FilterManager):
        self.filter_manager = filter_manager

    def send_request(self, request: str):
        self.filter_manager.filter_request(request)


if __name__ == '__main__':
    manager = FilterManager(Target())
    manager.set_filter(AuthenticationFilter())
    manager.set_filter(DebugFilter())

    client = Client()
    client.set_filter_manager(manager)
    client.send_request('HOME')
