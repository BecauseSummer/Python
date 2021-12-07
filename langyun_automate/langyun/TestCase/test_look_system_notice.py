# –*–coding:utf-8 –*–
# 2021-12-07 11:29
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

class look_system_notice(CaseLogin):
    def test_look_system_notice(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-10 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-10 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "系统消息").click()
        element = self.driver.find_element(By.LINK_TEXT, "系统消息")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(2) .jj").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.close()