# –*–coding:utf-8 –*–
# 2021-12-06 16:27
from time import sleep
from selenium.webdriver.common.by import By
from langyun_automate.langyun.page import webdriver_initialzation
'''
相册操作
'''
class photos(webdriver_initialzation.CaseLogin):
    def test_add_photos(self):
        # 新建相册
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-5 .img-responsive:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "班级相册").click()
        self.driver.switch_to.frame(3)
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "title").click()
        self.driver.find_element(By.NAME, "title").send_keys("TestPhoto")
        self.driver.find_element(By.NAME, "classId").click()

    def test_upload_photos(self):
        # 上传相册
        dropdown = self.driver.find_element(By.NAME, "classId")
        dropdown.find_element(By.XPATH, "//option[. = '小星星小班']").click()
        self.driver.find_element(By.NAME, "classId").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".hover:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-3:nth-child(1) .kp-tu").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".Hui-iconfont:nth-child(1)").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".tabBar > span:nth-child(2)").click()
        self.driver.switch_to.frame(0)
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(1) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(2) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(3) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(4) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(5) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(6) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(12) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(11) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(10) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(9) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(8) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(7) > img").click()
        self.driver.find_element(By.LINK_TEXT, "8").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(5) > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-2:nth-child(4) > img").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".tabBar > span:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".tabBar").click()
        self.driver.find_element(By.CSS_SELECTOR, ".tabBar > span:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-xs-12:nth-child(1) > .to_second_step").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5) > .btn-secondary").click()


    def test_del_photos(self):
        # 删除相册
        self.driver.switch_to.default_content()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-3:nth-child(1) .kp-tu").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-3:nth-child(1) > .show-kapian .kp-tu1").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-imgnext").click()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-phimg > img").click()
        self.driver.find_element(By.LINK_TEXT, "返回").click()

    def test_close_win(self):
        # 关闭窗口
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()
        self.driver.find_element(By.CSS_SELECTOR, ".not-hover").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        self.driver.close()