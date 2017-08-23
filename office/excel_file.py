'''
	读取txt文档中的内容然后写入excel表中
'''
#python字符串转字典，key必须使用双引号
import json
import xlrd
import xlwt
import os
from xlutils.copy import copy

def getInfo(filepath):
	contentdict={}
	with open(filepath, 'rb') as fs:
		contentdict = json.loads(fs.read())
		

	return contentdict

def createnewExcel(condict,filepath):
	wb = xlwt.Workbook()
	data = wb.add_sheet('Info')
	i_index = 0
	j_index = 0
	for i in condict:
		data.write(i_index, j_index, i)
		for j in condict[i]:
			j_index +=1
			data.write(i_index, j_index, j)
		j_index = 0 #写完一行后，换行重头写
		i_index +=1

	wb.save(filepath)

def writeInfoToExcel(condict,filepath):
	if os.path.exists(filepath):
		rb = xlrd.open_workbook(filepath, formatting_info=True)
				
		#获取行数
		sheet = rb.sheet_by_index(0)
		i_index = sheet.nrows
		j_index = sheet.ncols
		
		wb = copy(rb)
		ws = wb.get_sheet(0)
		for i in condict:
			j_index = 0 #写完一行后，换行重头写
			ws.write(i_index, j_index, i)
			for j in condict[i]:
				j_index +=1
				ws.write(i_index, j_index, j)
			
			i_index +=1
		wb.save(filepath)
	else:
		print('create excel file')
		createnewExcel(condict, filepath)

if __name__=='__main__':
	
	contentdict = getInfo('info.txt')
	writeInfoToExcel(contentdict, 'info.xls')