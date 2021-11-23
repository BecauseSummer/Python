# –*–coding:utf-8 –*–
# 2021-06-24 10:03
import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):
	'''Test MathFunc.py '''
	def setUp(self):
		print(" do something before test.Prepare environment")
		
	def tearDown(self):
		print("do something after test clean up")
	
	def test_add(self):
		'''test method add(a ,b)'''
		self.assertEqual(3, add(1, 2))
		self.assertNotEqual(3, add(2, 2))
		
	def test_minus(self):
		'''test method minus (a,b )'''
		self.assertEqual( 1 , minus( 3 , 2 ) )
		
	def test_multi(self) :
		"""Test method multi(a, b)"""
		self.assertEqual( 6 , multi( 2 , 3 ) )
	
	def test_divide(self) :
		"""Test method divide(a, b)"""
		self.assertEqual( 2 , divide( 6 , 3 ) )
		self.assertEqual( 2.5 , divide( 5 , 2 ) )

if __name__ == '__main__':
	'''
	verbosity 设置
	0(静默模式):你只能获得总的测试用例数和总的结果比如总共100个失败20成功80
	1(默认模式):非常类似静默模式只是在每个成功的用例前面有个".”每个失败的用例前面有个“F”。
	2(详细模式):测试结果会显示每个测试用例的所有相关的信息，并且你在命令行里加入不同的参数可以起到—样的效果
	'''
	unittest.main(verbosity=2)