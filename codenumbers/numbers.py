'''

   读取某个文件夹下所有的代码文件，统计已经写的代码行数，注释行数，空白行数
'''

#
#
#
import os

def countNumbers(filenames):
	code_lines = 0
	comment_lines = 0
	blank_lines = 0
	
	for filename in filenames:
		f = open(filename, 'rb')
		commnet_first_flag = False
		for line in f:
			line = line.decode('utf-8') # 中文编码的可以能会出现问题。
			print(line)
			if commnet_first_flag == True:
				comment_lines +=1
				if line[0] == '\'' and line[1] == '\'' and line[2] =='\'':
					commnet_first_flag = False
				else :
					continue
				
			else:
				if line[0] == '\r' and line[1] == '\n':
					blank_lines +=1
				elif line[0] == '#':
					comment_lines +=1
				elif line[0] == '\'' and line[1] == '\'' and line[2] =='\'':
					commnet_first_flag = True
					comment_lines +=1
				else:
					code_lines +=1

	return code_lines, comment_lines, blank_lines
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

if __name__ =='__main__':
	filelist = []
	traverseFolderAndFile('E:\\svnwork\\workspace\\github', filelist)
	#filelist.append('numbers.py')
	numbers = 0
	numbers += countNumbers(filelist)
	
	print('code_lines(%d), comment_lines(%d), blank_lines(%d)'%(numbers[0], numbers[1], numbers[2]))