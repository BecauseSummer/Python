# –*–coding:utf-8 –*–
# 2021-12-06 16:56
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from langyun_automate.langyun.page import webdriver_initialzation


class work_report(webdriver_initialzation.CaseLogin):
    def test_work_report(self):
        # 编辑工作汇报
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.LINK_TEXT, "个人计划").click()
        self.driver.find_element(By.LINK_TEXT, "工作汇报计划").click()
        element = self.driver.find_element(By.LINK_TEXT, "工作汇报计划")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        sleep(2)
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.close()