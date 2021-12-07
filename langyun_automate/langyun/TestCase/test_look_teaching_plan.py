# –*–coding:utf-8 –*–
# 2021-12-07 09:13
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

class teaching_plan(CaseLogin):
    def test_look_teaching_plan(self):
        # 查看教学计划
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR,  "#li-6 div").click()
        self.driver.switch_to.frame(2)
        self.driver.switch_to.frame(0)
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        self.driver.find_element(By.CSS_SELECTOR, ".langyui-layer-close").click()
        self.driver.close()
