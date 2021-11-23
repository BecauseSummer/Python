# –*–coding:utf-8 –*–
# 2021-04-14 14:26
from Demo.drive.auto import webUI_init
from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {
    		'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}

options.add_argument("disable-infobars")
web = webUI_init('chrome', 'https://www.baidu.com',options)
web.wait(1)
web.input_text(By.ID, 'kw', 'python')
web.click_element(By.ID, 'su')
web.wait(1)
web.quit()