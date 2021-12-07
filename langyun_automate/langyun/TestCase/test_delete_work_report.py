# –*–coding:utf-8 –*–
# 2021-12-07 10:45
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

class delete_work_reoirt(CaseLogin):
    def test_delete_work_report(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.LINK_TEXT, "个人计划").click()
        self.driver.find_element(By.LINK_TEXT, "工作汇报").click()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "删除").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.close()