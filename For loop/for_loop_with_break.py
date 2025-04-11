#python for 循环使用 Break中断

credit_card_number = "1324-8978-9067-7745"
for x in credit_card_number:
    if x == '6':
        break # 当x 值为6 时候，不会输出6 ，然后后面的也不会再输出，循环中断
    else:
         print(x)
    