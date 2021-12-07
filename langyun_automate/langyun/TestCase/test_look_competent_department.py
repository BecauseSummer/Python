# –*–coding:utf-8 –*–
# 2021-12-07 13:32
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin


'''
查看主管部门通知
'''
class competent_department(CaseLogin):
    def test_look_competent_department(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-10 .img-responsive:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "主管部门通知").click()
        element = self.driver.find_element(By.LINK_TEXT, "主管部门通知")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body").click()
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(1) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(5) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.close()

