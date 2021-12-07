# –*–coding:utf-8 –*–
# 2021-12-07 09:28
from selenium.webdriver.common.by import By

from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

class other_plan(CaseLogin):
    def test_look_other_plan(self):
        self.driver.set_window_size(1226, 902)
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 div").click()
        self.driver.find_element(By.LINK_TEXT, "学期计划").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.close()