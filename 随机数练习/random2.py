# random 猜数字游戏
import random

low = 1
high = 100

number = random.randint(low,high)
guesses = 0

while True:
    #让玩家来输入数字
    guess = int(input(f"请输入您猜测的在{low}到{high}之间的数字："))
    guesses += 1
    
    if guess < number:
        print("您猜的数字太小了")
    elif guess > number:
        print("您猜的数字太大了")
    else:
        print(f"恭喜你猜对了，这个数字就是:{number}")
        print(f"您总共猜了{guesses}次")
        break
    
