# python中字符串的格式化

price_1 = 3.4582
price_2 = -88.65456
price_3 = -18.99866

# 统一小数点后保留2位小数
print(f"价格 1 为 {price_1:.2f}\n"
      f"价格 2 为 {price_2:.2f}\n"
      f"价格 3 为 {price_3:.2f}")

# 体现出正负号
print(f"价格 1 为 {price_1:+.2f}\n"
      f"价格 2 为 {price_2:+.2f}\n"
      f"价格 3 为 {price_3:+.2f}")

#统一向右对齐
print(f"价格 1 为 {price_1:10.2f}\n"
      f"价格 2 为 {price_2:10.2f}\n"
      f"价格 3 为 {price_3:10.2f}")

#统一向左对齐 加<
print(f"价格 1 为 {price_1:<10.2f}\n"
      f"价格 2 为 {price_2:<10.2f}\n"
      f"价格 3 为 {price_3:<10.2f}")

#统一居中对齐 加^
print(f"价格 1 为 {price_1:^10.2f}\n"
      f"价格 2 为 {price_2:^10.2f}\n"
      f"价格 3 为 {price_3:^10.2f}")

#混合不同符号对齐
print(f"价格 1 为 {price_1:>+.2f}\n"
      f"价格 2 为 {price_2:>+.2f}\n"
      f"价格 3 为 {price_3:>+.2f}")

