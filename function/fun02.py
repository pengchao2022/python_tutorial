#python 函数传递参数

def greeting(name):
    print(f"您好！ {name}")

greeting("allen")

# 定义加法函数
def add(x, y):
    return x + y

result = add(3, 5)
print(result)

#定义减法函数
def sub(x, y):
    return x - y
result = sub(5, 3)
print(result)

#定义乘法函数

def plus(x, y):
    return x * y
result = plus(5, 3)
print(result)

#定义除法函数

def div(x, y):
    return x / y
result = div(9, 3)
print(result)

#定义取余函数
def yushu(x, y):
    return x % y
result = yushu(9, 4)
print(result)

#定义除法取整函数
def quzheng(x, y):
    return x // y
result = quzheng(46, 3)
print(result)

#定义创建名字函数

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
print(create_name('allen', 'ma'))




