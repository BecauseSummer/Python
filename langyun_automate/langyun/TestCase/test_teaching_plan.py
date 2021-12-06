# –*–coding:utf-8 –*–
# 2021-12-06 18:10
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page import webdriver_initialzation
from time import sleep

class teaching_plan(webdriver_initialzation.CaseLogin):
    def test_teaching_plan(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-6 .img-responsive:nth-child(1)").click()
        self.driver.switch_to.frame(2)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(3)").click()
        self.driver.find_element(By.NAME, "content[Wed][am][type][]").click()
        dropdown = self.driver.find_element(By.NAME, "content[Wed][am][type][]")
        dropdown.find_element(By.XPATH, "//option[. = '体育活动']").click()
        sleep(2)
        self.driver.find_element(By.NAME, "content[Wed][am][type][]").click()
        self.driver.find_element(By.NAME, "content[Wed][am][class][]").click()
        self.driver.find_element(By.NAME, "content[Wed][am][class][]").send_keys("捉迷藏7")
        self.driver.find_element(By.CSS_SELECTOR, "#form").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()