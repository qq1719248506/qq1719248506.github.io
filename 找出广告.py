def compare_strings(str1, str2):
	result = []
	# 获取最小长度作为循环次数上限
	min_length = len(min(str1, str2))
	for i in range(min_length):
		if str1[i] != str2[i]:
			break
	return i

with open ('.\\index.m3u8','r',encoding='utf-8') as file:
	k=0
	i=0
	s1=""
	l=0
	for item in file:
		if item.find("#EXTINF")==0:
			#下一行就是影片地址
			k=1
			continue
		if k==1:
			k=0
			i=i+1
			if i==1:
				s1=item
			if i==2:
				#利用第一个和第二个影片地址找出最大相同部分的长度，然后减3，以免错杀。
				l=compare_strings(s1,item)-3
				#print(l)
			if i>2:
				if compare_strings(s1,item)<l:
					print(item)