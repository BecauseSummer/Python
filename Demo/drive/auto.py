# –*–coding:utf-8 –*–
# 2021-04-14 14:10
from selenium import webdriver
import time

def open_broser(name, url, *args):
	'''
	封装打开浏览器的方法
	'''
	if name == 'chrome':
		driver = webdriver.Chrome()
	elif name == 'firfox':
		driver = webdriver.Firefox()
	elif name == 'ie':
		driver = webdriver.Ie()
	driver.get(url)
	driver.maximize_window()
	return driver

class webUI_init():
	def __init__(self, name, url, *args):
		self.dirver = open_broser(name, url, *args)
		
	# 扎到元素，输入文本
	def input_text( self, locator_type, value, text ):
		self.dirver.find_element(by = locator_type, value= value).send_keys(text)
		time.sleep(5)
	
	# 点击方法
	def click_element( self, locator_type, value ):
		self.dirver.find_element(by = locator_type, value = value).click()
		time.sleep(3)
	
	# 断言文本
	def assert_by_text( self, text, locator_type, value ):
		nike_name = self.dirver.find_element(by = locator_type, value = value).text
		assert text in nike_name
	# 退出
	def quit( self ):
		self.dirver.quit()
		print('done')
	
	# 等待时间
	def wait( self, n ):
		self.dirver.implicitly_wait(n)