# –*–coding:utf-8 –*–
# 2021-04-13 19:56
import unittest, ddt, os, allure
@ddt.ddt
class DDTExample(unittest.TestCase):
	@classmethod
	def setUpClass(  cls ) -> None:
		print(cls.__name__)
	@allure.title("结束")
	@classmethod
	def tearDownClass( cls )-> None:
		print('...end...')
	@allure.title("数据")
	@ddt.data(
		[1, 2],
		[3, 4],
		[5, 6]
	)
	@ddt.unpack
	def test_add( self, a, b ):
		print(a + b)
	
		
if __name__ == '__main__':
    unittest.main(['-s', '--alluredir','result'])
os.system('allure generate result -o report --clean')