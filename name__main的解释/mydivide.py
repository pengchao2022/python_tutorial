# 定义一个除法函数

def div (x, y):
    result = round((x / y))
    print(f"{x}除以{y}的结果是：{result}")

if __name__ == '__main__':    
    div(9, 3)
    div(9, 4)
