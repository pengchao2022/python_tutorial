#python for 循环使用 continue 跳过

credit_card_number = "1324-9089-5698-6654"
for x in credit_card_number:
    if x == '8':
        #遇到8之后，会跳过8 ，不输出8 但是整个循环继续执行
        continue
    else:
        print(x)