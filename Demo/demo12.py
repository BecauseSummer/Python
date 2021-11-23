# –*–coding:utf-8 –*–
# 2021-03-30 14:42
'''用正则表达式查找文本模式'''
import re
pattern = re.compile('((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}')
str = '192.168.3.102'
print(pattern.search(str)) # .search 查找