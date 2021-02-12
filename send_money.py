# -*- coding: utf-8 -*-

# 发工资

from money import saved_money


def send(salary):

    global saved_money
    saved_money += salary
    if saved_money > 1000:
        print(f"工资发啦")
    else:
        print("工资没发")
    return
