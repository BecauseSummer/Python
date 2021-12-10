# –*–coding:utf-8 –*–
# 2021-11-12 10:12
# 定义展示菜单的函数
import datetime
Milk_tea_list = []
milk_tea_dict = {1:"香蕉冰奶茶", 2:"西瓜冰奶茶",3:"橙子冰奶茶",4:"绵绵冰奶茶",5:"苹果冰奶茶"}
# 获取当前系统的时间，用于追加到milk_tea_list 列表中去
buy_time = datetime.datetime.now().strftime('%m-%d %T')
def show_menu():
    '''展示菜单'''
    print("*" * 50)
    print("欢迎使用【小星星自助点吧系统】 V 1.0")
    print("1. 点购奶茶")
    print("2. 显示已购奶茶")
    print("0. 退出系统")
    print("*" * 50)

def milk_tea_list():
    print("目前在售奶茶:\n""1. 香蕉冰奶茶","\t2. 西瓜冰奶茶","\t3. 橙子冰奶茶",
            "\t4. 绵绵冰奶茶","\t5. 苹果冰奶茶")

def buy_milk_tea():
    '''自购奶茶逻辑处理'''
    print("您选择的是业务是购买奶茶.")
    milk_tea_list()
    #  使用 try...except 处理输入非数字时出现的异常
    try:
        milk_tea_number = int(input("请选择您要购买的奶茶,您直接输入编号："))
        if milk_tea_number == 1:
            prices = 3 #单价
            print("您选择的是 {}".format(milk_tea_dict[1]),"单价 {} 元".format(prices))
        elif milk_tea_number == 2:
            prices = 5
            print("您选择的是【{}】".format(milk_tea_dict[2]), "单价 {} 元".format(prices))
        elif milk_tea_number == 3:
            prices = 7
            print("您选择的是【{}】".format(milk_tea_dict[3]),"单价 {} 元".format(prices))
        elif milk_tea_number == 4:
            prices = 9
            print("您选择的是【{}】".format(milk_tea_dict[4]), "单价 {} 元".format(prices))
        elif milk_tea_number == 5:
            prices = 11
            print("您选择的是【{}】".format(milk_tea_dict[5]), "单价 {} 元".format(prices))
        else:
            tips =print('oh~我们只售卖以上五种奶茶哦！新口味敬请期待！')
            return tips
        milk_tea_cup = int(input("您要多少杯呢？"))
        if milk_tea_cup != 0:
            money =  prices * milk_tea_cup
            print('您需要支付 {} 元'.format(money))
            # 判断是否有VIP会员，如果有，将享受9.5折优惠
            is_vip = input("您有会员卡吗？不区分大小写。")
            if is_vip == "Y" or is_vip == "y" or is_vip == '是':
                money *= 0.95
                print("折后价是：{:.2f} 元".format( float(money)), "谢谢惠顾~")
            else:
                print('您没有优惠,您需要支付 {:.2f} 元'.format(float(money)))
            pay_money = float(input("请输入付款金额："))
            if pay_money == money :
                print("已成功付款")
                Milk_tea_list.append((milk_tea_dict[milk_tea_number], buy_time))
            elif pay_money < money:
                print("请重新选择付款金额")
            elif pay_money > money :
                ret_money = pay_money - money
                print("找您 {:.2f} 元".format(float(ret_money)))
                Milk_tea_list.append([milk_tea_dict[milk_tea_number],buy_time])
        else:
            tips = print("您至少需要选择一杯奶茶及以上哦~")
            return tips
    except ValueError:
        print("输入有误,请重新输入...")

def show_milk_tea():
    '''
    显示已购买的奶茶;
    多次购买后，尾部进行追加已购买的奶茶
    '''
    if not Milk_tea_list:
        tips = print("已购奶茶为空，请先购买.")
        return tips
    print('-' * 50)
    for name in ["已购奶茶", "购买时间"]:
        print(name, end='\t\t')
    for items in Milk_tea_list:
        print("")
        print(items)
    print('-' * 50)

def  bys_system():
    '''
    return: 关闭程序函数
    '''
    print("感谢您使用【小星星自助点餐系统】,期待您下次使用~")
    exit() # 使用exit函数结束程序
