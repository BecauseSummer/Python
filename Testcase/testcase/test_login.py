# –*–coding:utf-8 –*–
# 2021-10-27 15:16
import os

import pytest

class Test_Login:
    def test_login(self):
        print("测试")

    def test_demo2(self):
        print("第二个测试用例")
        # assert 1 == 2

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')