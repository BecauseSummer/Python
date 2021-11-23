# –*–coding:utf-8 –*–
# 2021-10-25 17:43
'''
定义布尔型变量 has_ticket 表示是否有车票
定义整形变量 knife_lenght 表示刀的长度，单位：厘米
首先检查是否有车票，如果有允许进行安检
安检时，需要检查刀的长度，大于20厘米，不能通过安检
没有车票，不允许进门
'''
Allowable_knife_length = 20
try:
    # 使用try...except 捕获异常
    has_ticket = int(input("请选择是否已经购票.提示：1为表示已经购票，0则为没有购票。")) #  0 为没有购买车票，1为已经购买
    if has_ticket == 1:
        print("车票检查检查通过，准备开始安检...")
        winth_knife = int(input("是否带刀具？提示：1为表示带刀具，其他数字则为没有带刀具。"""))
        if winth_knife == 1:
            try:
                knife_lenght = float(input("请输入带刀长度："))
                if knife_lenght >= Allowable_knife_length :
                    lenght = knife_lenght - Allowable_knife_length
                    print("超出长度 %d cm."%lenght,end=" ""有 %d cm 长,不能带上车!"%knife_lenght)
                    #print()
                elif winth_knife == 0:
                    print("安检通过，谢谢您的配合，请您准备开始登车。")
            except ValueError:
                print("输入有误，请重新输入...")
            else:
                print("安检通过，谢谢您的配合，请您准备开始登车。")
    elif has_ticket == 0:
        print("没有车票，不允许进门...")
    else:
        print("请重新输入数字“0” 或者 “1”  0代表没有购票，1代表已经购票，请正确输入！")
except ValueError:
    print("必须为数字整数""0或1 0代表没有购票，1代表已经购票，请正确输入！")