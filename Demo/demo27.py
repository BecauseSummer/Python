# –*–coding:utf-8 –*–
# 2021-12-29 13:50
import datetime
dt = datetime.datetime.now()
buy_time = datetime.datetime.now().strftime('%m-%d %A  %T')
buy_time2 = datetime.datetime.now().strftime('%Y-%m-%d %T')
print('星期{}'.format(dt.strftime('%w')),buy_time)
print(buy_time)
print(buy_time2)