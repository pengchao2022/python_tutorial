# python 编写倒数计时器

import time
my_time = int(input("请在此输入您要的秒数："))
for x in range(my_time):
    print(x)
    time.sleep(1)
print("时间到了！")