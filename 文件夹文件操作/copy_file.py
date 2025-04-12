#Python复制文件练习

# 导入 shutil 模版

import shutil

#文件所在位置用str 代替
source_str = "/Users/pengchaoma/terraform/"
desti_str = "/Users/pengchaoma/vs"

source = f"{source_str}/variable.tf"
destination = f"{desti_str}/v1.tf"

shutil.copyfile(source, destination)

