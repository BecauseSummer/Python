# –*–coding:utf-8 –*–
# 2021-12-07 11:34
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

'''
查看园务通知
'''
class look_garden_affairs_notice(CaseLogin):
    def test_look_garden_affairs_notice(self):
        self.driver.set_window_size(1226, 902)
        self.driver.find_element(By.CSS_SELECTOR, "#li-10 .img-responsive:nth-child(1)").click()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        element = self.driver.find_element(By.LINK_TEXT, "详情")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".notice1-content > div").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.close()