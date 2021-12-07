# –*–coding:utf-8 –*–
# 2021-12-07 13:40
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

'''
发布班级通知
'''
class add_class_notice(CaseLogin):
    def test_add_class_notice(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-10 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-10 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "班级通知").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "创建草稿 ").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").send_keys("发发发")
        self.driver.find_element(By.NAME, "info").click()
        self.driver.find_element(By.NAME, "info").send_keys("方法方法付付付付付付付付付付")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.LINK_TEXT, "发布").click()
        self.driver.close()