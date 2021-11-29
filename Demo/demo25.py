# –*–coding:utf-8 –*–
# 2021-12-01 16:31

'''
完成任意整数序列的相加-生成一个整数序列,里面全是数字。求里面所有数字的和
'''

import random
List = []
for  i in range(10):
    List.append(random.randint(1, 100))
print('序列:{}'.format(List))
result = sum(List)
print('结果:{}'.format(result))