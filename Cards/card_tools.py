# –*–coding:utf-8 –*–
# 2021-10-26 17:39

card_list = [] # 记录所有名片字典
def show_menu():
    '''展示菜单'''
    print("*"* 50)
    print("欢迎使用【名片管理系统】 V 1.0")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片\n")
    print("0. 退出系统")
    print("*" * 50)

def create_card():
    '''创建名片'''
    print("创建名片信息：")
    # 名片信息

    user_name = input("请输入你的姓名：")
    phone_int = int(input("电话号码："))
    qq = int(input("qq号码："))
    email = input("邮箱：")

    card_dict = {"name":user_name, "phone":phone_int, "QQ":qq, "email":email}

    card_list.append(card_dict)
    # print(card_list)
    file = card_dict
    wire_file = open("./file/test.txt", 'w')
    for card_dict in file:
        wire_file.write(card_dict + "")
    print("write success!")
    wire_file.close()
    print("添加【%s】的名片成功！" %user_name)




def show_card():
    '''显示所有名片'''
    if not card_list:
        Tips = print("名片为空，请先使用名片添加功能！")
        return Tips

    print('-' * 50)
    print("显示所有名片：")
    for name in ["姓名", "手机号码", "QQ", "邮箱"] :
        print(name, end="\t\t")
    print("")
    print('-' * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
        card_dict["phone"], card_dict["QQ"], card_dict["email"]))

        # print(card_dict)
def search_card():
    '''查找已有名片'''
    if not card_list:
        tips = print("名片为空，请先使用名片添加功能！")
        return tips
    find_name = input("请输入你要查找的名片：")
    for card_dict in  card_list:
        if card_dict["name"] == find_name:
            for name in ["姓名", "手机号码", "QQ", "邮箱"] :
                print(name, end="\t\t")
                print("")
                print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"], card_dict["phone"], card_dict["QQ"], card_dict["email"]))
                del_card(card_dict)
        else:
            print("【%s】未找到！"%find_name)
        # TODO 找到的名片记录做修改和删除操作
        break
def del_card(find_dict):
    '''修改名片信息'''
    print(find_dict)
    action_int = input("请选择要执行的操作：【1】修改 【2】删除")
    if action_int == "1":
        print("修改名片：")
        find_dict['name'] = input_card_info(find_dict['name'],"姓名：")
        find_dict['phone'] = input_card_info(find_dict['phone'], "手机号码：")
        find_dict['QQ'] = input_card_info(find_dict['QQ'],"QQ：")
        find_dict['email'] = input_card_info(find_dict['email'],"email：")

        return print("修改完成")
    elif action_int == "2":
        card_list.remove(find_dict)
        print("删除名片：")
def input_card_info(dict_value, tips_message):
    result_str = input(tips_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
