# –*–coding:utf-8 –*–
# 2021-04-15 13:57
from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains

import time
# 打开浏览器
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.maximize_window()
browser.implicitly_wait(10)
# ActionChains(browser).move_to_element(browser.find_element_by_id('')).perform()
# element = browser.find_element_by_id("")
# browser.find_element_by_css_selector('').click()
# browser.switch_to_frame()
# browser.switch_to_default_content()
browser.find_element_by_link_text('地图').click()
time.sleep(5)
browser.quit() # 退出浏览器
# browser.close() 退出当前标签页

