# –*–coding:utf-8 –*–
# 2021-06-24 10:10
import unittest
import os
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
	file_path = 'D:/Python/BS/Report'
	if not os.path.exists(file_path):
		os.makedirs(file_path)
	fp = open( './Report/HTMLReport.html' , 'wb')
	runner = HTMLTestRunner(stream = fp ,title = 'MathFunc Test Report', description = 'generated by HTMLTestRunner.', verbosity = 2)
	runner.run( suite )
	fp.close()
	