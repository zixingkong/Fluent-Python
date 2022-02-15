# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_7.3
   Description :
   date：          2022/2/14
-------------------------------------------------
"""

promos = []  # ➊


def promotion(promo_func):  # ➋
    promos.append(promo_func)
    return promo_func


@promotion  # ➌
def fidelity(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):  # ➍
    """选择可用的最佳折扣
    """
    return max(promo(order) for promo in promos)
