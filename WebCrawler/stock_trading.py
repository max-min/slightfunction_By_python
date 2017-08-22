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
			except:
				continue
		#print(lst)

if __name__ =='__main__':

	lst = []
	getStockList( lst, 'http://quote.eastmoney.com/stocklist.html')
	#print(lst)