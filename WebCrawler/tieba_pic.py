'''

	@抓取某贴吧上图片


'''
# urllib2 = urllib.request
import urllib.request
import re
from bs4 import BeautifulSoup
headers = {
	'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
	'Referer':"http://tieba.baidu.com"
}


def getPicSrc(urlsrc):
	req = urllib.request.Request(url=urlsrc, headers = headers)
	html = urllib.request.urlopen(req).read()
	html = html.decode('utf-8')
	p = re.compile(u'<img.+?class="BDE_Image".+?>')
	list_of_pic = p.findall(html)
	print(list_of_pic)
	return list_of_pic

def downloadPic(listPic):
	counter = 0
	for i in listPic:
		soup = BeautifulSoup(i, 'html.parser')
		url = soup.img['src']
		#req = urllib.request.Request(url=url, headers=headers)
		#pic = urllib.request.urlopen(url).
		pic = urllib.request.urlopen(url).read()
		file = open('E:\\pic\\'+str(counter) + '.jpg','wb+')
		file.write(pic)
		file.close()
		counter += 1
		
if __name__ == '__main__':
	url='http://tieba.baidu.com/p/2166231880'
	downloadPic(getPicSrc(url))