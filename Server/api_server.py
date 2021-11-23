# –*–coding:utf-8 –*–
# 2021-09-09 17:33
import flask
import json
from flask import request
'''
flask: web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、password
'''

# 创建一个服务，把当前的这个Python文件当做一个服务
server = flask.Flask(__name__)
# server.config['JSON_AS_ASSCII'] = False
@server.route('/login', methods=['get', 'post']) # server.route 可以将普通函数转变化服务
def login():
    username = request.values.get('name')

    pwd = request.values.get('pwd')

    if username and pwd:
        if username == 'admin' and pwd == 'admin':
            resu = {'code':200, 'messages': '登录成功'}
            return json.dumps(resu, ensure_ascii=False)
        else:
            resu = {'code':-1, '\n' 'messages':'账号或密码错误'}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {'code':10001, '\n' 'messages':'参数不能为空'}
        return json.dumps(resu, ensure_ascii=False)

if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0 ')# 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问