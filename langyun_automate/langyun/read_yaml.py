# –*–coding:utf-8 –*–
# 2021-12-16 16:54
import yaml
import os

script_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(script_path, 'data.yaml')

cfg = open(yaml_path, 'r').read()
page_info = yaml.load(cfg, Loader=yaml.FullLoader)

url = page_info.get('Login_info').get('url')
username = page_info.get('Login_info').get('username')
passwrod = page_info.get('Login_info').get('password')

print("url是：{}".format(url) )
print("username是：{}".format(username))
print("password是：{}".format(passwrod))