# –*–coding:utf-8 –*–
# 2021-12-07 13:51
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin


class edit_emergency_situation(CaseLogin):
    def test_edit_emergency_situation(self):
        # 编辑突发状况
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-7 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-7 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "突发状况").click()
        element = self.driver.find_element(By.LINK_TEXT, "突发状况")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        element = self.driver.find_element(By.LINK_TEXT, "编辑")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "OutBurstScene").click()
        self.driver.find_element(By.NAME, "OutBurstScene").send_keys("滚滚滚让人")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()

    def test_add_emergency_situation(self):
        # 创建突发状况
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-7 div").click()
        self.driver.find_element(By.LINK_TEXT, "突发状况").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-warning").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "OutBurstName").click()
        self.driver.find_element(By.NAME, "OutBurstName").send_keys("磕伤")
        self.driver.find_element(By.NAME, "OutBurstScene").click()
        self.driver.find_element(By.NAME, "OutBurstScene").send_keys("滚滚滚")
        self.driver.find_element(By.NAME, "OutBurstContent").click()
        self.driver.find_element(By.NAME, "OutBurstContent").send_keys("滚滚滚")
        self.driver.find_element(By.ID, "teacher").click()
        dropdown = self.driver.find_element(By.ID, "teacher")
        dropdown.find_element(By.XPATH, "//option[. = '前端测试账号(勿删)']").click()
        self.driver.find_element(By.ID, "teacher").click()
        self.driver.find_element(By.CSS_SELECTOR, "#uploadifive-upload_all > input:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, "#uploadifive-upload_all > input:nth-child(3)").send_keys(
                "C:\\fakepath\\1.jpeg")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.close()

    def test_delete_emergency_situation(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-7 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-7 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "突发状况").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "删除").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.close()

