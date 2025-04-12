# python 中的过滤函数练习

#创建一个列表 list ，列表中有元组tuple

friends = [
    ("郭靖", 28),
    ("黄蓉", 20),
    ("欧阳锋", 50),
    ("黄老邪", 54),
    ("老顽童", 52)
]
age_filter = lambda data: data[1] >= 30

can_drink_friends = list(filter(age_filter, friends))

for friend in can_drink_friends:
    print(friend[0])
    print(friend[1])



