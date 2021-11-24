# –*–coding:utf-8 –*–
# 2021-11-12 10:11
from milk_tea_tools import *
'''
【小星星自助点吧系统】需求：
1. 实现用户可根据菜单选项选择所需奶茶;
2. 实现用户自行所购奶茶杯数;
3. 实现判断用户是否有会员卡享受优惠折扣;
4. 接收用户付款金额，找余等;
5. 实现用户可查询已购买的奶茶种类，购买时间等;

'''
while True:
    show_menu()
    try:
        business_number = int(input("请输入业务编号："))
        if business_number in [1, 2]:
            if business_number == 1:
                buy_milk_tea()
            elif business_number == 2:
                show_milk_tea()
        elif business_number in [0] :
            bys_system()
        else:
            print("请正确选择业务编号。")
    except ValueError:
        print('请正确选择业务编号。')