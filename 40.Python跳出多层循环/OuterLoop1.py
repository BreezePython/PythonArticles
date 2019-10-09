# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @Date     : 2019/9/11 0:03
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : OuterLoop.py
import random

people = ['zhang', 'me', 'li']
payments = ['AA', 'stand_treat']

# 为了避免一成不变的套路，我们添加两个列表随机
random.shuffle(payments)
print(payments)
random.shuffle(people)
print(people)

for payment in payments:
    for person in people:
        if payment == 'stand_treat':
            if person == 'me':
                print("居然我请客，赶紧尿遁...")
                people.remove('me')
                schlemiel = random.choice(people)
                print("倒霉孩子{}请客".format(schlemiel))
                # 当遇到我请客，直接结束外层循环，函数返回...
                break
            else:
                print("今天{}请客".format(person))
        else:
            print('今天吃饭{},等下{}付钱，大家记得把钱给它...'
                  .format(payment, person))
    else:
        # 未出现break操作，执行else，通过continue继续操作
        continue
    # 出现break操作，跳过else，直接外层break，结束外层循环
    break


# def dine_together():
#     # 为了避免一成不变的套路，我们添加两个列表随机
#     random.shuffle(payments)
#     print(payments)
#     random.shuffle(people)
#     print(people)
#
#     for payment in payments:
#         for person in people:
#             if payment == 'stand_treat':
#                 if person == 'me':
#                     print("居然我请客，赶紧尿遁...")
#                     people.remove('me')
#                     schlemiel = random.choice(people)
#                     print("倒霉孩子{}请客".format(schlemiel))
#                     # 当遇到我请客，直接结束外层循环，函数返回...
#                     return
#                 else:
#                     print("今天{}请客".format(person))
#             else:
#                 print('今天吃饭{},等下{}付钱，大家记得把钱给它...'
#                       .format(payment, person))
#
#
# dine_together()
