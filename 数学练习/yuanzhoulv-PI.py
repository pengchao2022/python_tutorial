#使用数学函数math中的PI

import math
#打印出圆周率pi 的值检查下
#print(math.pi)

#计算圆的周长 2*pi*r

r = float(input("请输入圆的半径："))
b = math.pi
lena = 2 * b * r

print(f"圆的周长为：{lena}")

print(f"圆的周长在四舍五入后的值为：{round(lena,2)}")

