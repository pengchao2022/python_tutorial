#python 写入文件

str = "/Users/pengchaoma/terraform/variable.tf"

text = "hello\n, 今天天气很好！"

with open(str, 'w') as file:
    file.write(text)


with open(str) as file:
    print(file.read())