'''
	抓取某个网站的股票交易信息
'''
import requests
from bs4 import BeautifulSoup
import re
headers = {
	'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
	'Referer':"http://tieba.baidu.com"
}

def getHTMLText(url):
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	return r.text

def getStockList(lst, stockurl):
	html = getHTMLText(stockurl)
	if html != '':
		soup = BeautifulSoup(html, 'html.parser')
		a = soup.find_all('a')
		
		for i in a:
			try:
				href = i.attrs['href']
				lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
				if len(lst) == 10:
					break
			except:
				continue
		#print(lst)

def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        if html=="":
        	continue
        infoDict = {}
        soup = BeautifulSoup(html, 'html.parser')
        stockInfo = soup.find('div',attrs={'class':'stock-bets'})
        print(stockInfo)
        '''
        股票数组都是事实数据，没办法重页面直接获取
        name = stockInfo.find(attrs={'class':'bets-name'})[0]
        infoDict.update({'股票名称': name.text.split()[0]})
        keyList = stockInfo.find('dt')
        valueList = stockInfo.find('dd')
        for i in range(len(keyList)):
        	key = keyList[i].text
        	val = valueList[i].text
        	infoDict[key] = val
        with open(fpath, 'a+', encoding='utf-8') as f:
        	f.write( str(infoDict) + '\n' )
        	count = count + 1
        	print("\r####当前进度: {:.2f}%".format(count*100/len(lst)),end="")
		'''

if __name__ =='__main__':

	lst = []
	getStockList( lst, 'http://quote.eastmoney.com/stocklist.html')
	#print(lst)
	getStockInfo(lst, 'http://quote.eastmoney.com/', 'BaiduStockInfo.txt')