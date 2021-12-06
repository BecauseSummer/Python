# –*–coding:utf-8 –*–
# 2021-04-14 16:02
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page import webdriver_initialzation

class Child(webdriver_initialzation.CaseLogin):
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