# –*–coding:utf-8 –*–
# 2021-12-06 17:54
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from langyun_automate.langyun.page import webdriver_initialzation

class term_plan(webdriver_initialzation.CaseLogin):
    def test_term_plan(self):
        # 编辑学期计划
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR,"#li-6 .img-responsive:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "学期计划").click()
        element = self.driver.find_element(By.LINK_TEXT, "学期计划")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        sleep(3)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()

    def test_close_win(self):
        self.driver.close()