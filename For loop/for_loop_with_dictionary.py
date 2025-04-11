#python for 循环使用字典

#字典使用大括号，每一个元素对于key: value
dic01 = {"a":8, "b":10, "c":87, "d":45}
for x in dic01:
    print(x) #只能迭代出key, 无法迭代出value

my_dic = {"a":8, "b":10, "c":87, "d":45}
for key,value in my_dic.items():
    print("key:",key)
    print("value:",value)
    
