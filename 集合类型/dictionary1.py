#python 字典练习

#python 字典是 键 ==》值 对应, 具有顺序性 和可变性，不允许有重复的键
# key:value 

capital = {
    "US": "Washington",
    "China": "Beijing",
    "Japan": "Tokyo",
    "France": "Paris",
    "UK": "landon"

}
#get 取得键值对
print(capital.get("Japan"))
print(capital.get("US"))
print(capital.get("UK"))

#update 更新键值对
capital.update({"Germany": "berlin"})
print(capital)

#pop()删除键值对
capital.pop("US")
print(capital)

#values()获得所有值
print(capital.values())

#items()获得所有键值对
print(capital.items())