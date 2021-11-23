# –*–coding:utf-8 –*–
# 2021-09-14 15:10
import requests
import json
url = 'https://yun.langlangyun.com/ly/user/login'
data = {
        "account":"131300008888",
        "password":"sbDgoEeEKGqyu8t/TM5vAQ=="
    }
result = requests.post(url, data).json()
res = json.dumps(result)
print(res)

# import json
#
# class Run_Main:
#     def sed_post(self, url, data):
#         result = requests.post(url = url, data=data).json()
#         res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
#         return res
#
#     def sed_get(self, url, data):
#         result = requests.get(url=url, data=data)
#         res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
#         return res
#
#     def run_main(self, method, url=None, data=None):
#         if method == 'post':
#             result = self.sed_post(url, data)
#         elif method == 'get':
#             result = self.sed_get(url, data)
#         else:
#             print("错误！")
#         return result
#
# if __name__ == '__main__':
#     url = 'https://yun.langlangyun.com/ly/user/login'
#     data = {
#         "account":"131300008888",
#         "password":"sbDgoEeEKGqyu8t/TM5vAQ=="
#     }
#     run = Run_Main()
#     res = run.run_main("post", url, data)
#     print(res)