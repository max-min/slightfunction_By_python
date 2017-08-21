
''''
	@敏感词汇

'''

def getFilteredWordList():
	wordList =[]
	with open('filtered_words.txt', 'r', encoding='utf-8') as f:
		for line in f.readlines():
			wordList.append(line.strip()) # 把末尾的'\n'删掉
	print(wordList)
	return wordList


def IsRightWord(message):
	wordlist = getFilteredWordList()
	for word in wordlist:
		if word in message:
			news = message.replace(word, '*'*len(word))
			print(news)
			return 0
	
	print(message)
	return 1



if __name__=='__main__':

	#message = input("\n\n input the word you want \n")
	#IsRightWord(message)
	IsRightWord('程序员都是死肥宅')

	