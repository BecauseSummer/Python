# –*–coding:utf-8 –*–
# 2021-12-01 16:31


def check_sum():
    '''
    完成任意整数序列的相加-生成一个整数序列,里面全是数字。求里面所有数字的和
    '''
    # 导入随机数的模块包
    import random
    List = []
    for  i in range(10):
        List.append(random.randint(1, 100)) # random.randint 随机整数
    print('序列:{}'.format(List))
    result = sum(List)
    print('结果:{}'.format(result))
check_sum()

def check_length():
    number = input('input:')
    if len(number) > 5:
        print('length:{}'.format(len(number)), 'True')
    else:
        print('False')
check_length()