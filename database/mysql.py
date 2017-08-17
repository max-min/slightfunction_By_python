import random
import pymysql

class DataBase(object):

	def __init__(self, dbtype, ip, port, user, password, name):
		self.dbtype = dbtype
		self.ip = ip
		self.port = port 
		self.user = user 
		self.password = password
		self.dbname = name


	def connectDB(self):
		conn =''
		if self.dbtype == 'Mysql':
			conn = pymysql.connect(host=self.ip, port=self.port, user=self.user, passwd=self.password, db=self.dbname, charset='utf8')  
		elif self.dbtype == 'Oracle':
			pass
		elif self.dbtype == 'SQLserver':
			pass
		else :
			print('unknow database type')
			return ''
		self.connhandle = conn
		self.cursorHandle = self.connhandle.cursor(pymysql.cursors.DictCursor) # 这样查询的为字典

	def queryDB(self, sqlstatement):
		self.cursorHandle.execute(sqlstatement)
		ResultList = self.cursorHandle.fetchall()
		return ResultList

	def createTable(self, tablename, args):

		#sqls = 'create table '+tablename + ' (id int NOT NULL AUTO_INCREMENT,' + args+' varchar(32), PRIMARY KEY(id) engine=innodb)'
		sqls = 'create table '+tablename + ' (id int not null primary key ,' + args+' varchar(32))'
		self.cursorHandle.execute(sqls)

	def updateDB(self, tablename,idindex, numbers):
		sqls= 'replace into ' + tablename +'(id, license_number) values('+str(idindex)+',\''+ numbers +'\')'
		self.cursorHandle.execute(sqls)

		print(sqls + 'execute !!!')

	def closeDB(self):
		self.cursorHandle.close()
		self.connhandle.close()



total_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def genera_random(nums):
	final_str = ''
	for i in range(0,nums):
		tmp = ''.join(random.sample(total_str, 4))
		final_str += tmp + '-'
	return final_str[:-1] # 除去最后多加的一个'-'

if __name__ == '__main__':
	
	dbconObj = DataBase('Mysql', '10.72.66.74', 3306, 'root', 'zxm10', 'usmsc')
	
	if dbconObj.connectDB() == '':
		print('connect database failed')
	else:
		#dbconObj.createTable('t_cfg_python', 'license_number')
		for i in range(0,200):
			strs = genera_random(4)
			print('i:' + str(i) + ' numbers:' + strs)
			dbconObj.updateDB('t_cfg_python', i, strs)
		dbconObj.connhandle.commit()