# –*–coding:utf-8 –*–
# 2021-03-29 18:22

# 不用正则表达式来查找文本模式
def isPhoneNumber(text):
	if len(text) != 12:
		return False
	for i in range(0, 3):
		if not text[i].isdecimal():
			return False
	if text[3] !='-':
		return False
	for i in range(4, 7):
		if not text[i].isdecimal():
			return False
	if text[7] != '-':
		return False
	for i in range(8, 12):
		if not text[i].isdecimal():
			return False
	return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.010-222-88688'
for i in range(len(message)):
	chuck = message[i :i + 12]
	#print(chuck)
	if isPhoneNumber(chuck):
		print('Phone number found:', chuck)
print('Done!')