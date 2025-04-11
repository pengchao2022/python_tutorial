#python 中tuple 元组的使用

fruits_tuple = ("香蕉", "西瓜", "猕猴桃", "菠萝", "油桃", "西瓜")
#统计有几个西瓜
result = fruits_tuple.count("西瓜")
print(result)

#index 方法找到元素的位置
position = fruits_tuple.index("西瓜")
print(position)

#元组不允洗添加元素，测试下,会有报错，tuple 元组不允许添加元素！
fruits_tuple.add("马铃薯")
print(fruits_tuple)