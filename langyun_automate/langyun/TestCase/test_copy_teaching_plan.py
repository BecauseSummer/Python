# –*–coding:utf-8 –*–
# 2021-12-07 10:32
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin
from selenium.webdriver import ActionChains

'''
复制教学计划
'''

class copy_teaching_plan(CaseLogin):
    def test_copy_teaching_plan(self):
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(2)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "复制计划").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "week").click()
        dropdown = self.driver.find_element(By.NAME, "week")
        dropdown.find_element(By.XPATH, "//option[. = '第11周']").click()
        self.driver.find_element(By.NAME, "week").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        self.driver.close()