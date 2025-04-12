#Python复制文件练习

#copyfile --- 只能复制文件的内容，不会复制文件什么时候建立的等信息属性
#copy ----  只复制文件的内容，也可以复制目录
#copy2 ---- 不仅可以复制文件的内容，还可以复制文件其他属性，比如创建时间，文件的权限等

# 导入 shutil 模版


import shutil

#文件所在位置用str 代替
source_str = "/Users/pengchaoma/terraform/" # 文件所处的目录
desti_str = "/Users/pengchaoma/vs" # 要复制到的目录

source = f"{source_str}/variable.tf"

#复制后重新命名的文件
destination = f"{desti_str}/v1.tf"

shutil.copyfile(source, destination)

