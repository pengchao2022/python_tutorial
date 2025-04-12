#python 删除非空文件夹

import os
import shutil



path = "/Users/pengchaoma/vs"

shutil.rmtree(f"{path}/non_empty")

