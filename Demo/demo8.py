# –*–coding:utf-8 –*–
# 2021-03-23 15:17
while True:
	try:
		unit_price = float( input( '请输入商品的单价（元）:' ) )
		
		num = int( input( '请输入商品的数量:' ) )
		price = unit_price * num
		if unit_price<=0 or num <=0:
			print("请输入正确的单价或数量。")
			continue
		print( '需要支付' , price , '元:' )
		pay_me = float( input( '请您付账:' ) )
		
		while True:
			if  pay_me < price:
				print("请正确输入支付金额！")
				pay_me = float( input( '请付账:' ) )
			else:
				pay_you = pay_me - price
				if pay_me == price:
					print("谢谢惠顾")
					break
				else:
					print("找您:", pay_you, '元。')
					break
	except ValueError:
		print("请正确输入单价或数量。")
		break