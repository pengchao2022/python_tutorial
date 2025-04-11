# 倒计时加入秒数

import time

my_time = int(input("请在此输入您的秒数："))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = x // 60 % 60 #//运算符代表整数除法（或称为地板除法），它会返回除法运算后的整数部分，忽略小数点后的所有位数‌‌

    print(f"{minutes:02}:{seconds:02}")
    time.sleep(1)
print("时间到了！")