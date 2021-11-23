# –*–coding:utf-8 –*–
# time:2021-01-26 16:50
import unittest
import HTMLTestRunner

class DemoTest(unittest.TestCase):
    def test_one(self):
        print('1')
    def test_two(self):
        print('2')

if __name__ == '__main__':
    print('start')
    suite = unittest.TestSuite()
    filename = './result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='TEST', description='报告描述')
    runner.run(suite)
    fp.close()