# –*–coding:utf-8 –*–
# 2021-12-07 10:57
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin
'''
删除学期计划

'''

class delete_term_plan(CaseLogin):
    def test_delete_term_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 div").click()
        self.driver.find_element(By.LINK_TEXT, "学期计划").click()
        element = self.driver.find_element(By.LINK_TEXT, "学期计划")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "删除").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.close()