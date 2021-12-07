# –*–coding:utf-8 –*–
# 2021-12-07 09:46
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

class add_work_report(CaseLogin):
    def test_add_work_report(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "工作总结").click()
        element = self.driver.find_element(By.LINK_TEXT, "工作总结")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body").click()
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "工作总结").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").send_keys("哈哈哈哈")
        self.driver.find_element(By.NAME, "ClassId").click()
        # dropdown = self.driver.find_element(By.NAME, "ClassId")
        dropdown = self.driver.find_element(By.NAME, "ClassId")
        dropdown.find_element(By.XPATH, "//option[. = '小星星小班']").click()
        self.driver.find_element(By.NAME, "ClassId").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()