#python 字符串索引练习

credit_card_number = "1234-5678-8976-4537"

#索引是从0开始计算的
first_char = credit_card_number[0]

print(f"第一个号码是：{first_char}")

second_char = credit_card_number[1]

print(f"第二个号码是：{second_char}")

#索引前4位数字，从0开始，到4 结束， 0 1 2 3 ， 4 不包含在内
first_four_char = credit_card_number[0:4]

print(f"卡号的1到4 位数字是:{first_four_char}")

#提取卡号最后一位数字，用-1 来取得
last_one = credit_card_number[-1]

print(f"卡号的最后一位数字是：{last_one}")

#提取卡号倒数第二个数字，用-2 来取得
last_second_one = credit_card_number[-2]

print(f"卡号的倒数第二个数字是{last_second_one}")