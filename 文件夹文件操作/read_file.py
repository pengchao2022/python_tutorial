#python 读取文件内容

str = "/Users/pengchaoma/terraform/main.tf"

try: #异常处理
    with open(str) as file:
        print(file.read())
except FileNotFoundError:
    print("文件并不存在！")