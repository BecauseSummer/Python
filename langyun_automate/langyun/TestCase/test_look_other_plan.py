# –*–coding:utf-8 –*–
# 2021-12-07 09:21
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin
from time import sleep

class other_plan(CaseLogin):
    def test_look_other_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body").click()
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(2)
        sleep(2)
        self.driver.find_element(By.LINK_TEXT, "其他计划").click()
        self.driver.find_element(By.LINK_TEXT, ".layui-layer-close").click()
        self.driver.close()