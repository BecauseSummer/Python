# –*–coding:utf-8 –*–
# 2021-12-07 10:06
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin
'''
创建整年计划
'''
class add_year_plan(CaseLogin):
    def test_add_year_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 div").click()
        self.driver.find_element(By.LINK_TEXT, "整年计划").click()
        element = self.driver.find_element(By.LINK_TEXT, "整年计划")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "创建年度计划 ").click()
        self.driver.switch_to.frame(0)
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.find_element(By.NAME, "year").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(4)
        self.driver.find_element(By.CSS_SELECTOR, ".menuOn").click()
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(3)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()