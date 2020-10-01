# -*- coding: utf-8 -*-
# @Author      : BrotherBe
# @Time        : 2020-05-26 14:23
# @Version     : Python 3.6.8
"""
业务代表模式
业务代表模式（Business Delegate Pattern）用于对表示层和业务层解耦。它基本上是用来减少通信或对表示层代码中的业务层代码的远程查询功能。在业务层中我们有以下实体。
客户端（Client） - 表示层代码可以是 JSP、servlet 或 UI java 代码。
业务代表（Business Delegate） - 一个为客户端实体提供的入口类，它提供了对业务服务方法的访问。
查询服务（LookUp Service） - 查找服务对象负责获取相关的业务实现，并提供业务对象对业务代表对象的访问。
业务服务（Business Service） - 业务服务接口。实现了该业务服务的实体类，提供了实际的业务实现逻辑。

实现
我们将创建 Client、BusinessDelegate、BusinessService、LookUpService、JMSService 和 EJBService 来表示业务代表模式中的各种实体。
BusinessDelegatePatternDemo，我们的演示类使用 BusinessDelegate 和 Client 来演示业务代表模式的用法。
"""
import abc


class BusinessService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_processing(self):
        """处理"""


class EJBService(BusinessService):
    def do_processing(self):
        print("Processing task by invoking EJB Service")


class JMSService(BusinessService):
    def do_processing(self):
        print("Processing task by invoking JMS Service")


class BusinessLookup(object):
    def get_business_service(self, service_type: str):
        if service_type == 'EJB':
            return EJBService()
        else:
            return JMSService()


class BusinessDelegate(object):
    business_lookup = BusinessLookup()
    business_service = None
    service_type = None

    def set_service_type(self, service_type):
        self.service_type = service_type

    def do_task(self):
        self.business_service = self.business_lookup.get_business_service(self.service_type)
        self.business_service.do_processing()


class Client(object):
    def __init__(self, business_service: BusinessDelegate):
        self.business_service = business_service

    def do_task(self):
        self.business_service.do_task()


if __name__ == '__main__':
    business_delegate = BusinessDelegate()
    business_delegate.set_service_type('EJB')
    client = Client(business_delegate)
    client.do_task()
    business_delegate.set_service_type('JMS')
    client.do_task()
