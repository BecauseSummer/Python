# –*–coding:utf-8 –*–
# 2021-12-07 13:47
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

'''
编辑食谱
'''
class edit_recipe(CaseLogin):
    def test_edit_recipe(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-7 div").click()
        self.driver.find_element(By.CSS_SELECTOR, "#li-8 div").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()

    def test_add_recipe(self):
        # 创建食谱
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-8 div").click()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-warning").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "content[Mon][meal0][food][]").click()
        self.driver.find_element(By.NAME, "content[Mon][meal0][food][]").send_keys("小菜")
        self.driver.find_element(By.NAME, "content[Mon][meal1][food][]").click()
        self.driver.find_element(By.NAME, "content[Mon][meal1][food][]").send_keys("面包、")
        self.driver.find_element(By.NAME, "content[Mon][meal2][food][]").click()
        self.driver.find_element(By.NAME, "content[Mon][meal2][food][]").send_keys("小菜 ")
        self.driver.find_element(By.NAME, "content[Mon][meal3][food][]").click()
        self.driver.find_element(By.NAME, "content[Mon][meal3][food][]").send_keys("小菜")
        self.driver.find_element(By.NAME, "content[Mon][meal4][food][]").click()
        self.driver.find_element(By.NAME, "content[Mon][meal4][food][]").send_keys("小菜")
        self.driver.find_element(By.NAME, "content[Mon][meal5][food][]").click()
        self.driver.find_element(By.NAME, "content[Mon][meal5][food][]").send_keys("小菜")
        self.driver.find_element(By.NAME, "week").click()
        time.sleep(3)
        dropdown = self.driver.find_element(By.NAME, "week")
        dropdown.find_element(By.XPATH, "//option[. = '第18周']").click()
        self.driver.find_element(By.NAME, "week").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.find_element(By.NAME, "semester").click()
        self.driver.find_element(By.NAME, "semester").click()
        self.driver.find_element(By.NAME, "year").click()
        dropdown = self.driver.find_element(By.NAME, "year")
        dropdown.find_element(By.XPATH, "//option[. = '2023-2024']").click()
        self.driver.find_element(By.NAME, "year").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.close()

    def test_copy_recipe(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-8 div").click()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "复制食谱").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "week").click()
        dropdown = self.driver.find_element(By.NAME, "week")
        dropdown.find_element(By.XPATH, "//option[. = '第20周']").click()
        self.driver.find_element(By.NAME, "week").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.close()