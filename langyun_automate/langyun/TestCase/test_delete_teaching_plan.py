# –*–coding:utf-8 –*–
# 2021-12-07 10:51
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin
'''
删除教学计划
'''
class delete_teaching_plan(CaseLogin):
    def test_delete_teaching_plan(self):

        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.LINK_TEXT, "个人计划").click()
        self.driver.switch_to.frame(2)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "删除").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.close()