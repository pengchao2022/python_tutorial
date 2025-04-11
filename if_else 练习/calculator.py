#计算机 一个简单的计算器程序

operator = input("请输入运算符：(加法：+, 减法：-, 乘法：*, 除法：/, 取余：%)\n")
num1 = float(input("请输入index第一个数字："))
num2 = float(input("请输入您的第二个数字："))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
elif operator == '%':
    result = num1 % num2
else:
    print("运算符号输入有误！")
print(f"运算结果是：{result}")
print(f"运算结果以整数的方式输出：{round(result)}")

