# 验证使用者输入的合法性

#使用者名称不能超过12 个字符
username = input("请在此输入您的名称:")

if len(username) > 12:
    print("使用者名称不可以超过12个字符！")

elif " " in username:
    print("使用者名称不可以包含有空格！")

#isalpha 方法来判断用户名中是否全为字母
elif not username.isalpha():
    print("用户名中不能包含数字!")
    
else:
    print("欢迎  " + username)
    