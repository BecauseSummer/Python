# –*–coding:utf-8 –*–
# 2021-10-26 14:15
import random
the_finger_guessing_game = random.randint(1 , 3)
computer = random.randint(1, 3)
player = the_finger_guessing_game
print("玩家出的拳是：%d \n电脑出的拳是：%d" % (player, computer))

if player == 1 and computer == 2 :
    print("玩家胜利！")
elif player == 2 and computer == 3 :
    print("玩家胜利")
elif player == 3 and computer == 1 :
    print("玩家胜利！")
elif player == computer :
    print("打成平手！")

else :
    print("电脑胜利!")



