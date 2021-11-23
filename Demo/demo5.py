# –*–coding:utf-8 –*–
# time:2021-02-26 09:56
'''
简易计算器
'''
import wx

class get_the_data(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, '靓仔计算器', size=(600, 700))
		panel = wx.Panel(self, -1)
		wx.StaticText( panel , -1 , "Operator:" ,
		               (5 , 10) )
		list = [ "+" , "-" , "*" , "/" ]
		
			
		self.operation = wx.ComboBox( panel , -1 , value = '请选择' , choices = list , style = wx.CB_SORT , pos = (110 , 5) ,
									  size = (60 , 25) )
		
		wx.StaticText( panel , -1 , "数字:" , (5 , 40) )
		self.number1 = wx.TextCtrl( panel , pos = (110 , 40) , size = (40 , 20) )
		self.number2 = wx.TextCtrl( panel , pos = (160 , 40) , size = (40 , 20) )
		
		wx.StaticText( panel , -1 , "求值:" , (5 , 70) )
		self.btn = wx.Button( panel , label = "=" , pos = (110 , 70) , size = (90 , 20) )
		self.Bind( wx.EVT_BUTTON , self.operation_Digital , self.btn )
		
		wx.StaticText( panel , -1 , "结果:" , (5 , 110) )
		self.get_result = wx.TextCtrl( panel , pos = (55 , 150) , size = (150 , 90) ,
									   style = wx.TE_MULTILINE | wx.HSCROLL )
		
	
	def operation_Digital( self , event ) :
		num1 = self.number1.GetValue()
		num2 = self.number2.GetValue()
		op = self.operation.GetValue()
		if num1.isdigit() and num2.isdigit() :
			if op == "+" :
				result = int( num1 ) + int( num2 )
			elif op == "-" :
				result = int( num1 ) - int( num2 )
			elif op == "*" :
				result = int( num1 ) * int( num2 )
			elif op == "/" :
				if int( num2 ) != 0 :
					result = int( num1 ) / int( num2 )
				else :
					result = "Please input again."
			else :
				pass
		else :
			result = "Sorry, wrong input, please re-enter."
		
		self.get_result.SetValue( str( result ) )

		
if __name__ == '__main__':
	app = wx.App()
	frame = get_the_data()
	frame.Show()
	app.MainLoop()