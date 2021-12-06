# –*–coding:utf-8 –*–
# 2021-12-06 17:38
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from langyun_automate.langyun.page import webdriver_initialzation

class work_summary(webdriver_initialzation.CaseLogin):
    def test_work_summary(self):
        # 编辑工作总结
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        sleep(3)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "工作总结").click()

    def test_close_win(self):
        self.driver.close()