# –*–coding:utf-8 –*–
# 2021-12-06 16:41
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login():
    def setup(self, url, username, password):
        self.driver = webdriver.Chrome()
        self.url = url
        self.username = username
        self.passwrod =password

    def tearDown(self):
        self.driver.quit()

class Child_attendance(Login):
    def test_click_attendance_analysis(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-5 .img-responsive:nth-child(1)").click()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "班级考勤分析").click()
        self.driver.find_element(By.LINK_TEXT, "年级考勤分析").click()
        self.driver.find_element(By.LINK_TEXT, "考勤分析").click()
        self.driver.switch_to.frame(0)
        time.sleep(3)
        self.driver.find_element(By.NAME, "yearMonth").click()
        self.driver.find_element(By.NAME, "yearMonth").send_keys("2020-12")
        self.driver.find_element(By.ID, "cx").click()
        self.driver.close()

