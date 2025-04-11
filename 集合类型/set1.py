#set 集合，set 没有顺序，不能重复

fruits_set = {"苹果", "香蕉", "西瓜"}
fruits_set.add("香蕉")
fruits_set.add("马铃薯")
for fruit in fruits_set:
    #print(fruit)

    #让输出结果不用换行，横着排列
    print(fruit, end=" ")

#判断元素有没有在set list 里面
if "香蕉" in fruits_set:
    print("有一个香蕉！")

if "梨瓜" in fruits_set:
    print("有一个梨瓜")
else:
    print("没有梨瓜！")
