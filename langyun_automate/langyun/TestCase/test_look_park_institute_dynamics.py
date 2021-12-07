# –*–coding:utf-8 –*–
# 2021-12-07 11:32
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

class look_park_institute_dynamics(CaseLogin):
    def test_look_park_institute_dynamics(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-10 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-10 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "园所动态").click()
        element = self.driver.find_element(By.LINK_TEXT, "园所动态")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(2) .mt-10").click()
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(2) a:nth-child(3) > .hy-txt").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.close()