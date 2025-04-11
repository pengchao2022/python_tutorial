#使用字典完成菜单和项目

menu = {
    "披萨": 300,
    "爆米花": 50,
    "可口可乐": 6,
    "百事可乐": 8,
    "炸鸡": 120,
    "薯条": 66
}
print("菜单")
print("--------------------")

cart = []
total = 0

for item, price in menu.items():
    print(f"{item}: {price}")

while True:
    food = input("请输入一个菜单项目：(输入 q 结束：)")
    if food.lower() == 'q':
        break
    elif menu.get(food) is None:
        print("没有这个商品！")
    else:
        cart.append(food)
        total += menu.get(food)
        print(food, end=" ")
        
print(f"总金额：{total}")

