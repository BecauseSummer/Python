# –*–coding:utf-8 –*–
# 2021-12-07 09:53
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page import webdriver_initialzation
'''
创建教学计划
'''

class add_teaching_plan(webdriver_initialzation.CaseLogin):
    def test_add_teaching_plan(self):
        self.driver.set_window_size(1936, 1036)
        self.driver.find_element(By.LINK_TEXT, "个人计划").click()
        self.driver.switch_to.frame(2)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "创建教学计划").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "content[Mon][am][type][]").click()
        dropdown = self.driver.find_element(By.NAME, "content[Mon][am][type][]")
        dropdown.find_element(By.XPATH, "//option[. = '读书']").click()
        self.driver.find_element(By.NAME, "content[Mon][am][type][]").click()
        self.driver.find_element(By.NAME, "content[Mon][am][class][]").click()
        self.driver.find_element(By.NAME, "content[Mon][am][class][]").send_keys("music")
        self.driver.find_element(By.CSS_SELECTOR, ".Mon_am:nth-child(2) .select").click()
        dropdown = self.driver.find_element(By.CSS_SELECTOR, ".Mon_am:nth-child(2) .select")
        dropdown.find_element(By.XPATH, "//option[. = '广泛的第三']").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".Mon_am:nth-child(2) .select").click()
        self.driver.find_element(By.CSS_SELECTOR, ".Mon_am:nth-child(2) .input-text").click()
        self.driver.find_element(By.CSS_SELECTOR, ".Mon_am:nth-child(2) .input-text").send_keys("music")
        self.driver.find_element(By.CSS_SELECTOR, ".tabBar1 > span:nth-child(2)").click()
        self.driver.find_element(By.NAME, "content[Mon][pm][type][]").click()
        dropdown = self.driver.find_element(By.NAME, "content[Mon][pm][type][]")
        dropdown.find_element(By.XPATH, "//option[. = '体育活动']").click()
        self.driver.find_element(By.NAME, "content[Mon][pm][type][]").click()
        self.driver.find_element(By.NAME, "content[Mon][pm][class][]").click()
        self.driver.find_element(By.NAME, "content[Mon][pm][class][]").send_keys("抓迷藏")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()
