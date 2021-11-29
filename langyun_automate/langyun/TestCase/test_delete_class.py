# –*–coding:utf-8 –*–
# 2021-04-14 16:02
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Login():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) # 全局隐式等待10s
        self.url = "http://t2.aservice.langlangyun.com:5480/langyun/public/index.php/workplace/pub/login.html"
        self.username = '13006662818'
        self.password = 'langyun'

class Child(Login):
    def test_select_child(self):
        self.driver.find_element(By.CLASS_NAME,"#li-5 div").click()
        self.driver.find_element(By.LINK_TEXT, "班级信息").click()
        element = self.driver.find_element(By.LINK_TEXT,"班级信息")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "删除").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()