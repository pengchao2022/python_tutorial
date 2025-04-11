# Python 循环嵌套练习

rows = int(input("请在此输入您的行数："))
cols = int(input("请在此输入您的列数："))
symbol = str(input("请输入您的符号："))

for i in range(rows):
    for y in range(cols):
        print(symbol, end=" ")
    print()
    