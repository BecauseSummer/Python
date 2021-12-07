# –*–coding:utf-8 –*–
# 2021-12-07 11:27
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

class look_class_notice(CaseLogin):
    def test_look_class_notice(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-10 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-10 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "班级通知").click()
        element = self.driver.find_element(By.LINK_TEXT, "班级通知")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(8) .row > .mr-10").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(14) .row > .mr-10").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.close()