# –*–coding:utf-8 –*–
# 2021-12-07 11:21
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin
'''

删除整年计划
'''

class delete_year_plan(CaseLogin):
    def test_delete_year_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "整年计划").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "删除").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.close()