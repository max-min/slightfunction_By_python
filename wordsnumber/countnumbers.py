
'''
	统计一个纯英文文本中单词的个数
'''




def countWordsNumber(filename):
	f = open(filename, 'r')

	content = f.read()
	rows = content.split('\n')
	wordnumber = 0
	for i in range(len(rows)):
		wordlist = rows[i].split(' ')
		wordnumber += len(wordlist)
		'''
		标点符号一般会和最后一个单词连在一起，故不需要额外处理
		for j in range(len(wordlist)):
			if wordlist[j] == ',' or wordlist[j] ==';' or wordlist[j]=='.':
				wordnumber = wordnumber -1
		'''
	return wordnumber


if __name__ =='__main__':
	print(countWordsNumber('test.txt'))

