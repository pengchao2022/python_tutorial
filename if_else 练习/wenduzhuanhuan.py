# Python 温度转换程序

unit = input("请在此输入您当前的温度单位：摄氏 C，华氏 F :------->").upper()
#print("\n")
temp = float(input("请在此输入当前的温度："))

if unit == 'C':
#摄氏转换为华氏
    temp = round(9 * temp / 5 + 32)
    print(f"当前的温度为：{temp}F")
elif unit == 'F':
#华氏转换为摄氏
    temp = round((temp - 32) * 5 / 9)
    print(f"当前的温度为：{temp}C")
else:
    print("单位不正确！")



