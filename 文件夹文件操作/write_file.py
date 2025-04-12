#python 写入文件

str = "/Users/pengchaoma/terraform/variable.tf"

text = "hello\n, 今天天气很好！"

#内容写入文件
with open(str, 'w') as file:
    file.write(text)

#插入文字内容
with open(str, 'a') as file:
    file.write('\n Allen Ma 2025\n')

#读取文件内容并打印
with open(str) as file:
    print(file.read())