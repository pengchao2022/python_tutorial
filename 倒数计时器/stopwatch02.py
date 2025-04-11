# python 实现倒计时
import time

my_time = int(input("请在此输入您的倒计时秒数："))
for x in range(my_time, 0, -1):
    print(x)
    time.sleep(1)
print("时间到了！")

