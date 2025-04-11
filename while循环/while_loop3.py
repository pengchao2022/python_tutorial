#While 循环练习3

num = int(input("请输入1 到 10 之间的数字："))
while num < 1 or num > 10:
    print(f"您输入的数字{num}是无效的！")
    num = int(input("请输入1 到 10 之间的数字："))
print(f"您输入了{num}.")


