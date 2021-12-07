# –*–coding:utf-8 –*–
# 2021-12-07 10:21
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin
'''
导出其他计划
'''

class export_ohter_plan(CaseLogin):
    def test_export_other_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body").click()
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "其他计划").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "导出").click()
        self.driver.close()
