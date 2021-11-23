# –*–coding:utf-8 –*–
# 2021-11-03 17:20



str = input("请输入：")
# file = open(line, "a")
file_path = "./file/a.txt"
file = open(file_path, "a")
if str =="":
    print("请输入...")
else:
    for line in str:
        file.write(line +"")
    print(str,"write success~")
    file.close()


