# 复利计算器实例

amount = 0
while amount <= 0:
    amount = float(input("请在此输入您的本金金额:"))
    if amount <= 0:
        print("本金金额不能小于或等于0")
#print(amount)

rate = 0
while rate <= 0:
    rate = float(input("请在此输入您的利率："))
    if rate <= 0:
        print("利率不能小于或等于0")
#print(rate)

time = 0

while time <= 0:
    time = int(input("请在此输入您的年限："))
    if time <= 0:
        print("年限不能小于或等于零！")

#print(time)

print(f"金额：{amount}")
print(f"利率：{rate}")
print(f"年限：{time}")

total = amount*(1 + (rate / 100)) ** time

print(f"您总共获得的金额为：{total}")