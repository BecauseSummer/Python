# –*–coding:utf-8 –*–
# 2021-12-06 17:58
import unittest, yaml, time, allure
from selenium import webdriver
from .login_page import LoginPage

class CaseLogin(unittest.TestCase) :
    '''
    朗云登录Case
    '''
    def get_url(self):
        data = open('data.yaml', mode='r', encoding='utf-8')
        url_info = yaml.load(data, Loader=yaml.FullLoader)
        url = url_info.get('Login_info').get('url')
        return url

    def get_username(self) :
        data = open('data.yaml', mode='r', encoding='utf-8')
        username_name = yaml.load(data, Loader=yaml.FullLoader)
        username = username_name.get('Login_info').get('username')
        return username

    def get_password(self) :
        data = open('data.yaml', mode='r', encoding='utf-8')
        password_pwd = yaml.load(data, Loader=yaml.FullLoader)
        password = password_pwd.get('Login_info').get('password')
        return None

    @allure.title("登录成功")
    def setUp(self, url, username, password) :
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # 全局隐式等待10s
        self.url = CaseLogin.get_url(url)
        self.username = CaseLogin.get_username(username)
        self.password = CaseLogin.get_password(password)

    def testLogin(self) :
        login_page = LoginPage(self.driver, self.url, u'后台登录 - 朗云智慧幼教管理平台')
        login_page.open()
        login_page.input_username(self.username)
        time.sleep(2)
        login_page.input_password(self.password)
        login_page.click_submit()
        time.sleep(5)
        assert self.driver.title == u'朗云智慧幼教管理平台', '登录失败'
        self.login_page = login_page

    def tearDown(self) :
        self.driver.quit()
