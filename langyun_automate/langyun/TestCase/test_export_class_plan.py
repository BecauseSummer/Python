# –*–coding:utf-8 –*–
# 2021-12-07 10:10
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

'''
导出班级计划
'''
class export_class_plan(CaseLogin):
    def test_export_class_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 div").click()
        self.driver.switch_to.frame(2)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "导出").click()
        self.driver.close()