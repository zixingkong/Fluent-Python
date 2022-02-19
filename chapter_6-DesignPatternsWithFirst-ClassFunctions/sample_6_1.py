# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_6.1
   Description : 设计模式：策略模式
                定义一系列算法，把它们一一封装起来，并且使它们可以相互替换。本模式使得算法可以独立于使用它的客户而变化
                上下文
                    把一些计算委托给实现不同算法的可互换组件，它提供服务。在这个电商示例中，上下
                    文是 Order，它会根据不同的算法计算促销折扣。
                策略
                    实现不同算法的组件共同的接口。在这个示例中，名为 Promotion 的抽象类扮演这个角
                    色。
                具体策略
                    “策略”的具体子类。 fidelityPromo、 BulkPromo 和 LargeOrderPromo 是这里实现的三个
                    具体策略
   date：          2022/2/13
-------------------------------------------------
"""
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    """订单类"""

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        """返回折扣金额"""


class FidelityPromo(Promotion):
    """为积分为1000或以上的顾客提供5%折扣"""

    def discount(self, order):
        return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    """单个商品为20个或以上时提供10%折扣"""

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):
    """订单中的不同商品达到10个或以上时提供7%折扣"""

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .7
        return 0


if __name__ == '__main__':
    joe = Customer('John Doe', 0)  # ➊
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),  # ➋
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    print(Order(joe, cart, FidelityPromo()))  # ➌
    print(Order(ann, cart, FidelityPromo()))  # ➍
    banana_cart = [LineItem('banana', 30, .5),  # ➎
                   LineItem('apple', 10, 1.5)]
    print(Order(joe, banana_cart, BulkItemPromo()))  # ➏
    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    print(Order(joe, long_order, LargeOrderPromo()))  # ➑
    print(Order(joe, cart, LargeOrderPromo()))
