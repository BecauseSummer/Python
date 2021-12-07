# –*–coding:utf-8 –*–
# 2021-12-07 14:05
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from langyun_automate.langyun.page.webdriver_initialzation import CaseLogin

class childrens_archives(CaseLogin):
    def test_pages(self):
        # 翻页操作
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.LINK_TEXT, "健康看板").click()
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-2 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "成长档案").click()
        self.driver.switch_to.frame(4)
        self.driver.find_element(By.LINK_TEXT, "2").click()
        self.driver.find_element(By.LINK_TEXT, "3").click()
        self.driver.find_element(By.LINK_TEXT, "4").click()

    def test_edit_childrens_archives(self):
        # 编辑已有成长档案
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 div").click()
        self.driver.find_element(By.LINK_TEXT, "成长档案").click()
        element = self.driver.find_element(By.LINK_TEXT, "成长档案")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.NAME, "info").click()
        self.driver.find_element(By.NAME, "info").send_keys("好的啊实打实阿萨德大声道asadadas22222222222222222222222222222")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()

    def test_edit_childrens(self):
        # 编辑幼儿
        # Test name: 幼儿档案-编辑幼儿
        # Step # | name | target | value
        # 1 | open | http://t2.aservice.langlangyun.com:5480/langyun/public/index.php/workplace/index/index.html |
        self.driver.get("http://t2.aservice.langlangyun.com:5480/langyun/public/index.php/workplace/index/index.html")
        # 2 | setWindowSize | 1936x1096 |
        self.driver.set_window_size(1936, 1096)
        # 3 | click | css=#li-2 div |
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 div").click()
        # 4 | selectFrame | index=2 |
        self.driver.switch_to.frame(2)
        # 5 | click | linkText=编辑 |
        self.driver.find_element(By.LINK_TEXT, "编辑").click()
        # 6 | selectFrame | index=0 |
        self.driver.switch_to.frame(0)
        # 7 | click | name=username |
        self.driver.find_element(By.NAME, "username").click()
        # 8 | type | name=username | 测试小孩
        self.driver.find_element(By.NAME, "username").send_keys("测试小孩")
        # 9 | click | name=nation |
        self.driver.find_element(By.NAME, "nation").click()
        # 10 | select | name=nation | label=彝族
        dropdown = self.driver.find_element(By.NAME, "nation")
        dropdown.find_element(By.XPATH, "//option[. = '彝族']").click()
        # 11 | click | name=nation |
        self.driver.find_element(By.NAME, "nation").click()
        # 12 | click | css=.col-xs-12 > .btn-secondary |
        self.driver.find_element(By.CSS_SELECTOR, ".col-xs-12 > .btn-secondary").click()
        # 13 | mouseOver | css=.col-xs-12 > .btn-secondary |
        element = self.driver.find_element(By.CSS_SELECTOR, ".col-xs-12 > .btn-secondary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 14 | mouseOut | css=.col-xs-12 > .btn-secondary |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.close()

    def test_look_childrens_archives_details(self):
        # 查看成长档案
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.LINK_TEXT, "成长档案").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".upload-pre-item > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(5) > .formControls").click()
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()

    def test_details_details(self):
        # Test name: 幼儿档案-点击详情
        # Step # | name | target | value
        # 1 | open | http://t2.aservice.langlangyun.com:5480/langyun/public/index.php/workplace/index/index.html |
        self.driver.get("http://t2.aservice.langlangyun.com:5480/langyun/public/index.php/workplace/index/index.html")
        # 2 | setWindowSize | 1936x1096 |
        self.driver.set_window_size(1936, 1096)
        # 3 | click | css=#li-2 .img-responsive:nth-child(1) |
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)").click()
        # 4 | selectFrame | index=2 |
        self.driver.switch_to.frame(2)
        # 5 | click | linkText=详情 |
        self.driver.find_element(By.LINK_TEXT, "详情").click()
        # 6 | selectFrame | index=0 |
        self.driver.switch_to.frame(0)
        # 7 | click | css=.tabBar > span:nth-child(2) |
        self.driver.find_element(By.CSS_SELECTOR, ".tabBar > span:nth-child(2)").click()
        # 8 | click | css=.tabBar > span:nth-child(1) |
        self.driver.find_element(By.CSS_SELECTOR, ".tabBar > span:nth-child(1)").click()
        # 9 | click | css=.face-image > .btn |
        self.driver.find_element(By.CSS_SELECTOR, ".face-image > .btn").click()
        # 10 | mouseOver | css=.face-image > .btn |
        element = self.driver.find_element(By.CSS_SELECTOR, ".face-image > .btn")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # 11 | mouseOut | css=.face-image > .btn |
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        # 12 | selectFrame | relative=parent |
        self.driver.switch_to.default_content()
        # 13 | click | css=.layui-layer-close |
        self.driver.find_element(By.CSS_SELECTOR, ".layui-layer-close").click()

    def test_out_childrens(self):
        # Test name: 幼儿档案-离园幼儿
        # Step # | name | target | value
        # 1 | open | http://t2.aservice.langlangyun.com:5480/langyun/public/index.php/workplace/index/index.html |
        self.driver.get("http://t2.aservice.langlangyun.com:5480/langyun/public/index.php/workplace/index/index.html")
        # 2 | setWindowSize | 1226x902 |
        self.driver.set_window_size(1226, 902)
        # 3 | click | css=#li-2 .img-responsive:nth-child(1) |
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)").click()
        # 4 | selectFrame | index=2 |
        self.driver.switch_to.frame(2)
        # 5 | click | linkText=离园 |
        self.driver.find_element(By.LINK_TEXT, "离园").click()
        # 6 | click | linkText=确定 |
        self.driver.find_element(By.LINK_TEXT, "确定").click()

    def test_import_childrens(self): # 导入幼儿
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "模板导入").click()
        self.driver.find_element(By.ID, "importEasyFile").click()
        self.driver.find_element(By.ID, "importEasyFile").send_keys("C:\\fakepath\\easyTemplate.xlsx")
        self.driver.find_element(By.LINK_TEXT, "确定").click()

    def test_export_childrens(self):# 导出幼儿
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 div").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-2 div")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.CSS_SELECTOR, "th > input").click()
        self.driver.find_element(By.ID, "batch-output").click()

    def test_batch_delete_childrens(self):# 批量删除幼儿
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.NAME, "id").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(2) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(3) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(4) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(5) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(20) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(19) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(18) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(17) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(16) > td:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(16) input").click()
        self.driver.find_element(By.ID, "batch-delete").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()

    def test_in_childrens(self):
        self.driver.set_window_size(1226, 902)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 div").click()
        self.driver.find_element(By.CSS_SELECTOR, "#li-11 div").click()
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 div").click()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "离园幼儿").click()
        self.driver.find_element(By.LINK_TEXT, "入园").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    def test_del_childrens_archives(self): # 删除成长档案
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 div").click()
        self.driver.find_element(By.LINK_TEXT, "成长档案").click()
        element = self.driver.find_element(By.LINK_TEXT, "成长档案")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.NAME, "id").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-c:nth-child(5) input").click()
        self.driver.find_element(By.ID, "batch-delete").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()

    def test_del_childrens(self): # 删除幼儿
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)").click()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "删除").click()
        self.driver.find_element(By.LINK_TEXT, "确定").click()

    def test_add_childrens(self): # 添加幼儿
        # Test name: 添加幼儿
        # Step # | name | target | value
        # 1 | open | http://t2.aservice.langlangyun.com:5480/langyun/public/index.php/workplace/pub/login.html |
        self.driver.get("http://t2.aservice.langlangyun.com:5480/langyun/public/index.php/workplace/pub/login.html")
        # 2 | setWindowSize | 1226x902 |
        self.driver.set_window_size(1226, 902)
        # 3 | click | name=account |
        self.driver.find_element(By.NAME, "account").click()
        # 4 | type | name=account | 13006662818
        self.driver.find_element(By.NAME, "account").send_keys("13006662818")
        # 5 | type | name=password | langyun
        self.driver.find_element(By.NAME, "password").send_keys("langyun")
        # 6 | click | css=.btn-secondary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        # 7 | click | css=#li-2 .img-responsive:nth-child(1) |
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)").click()
        # 8 | selectFrame | index=2 |
        self.driver.switch_to.frame(2)
        # 9 | click | linkText=添加幼儿  |
        self.driver.find_element(By.LINK_TEXT, "添加幼儿 ").click()
        # 10 | selectFrame | index=0 |
        self.driver.switch_to.frame(0)
        # 11 | click | name=username |
        self.driver.find_element(By.NAME, "username").click()
        # 12 | type | name=username | 测试
        self.driver.find_element(By.NAME, "username").send_keys("测试")
        # 13 | click | css=.tabCon > .row |
        self.driver.find_element(By.CSS_SELECTOR, ".tabCon > .row").click()
        # 14 | click | name=birthday |
        self.driver.find_element(By.NAME, "birthday").click()
        # 15 | type | name=birthday | 2020-09-03
        self.driver.find_element(By.NAME, "birthday").send_keys("2020-09-03")
        # 16 | click | css=.laydate-btns-confirm |
        self.driver.find_element(By.CSS_SELECTOR, ".laydate-btns-confirm").click()
        # 17 | click | name=gardenDate |
        self.driver.find_element(By.NAME, "gardenDate").click()
        # 18 | type | name=gardenDate | 2020-05-15
        self.driver.find_element(By.NAME, "gardenDate").send_keys("2020-05-15")
        # 19 | click | name=gardenDate |
        self.driver.find_element(By.NAME, "gardenDate").click()
        # 20 | click | css=.laydate-btns-confirm |
        self.driver.find_element(By.CSS_SELECTOR, ".laydate-btns-confirm").click()
        # 21 | click | css=.col-xs-9 > .select-box |
        self.driver.find_element(By.CSS_SELECTOR, ".col-xs-9 > .select-box").click()
        # 22 | click | name=class |
        self.driver.find_element(By.NAME, "class").click()
        # 23 | select | name=class | label=小星星小班
        dropdown = self.driver.find_element(By.NAME, "class")
        dropdown.find_element(By.XPATH, "//option[. = '小星星小班']").click()
        # 24 | click | name=class |
        self.driver.find_element(By.NAME, "class").click()
        # 25 | click | name=parent[name][] |
        self.driver.find_element(By.NAME, "parent[name][]").click()
        # 26 | type | name=parent[name][] | wei liu
        self.driver.find_element(By.NAME, "parent[name][]").send_keys("wei liu")
        # 27 | type | name=parent[phone][] | 13008800729
        self.driver.find_element(By.NAME, "parent[phone][]").send_keys("13008800729")
        # 28 | click | name=parent[phone][] |
        self.driver.find_element(By.NAME, "parent[phone][]").click()
        # 29 | type | name=parent[phone][] | 13008800728
        self.driver.find_element(By.NAME, "parent[phone][]").send_keys("13008800728")
        # 30 | click | css=.col-xs-12 > .btn-secondary |
        self.driver.find_element(By.CSS_SELECTOR, ".col-xs-12 > .btn-secondary").click()
        # 31 | click | linkText=确定 |
        self.driver.find_element(By.LINK_TEXT, "确定").click()
        # 32 | click | name=birthday |
        self.driver.find_element(By.NAME, "birthday").click()
        # 33 | click | css=.laydate-prev-y |
        self.driver.find_element(By.CSS_SELECTOR, ".laydate-prev-y").click()
        # 34 | click | css=.laydate-prev-y |
        self.driver.find_element(By.CSS_SELECTOR, ".laydate-prev-y").click()
        # 35 | doubleClick | css=.laydate-prev-y |
        element = self.driver.find_element(By.CSS_SELECTOR, ".laydate-prev-y")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 36 | click | css=.laydate-btns-confirm |
        self.driver.find_element(By.CSS_SELECTOR, ".laydate-btns-confirm").click()
        # 37 | click | css=.col-xs-12 > .btn-secondary |
        self.driver.find_element(By.CSS_SELECTOR, ".col-xs-12 > .btn-secondary").click()

    def add_childrens_archives(self): # 添加成长档案
        self.driver.set_window_size(1226, 902)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)").click()
        self.driver.find_element(By.LINK_TEXT, "成长档案").click()
        self.driver.switch_to.frame(3)
        self.driver.find_element(By.LINK_TEXT, "新建成长档案 ").click()
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "children").click()
        dropdown = self.driver.find_element(By.ID, "children")
        dropdown.find_element(By.XPATH, "//option[. = '士大夫士大']").click()
        self.driver.find_element(By.ID, "children").click()
        self.driver.find_element(By.CSS_SELECTOR, "img:nth-child(5)").click()
        self.driver.find_element(By.NAME, "info").click()
        self.driver.find_element(By.NAME, "info").send_keys("好的啊实打实阿萨德大声道asadadasadas 大萨达啊")
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").send_keys("C:\\fakepath\\1.jpeg")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

    def test_select_childrens(self):# 查询幼儿
        self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".btn-secondary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 div").click()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("云001")
        self.driver.find_element(By.ID, "cx").click()

    def test_pages_childrens(self):
        self.driver.set_window_size(1936, 1096)
        self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#li-2 .img-responsive:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.LINK_TEXT, "2").click()
        self.driver.find_element(By.LINK_TEXT, "3").click()
        self.driver.find_element(By.LINK_TEXT, "4").click()
        self.driver.find_element(By.LINK_TEXT, "1").click()

