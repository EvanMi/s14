# -*- coding:utf-8 -*-
# Author: Evan Mi
# "xx".isdigit()判断是否为整数

total_fee = int(input("enter your wage : "))
pro_lst = [["iphone", 6000], ["computer", 3999], ["bike", 500]]
bought_lst = []

"""
for index, item in enumerate(pro_lst):
    print(index, item)
"""

if total_fee <= 0:
    print("fuck off , you poverty")
else:
    for lst in pro_lst:
        print(pro_lst.index(lst)+1, lst[0], "\t", lst[1])
    buy_order = input("enter the number of product you want to buy : ")
    while total_fee >= 0:
        if buy_order == 'q' or total_fee == 0:
            print("-------------------------------------------")
            print("your balance is : ", total_fee)
            print("-------------------------------------------")
            print("you have bought the products below:")
            for item in bought_lst:
                print(item[0], "\t", item[1])
            break
        elif int(buy_order) < 1 or int(buy_order) > len(pro_lst):
            print("no such product")
            for lst in pro_lst:
                print(pro_lst.index(lst)+1, lst[0], "\t", lst[1])
            buy_order = input("enter the number of product you want to buy : ")
        elif pro_lst[int(buy_order)-1][1] > total_fee:
            print("you don't have enough money!")
            print("your balance is : ", total_fee)
            for lst in pro_lst:
                print(pro_lst.index(lst)+1, lst[0], "\t", lst[1])
            buy_order = input("enter the number of product you want to buy : ")
        else:
            total_fee = total_fee - pro_lst[int(buy_order)-1][1]
            bought_lst.append(pro_lst[int(buy_order)-1])
            for lst in pro_lst:
                print(pro_lst.index(lst)+1, lst[0], "\t", lst[1])
            print("your balance is : ", total_fee)
            if total_fee != 0:
                buy_order = input("enter the number of product you want to buy : ")
