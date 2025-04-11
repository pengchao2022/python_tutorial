#python 做一个石头剪刀布游戏

import random
player = None
computer = None
running = True
options = ("剪刀", "石头", "布")

while running:
    player = input("请输入石头，剪刀，布：")
    while player not in options:
        input("输入错误，请输入石头，剪刀，布：")
    computer = random.choice(options)
    print(f"玩家:{player},电脑：{computer}")
    if player == computer:
        print("平局")
    elif player == "剪刀" and computer == "布":
        print("玩家赢！")
    elif player == "布" and computer == "石头":
        print("玩家赢！")
    elif player == "石头" and computer == "剪刀":
        print("玩家赢!")
    else:
        print("电脑赢")
    play_agin = input("再玩一局？(y/n)").lower()
    if not play_agin == 'y':
        running = False

print("感谢来玩这个游戏！")