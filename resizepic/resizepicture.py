
'''
	修改图片的分辨率

'''
from PIL import Image
import os,sys

#修改某张图片大小
def resizePic(picname,new_picname, new_width, new_hight):
	img = Image.open(picname)
	out_img = img.resize((new_width, new_hight), Image.ANTIALIAS)
	out_img.save(new_picname)


#遍历某个目录下所有的文件，包括文件夹
def traverseFolderAndFile(pathname, outfilelist):
	alllist = []
	if pathname is None:
		print("failed")
	else:
		alllist= os.listdir(pathname)
	
	for i in range(len(alllist)):
		newpathname = pathname + '\\' + alllist[i]
		if os.path.isdir(newpathname):
			traverseFolderAndFile(newpathname, outfilelist)
		elif os.path.isfile(newpathname):
			outfilelist.append(newpathname)
		else:
			print('it\'s a special file (socket, FIFO, device file')
			


	return outfilelist


if __name__ == '__main__':

	outfilelist =[]
	print(traverseFolderAndFile('E:\\svnwork\\workspace\\github', outfilelist))
	for i in range(len(outfilelist)):
		resizePic(outfilelist[i], 'new_' + outfilelist[i], 960, 800)

	#resizePic('road.jpg', 'new_road.jpg', 960, 800)
