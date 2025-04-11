# python 列表练习

fruits = ["苹果", "香蕉", "猕猴桃", "西瓜", "橘子", "菠萝"]

#打印出列表里的指定元素
print(fruits[0])
print(fruits[1])

#打印处列表里的素有元素 使用for loop
for f in fruits:
    print(f)

#使用append 向列表里添加元素
fruits.append("梨瓜")
print(fruits)

#使用remove 在列表里移除元素 
fruits.remove("香蕉")
print(fruits)

#使用index 来获得列表元素的索引
print(fruits.index("猕猴桃"))
print(fruits.index("梨瓜"))

#列表的特性是可以允许有相同的元素，比如，已经有了梨瓜，还可以再添加梨瓜
fruits.append("梨瓜")
fruits.append("梨瓜")
print(fruits)

#使用count 方法来统计列表里面元素出现的个数
print(fruits.count("梨瓜"))
print(fruits.count("苹果"))
print(fruits.count("香蕉"))
print(fruits.count("猕猴桃"))

#使用reverse 方法来反转列表
print(fruits)
fruits.reverse()
print(fruits)