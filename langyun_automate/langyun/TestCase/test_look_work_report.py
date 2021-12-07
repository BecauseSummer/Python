# –*–coding:utf-8 –*–
# 2021-12-07 09:00
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from langyun_automate.langyun.page import webdriver_initialzation

class look_work_report(webdriver_initialzation.CaseLogin):
    def test_look_work_report(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body").click()
        actions = ActionChains(self.driver)
        sleep(3)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "工作总结").click()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
    def test_close_win(self):
        self.driver.close()