# –*–coding:utf-8 –*–
# 2021-12-07 10:03
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin
'''
创建学期计划
'''

class add_term_plan(CaseLogin):
    def test_add_term_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "学期计划").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "创建学期计划 ").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "ClassId").click()
        dropdown = self.driver.find_element(By.NAME, "ClassId")
        dropdown.find_element(By.XPATH, "//option[. = '小星星小班']").click()
        self.driver.find_element(By.NAME, "ClassId").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()