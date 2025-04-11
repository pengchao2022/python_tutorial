#购物车物品的输入与计算

item = input("您想购买什么物品呢？")
price = float(input("单价为："))
quantity = int(input("您要购买几个呢：？"))

total = price * quantity
print(f"您要购买的物品是：{item},每个单价为：{price},您说要买：{quantity}个，需要支付的钱数为：{total}")

