# coding=utf-8

from selenium.webdriver.common.by import By

from .base import BasePage

class LoginPage(BasePage):
    # 手机号码输入框
    username_loc = (By.XPATH, '//*[@id="form"]/div[1]/div/div/div/input')
    # 登录密码输入框
    password_loc = (By.XPATH, '//*[@id="password-input"]')
    # 登录按钮
    submit_loc = (By.XPATH, '//*[@id="login-btn"]')
    infant_loc = (By.XPATH, '//*[@id="li-2"]/a')
    def open(self):
        self._open(self.base_url, self.page_title)

    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        self.find_element(*self.submit_loc).click()

