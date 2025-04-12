#练习使用python中的map 函数

#声明一个列表，里面都是元组tuple
store = [
    ("衬衫", 20),
    ("裤子", 40),
    ("球鞋", 120),
    ("帽子", 500)
]
to_euros = lambda data: (data[0], round(data[1]*0.82))
store_euros = list(map(to_euros, store))
print(store_euros)


to_usd = lambda data: (data[0], round(data[1]/30))
store_usds = list(map(to_usd, store))
print(store_usds)

for item in store_usds:
    print(item)

for item in store_euros:
    print(item)