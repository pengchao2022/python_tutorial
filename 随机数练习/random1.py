#python random 模块练习

import random

#查看random 函数的使用方法可以使用help
#help(random)
#randint() 指定a到b 之间的整数 
print(random.randint(1,10))

#random()方法可以生成0到1 之间的一个浮点数
print(random.random())

#在列表中随机选择一个元素
options = ["剪刀", "石头", "布"]
rand_option = random.choice(options)
print("电脑选择的是:", rand_option)

#将一个列表打乱
cards = ["2", "3", "4", "5", "6", "7", "8", "9"]
random.shuffle(cards)
print(cards)