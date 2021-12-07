# –*–coding:utf-8 –*–
# 2021-12-07 08:55
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
from langyun_automate.langyun.page import webdriver_initialzation

class year_plan(webdriver_initialzation.CaseLogin):
    def test_year_plan(self):
        # 编辑整年计划
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0 ,0).perform()
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, "整年计划").click()
        element = self.driver.find_element(By.LINK_TEXT, "整年计划")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    def test_close_win(self):
        self.driver.close()
