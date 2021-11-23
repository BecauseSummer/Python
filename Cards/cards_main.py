# –*–coding:utf-8 –*–
# 2021-10-26 17:11
import sys

import card_tools
while True:
    # 使用一个变量来存放用户输入的内容。
    card_tools.show_menu()
    try:
        action_int = int(input("请选择希望执行的操作："))

        # 判断用户输入是否为1,2,3,0
        if action_int in [1, 2, 3]:
            if action_int == 1:
                card_tools.create_card()
            elif action_int == 2:
                card_tools.show_card()
            elif action_int == 3:
                card_tools.search_card()

        elif action_int in [0]:
            print("感谢您的使用，再见~")
            sys.exit()
        else:
            print("请正确选择功能")

    except ValueError:
        print("请输入数字整数~")
        sys.exit()


