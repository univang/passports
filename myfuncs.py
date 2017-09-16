import re

def compare(str1, str2):
	# i.tag in rowEl[0]
	# !!!!!!!!!!!!!!!! valids = re.findall(r"[^A-Za-z]+", my_string)
	key1 = re.sub(r"[^A-Za-zА-ЯЁа-яё]+", '', str1)
	key2 = re.sub(r"[^A-Za-zА-ЯЁа-яё]+", '', str2)
	
	if key1 == key2:
		# print('Found!')
		return 1
	else:
		# print('Fail!')
		return 0