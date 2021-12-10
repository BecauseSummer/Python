# –*–coding:utf-8 –*–
# 2021-12-13 10:51

def write_name():
    name = input("you name:")
    filename = open('./name.txt','a+')
    filename.write(name)
    filename.close()
    print('write success')

write_name()