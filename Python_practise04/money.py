# -*- coding: utf-8 -*-

'''
原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额
'''

class Money:
    saved_money = 1000
    def __init__(self):
        print(self.saved_money)

    def send(self):
        self.saved_money += self.salary

    def select(self):

        print(f"我的工资发了: {salary}")
        print(f"我的最终存款是: {saved_money}")

if __name__ == '__main__':
    send()
    select()