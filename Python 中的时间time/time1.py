#练习将时间格式化

import time

print(time.ctime(0))

print(time.time())

#取得当地的时间localtime()
local_time = time.localtime()
#print(local_time)

print("格式化的时间：", time.strftime("%Y-%m-%d %H:%M:%S", local_time))

