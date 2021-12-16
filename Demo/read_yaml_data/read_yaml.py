# –*–coding:utf-8 –*–
# 2021-12-16 16:40
import yaml
import os

script_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(script_path, "host.yaml")

cfg = open(yaml_path, 'r').read()
print(type(cfg))

host_info = yaml.load(cfg, Loader=yaml.FullLoader)
print(type(host_info))

def get_ip():
    port = host_info.get('DB').get('port')
    print(port)
    ip = print('ip是：%s'%host_info.get('DB').get('ip'))
    return ip, port

def get_port():
    port = print('IP地址是:%s'%host_info.get('k8s')[0].get('ip'))
    return port

get_ip()
get_port()