# coding=utf-8
import os, unittest
from HTMLTestRunner import HTMLTestRunner
from .page import webdriver_initialzation

if __name__ == '__main__':
    unittest.main(['-s', '--alluredir','result'])
    suite = unittest.TestSuite()
    suite.addTests( unittest.TestLoader().loadTestsFromTestCase( webdriver_initialzation.CaseLogin ) )
    filepath = 'D:/Python/langyun_automate/Report'
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    fp = open( './Report/HTMLReport.html' , 'wb' )
    runner = HTMLTestRunner( stream = fp , title = 'MathFunc Test Report' ,
                             description = 'generated by HTMLTestRunner.' , verbosity = 2 )
    runner.run( suite )
    fp.close()
    os.system('allure generate result -o report --clean')
    
