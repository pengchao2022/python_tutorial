# 练习使用list, set, tuple

goods = [] #列表list

prices = [] #列表

#循环执行
while True:
    good = input("请输入想要购买的物品：")
    if good.lower()== 'q':
        break

    price = float(input(f"请输入物品{good}的价格："))

    goods.append(good)
    prices.append(price)

print("商品列表：", goods)
print("价格列表：", prices)

for index, good in enumerate(goods):
    #print("索引 index:", index)
    #print("商品名称:", good)
     print(f"第{index + 1}商品是：{good}, 价格为:{prices[index]}")

total = sum(prices)

print(f"总价格为:￥{total}")