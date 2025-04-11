import os

str = "/Users/pengchaoma/terraform"

#对于windows 系统,str 需要加r 
#str = r"/Users/pengchaoma/terraform"


if os.path.exists(str):
    print("文件夹存在！")

else:
    print("文件夹不存在！")

