# –*–coding:utf-8 –*–
# 2021-12-07 09:59
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

'''
创建其他计划
'''
class add_other_plan(CaseLogin):
    def test_add_other_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-5 div").click()
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # body
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "其他计划").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "创建计划 ").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").send_keys("哈哈哈哈")
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()