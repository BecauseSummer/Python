# –*–coding:utf-8 –*–
# 2021-12-06 16:13
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

class Login():
    def setup(self, url,username, password):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.url = url
        self.username = username
        self.password = password

    def tearDown(self):
        self.driver.quit()

class add_class(Login):
    def test_add_new_class(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-5 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-5 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "班级信息").click()
        element = self.driver.find_element(By.LINK_TEXT, "班级信息")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "添加班级").click()
        self.driver.switch_to.frame(0)
        sleep(3)
        self.driver.find_element(By.NAME, "ClassName").click()
        self.driver.find_element(By.NAME, "ClassName").send_keys("TEST CLASS")
        self.driver.find_element(By.NAME, "InfantNum").click()
        self.driver.find_element(By.NAME, "InfantNum").send_keys("60")
        self.driver.find_element(By.ID, "time_case").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-this").click()
        self.driver.find_element(By.CSS_SELECTOR, ".am-selected-status").click()
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(23) > .am-selected-text").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(8)").click()
        self.driver.find_element(By.NAME, "slogan").click()
        self.driver.find_element(By.NAME, "slogan").send_keys("..")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        sleep(3)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.LINK_TEXT, "升班").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.find_element(By.LINK_TEXT, "升班").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.find_element(By.LINK_TEXT, "毕业").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "ClassName").click()
        self.driver.find_element(By.NAME, "ClassName").send_keys("TEST CLASS22")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.LINK_TEXT, "毕业").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.close()
