# 计算字符串的函数

name = "allen Ma I love python 我爱python"

length = len(name)

print(f"您的字符串共有{length}个字符")

#找到第一个空格
space_pos = name.find(" ")
print(f"第一个空格出现在第{space_pos}个字后面")

#让第一个字母变为大写
name_capitalized = name.capitalize()
print(f"您的全名(第一个字母大写):{name_capitalized}")

#让你的名字全部大写
name_upper = name.upper()
print(f"您的全部大写的名字为:{name_upper}")

#让你的名字全部小写
name_lower = name.lower()
print(f"您的全部小写的名字为：{name_lower}")

#count 方法的使用
phone_numebr = input("请在此输入你的电话号码：")
dash_count = phone_numebr.count("-")
print(f"您的电话号码中有{dash_count}个短横线")

#replace 方法的使用
#电话号码中短横线- 替换为空格

phone_numebr = phone_numebr.replace("-"," ")
print(f"取掉短横线-后您的电话号码为：{phone_numebr}")

