#Email 字符串分析

email = "pengchao.ma6666@gmail.com"

#先找到@的位置
index = email.index("@")

print(f"Email 中@所处的位置为：{index}")

#找到使用者的名称
username = email[0:index]
print(f"Email 中使用者的名称为：{username}")

#找到邮件中的域名
#index + 1 如果不加1 会包含@， index+1 后面不要跟任何参数，表示遍历到最后
domain = email[(index+1):]
print(f"Email 中的域名为：{domain}")

