# –*–coding:utf-8 –*–
# 2021-12-06 18:17
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page import webdriver_initialzation
from time import sleep

class other_plan(webdriver_initialzation.CaseLogin):
    def test_other_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-6 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "其他计划").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        self.driver.switch_to.frame(0)
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".btn > .Hui-iconfont").click()
        self.driver.find_element(By.LINK_TEXT, "其他计划").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-title")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "layui-layer-moves")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()

    def test_close_win(self):
        self.driver.close()