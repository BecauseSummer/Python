# –*–coding:utf-8 –*–
# 2021-03-25 16:14

import functools, inspect

def is_admin(fun):
	@functools.wraps(fun)
	def wrapper(*args, **kwargs):
		'''
		inspect.getcallargs
		'''
		inspect_rec = inspect.getcallargs(fun, *args, **kwargs)
		print('inspect的返回值:%s' %(inspect_rec))
		if inspect_rec.get('name') == 'root':
			temp = fun(*args, **kwargs)
			return temp
		else:
			print('not root user,no permisson add stduent')
	return wrapper
loggin_session = ['root', 'admin', 'redhat']
def Is_login(fun):
	@functools.wraps(fun)
	def wrapper(*args, **kwargs):
		if args[0] in loggin_session:
			temp = fun(*args, **kwargs)
			return temp
	return wrapper

@Is_login
@is_admin
def add_admin(name):
	print('添加学生信息')
add_admin('westos')
add_admin('redhat')
add_admin('root')
add_admin('root')
print('内存地址是:',id(add_admin))
