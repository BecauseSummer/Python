# –*–coding:utf-8 –*–
# 2021-03-29 11:50
import json

filename = 'result.json'


def input_json_data_from_file( path ) :
	"""
	从文件中获取json数据
	:param path: 文件路径
	:return json_data: 返回转换为json格式后的json数据
	"""
	try :
		with open( path , 'rb+' ) as f :
			try :
				json_data = json.load( f )
			except Exception as e :
				print( 'json数据格式不正确：' + str( e ) )
		return json_data
	except Exception as e :
		print( '文件不存在：' + str( e ) )


def analyze_json( jsons ) :
	"""
	解析传进来的jsons,将jsons解析成key-value并输出
	:param jsons: 需要解析的json字符串
	:return:
	"""
	# json_data = json.loads(jsons)
	# if isinstance(json_data, dict):
	# isinstance函数是Python的内部函数，他的作用是判断jsons这个参数是否为dict类型
	# 如果是的话返回True，否则返回False
	if isinstance( jsons , dict ) :
		for key in jsons.keys() :
			key_value = jsons.get( key )
			if isinstance( key_value , dict ) :
				analyze_json( key_value )
			elif isinstance( key_value , list ) :
				for json_array in key_value :
					analyze_json( json_array )
			else :
				print( str( key ) + " = " + str( key_value ) )
	elif isinstance( jsons , list ) :
		for json_array in jsons :
			analyze_json( json_array )
	else :
		print( '请输入正确的json数据' )


def output_value( jsons , key ) :
	"""
	通过参数key，在jsons中进行匹配并输出该key对应的value
	:param jsons: 需要解析的json串
	:param key: 需要查找的key
	:return:
	"""
	key_value = ''
	if isinstance( jsons , dict ) :
		for json_result in jsons.values() :
			if key in jsons.keys() :
				key_value = jsons.get( key )
			else :
				output_value( json_result , key )
	elif isinstance( jsons , list ) :
		for json_array in jsons :
			output_value( json_array , key )
	if key_value != '' :
		print( str( key ) + " = " + str( key_value ) )


def main( path ) :
	json_data = input_json_data_from_file( path )
	print( '原始数据：' + str( json_data ) )
	
	print( '……………………………………调用解析……………………………………' )
	# 调用解析
	print( '将jsons1解析后的结果如下：' )
	analyze_json( json_data )
	
	print( '……………………………………调用查找……………………………………' )
	# 调用查找
	print( '查找jsons1中t2key的value值如下：' )
	output_value( json_data , "orderId" )
	print( '……………………………………运行结束……………………………………' )


if __name__ == '__main__' :
	main( rb"result.json" )