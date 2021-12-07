# –*–coding:utf-8 –*–
# 2021-12-07 13:54
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

'''
服药模块
'''
class Medication_record(CaseLogin):
    def test_medication_record(self):
        # 查看服药记录
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-7 div").click()
        self.driver.find_element(By.LINK_TEXT, "用药服药记录").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "记录").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(1) > td:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(2) > td:nth-child(2)").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.close()

    def test_medication_record_details(self):
        #  查看服药记录详情
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-7 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-7 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "用药服药记录").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.close()

    def test_take_medication(self):
        # 进行服药
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.LINK_TEXT, "退出").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.find_element(By.CSS_SELECTOR, "#li-7 .img-responsive:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "用药服药记录").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "服药").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "info").click()
        self.driver.find_element(By.NAME, "info").send_keys("22222")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()

    def test_delete_medication(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-7 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-7 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "用药服药记录").click()
        element = self.driver.find_element(By.LINK_TEXT, "用药服药记录")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(2) input").click()
        self.driver.find_element(By.ID, "batch-delete").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.close()