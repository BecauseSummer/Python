# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    BasePage 封装所有页面的公用方法，例如 driver、url、FindElement 等
    """

    # 初始化 driver、url、page_title
    def __init__(self, selenium_driver, base_url, page_title):
        self.driver = selenium_driver
        self.base_url = base_url
        self.page_title = page_title

    # 通过 title 断言进入的页面是否正确
    # 试用 title 获取当前窗口 title，检查输入的 title 是否在当前 title 中，返回比较结果（True or False）
    def on_page(self, page_title):
        return page_title in self.driver.title

    # 打开页面
    # 以_open开发的方法，在使用 import * 时，该方法不会被导入，保证该方法为私有类
    def _open(self, url, page_title):
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(page_title), f'打开页面失败 {url}'

    def open(self):
        self._open(self.base_url, self.page_title)

    # 查找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(f'{self} 页面中未能找到 {loc} 元素')

    # 重新 switch_frame
    def switch_frame(self, loc):
        self.driver.switch_frame(loc)

    # 执行js脚本
    def script(self, src):
        self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, f'_{loc}')  # 相当于 self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(f'{self} 页面中未能找到 {loc} 元素')
