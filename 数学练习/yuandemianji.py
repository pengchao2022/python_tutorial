# 利用数学函数math 来计算圆的面积

import math

b = math.pi
r = float(input("请在此输入圆的半径："))
area = 2 * b * pow(r,2)

print(f"圆的精确面积为：{area}")

print(f"圆的面积在四舍五入后为：{round(area,2)}")

