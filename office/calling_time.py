'''
	根据从移动导出的通话记录，统计出这个月的通话时间总长

'''
import os
import xlrd
import time
import re

def getSeconds(lst_time):
	ls_time = re.findall(r'(\d+)', lst_time)
	seconds = 0
	if len(ls_time) == 1:
		seconds = int(ls_time[0])
	elif len(ls_time) == 2:
		seconds = int(ls_time[0]) * 60 + int(ls_time[1])
	elif len(ls_time) == 3:
		seconds = int(ls_time[0]) *60*60 +int(ls_time[1]) * 60 + int(ls_time[2])
	else:
		print('param error: paser time failed')
	return seconds

def statisticsCallingTime(filepath):
	if os.path.exists(filepath):
		rb = xlrd.open_workbook(filepath, formatting_info=True)
		#获取行数
		sheet = rb.sheet_by_index(0)
		index = sheet.nrows
		print('行数：' + str(index) + '列数' + str(sheet.ncols))
		#print(sheet.row_values(1))
		#print(sheet.col_values(5))
		lst = sheet.col_values(3)
		times =sheet.col_values(5)
		for i in range(len(lst)):
			if lst[i] == u'主叫':
				#calling_time = time.strptime(times[i], "%H:%M:%S")
				calling_time = getSeconds(times[i])

				print(calling_time)
			elif lst[i] == u'被叫':
				#becalled_time = time.strptime(times[i], "%H:%M:%S")
				becalled_time = getSeconds(times[i])
				print(becalled_time)
			else:
				print('nothing to do')

if __name__ =='__main__':
	statisticsCallingTime('13823174936.xls')
