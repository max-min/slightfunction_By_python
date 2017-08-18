'''
 @随机生成的字符串保存到非对称的redis中
'''

import redis
import random

class RedisHandle(object):

	def __init__(self):
		self.r = None
		pass


	def connectRedis(self, ip, port):
		self.r = redis.Redis(host=ip, port=port)
		if self.r is None:
			print('connect failed')
			return -1
		else:
			print('connnect success')
			return 0



total_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def genera_random(nums):
	final_str = ''
	for i in range(0,nums):
		tmp = ''.join(random.sample(total_str, 4))
		final_str += tmp + '-'
	return final_str[:-1] # 除去最后多加的一个'-'

if __name__=='__main__':
	redisObj = RedisHandle()
	if redisObj.connectRedis('10.72.66.74', 6379) == 0:
		for i in range(200):
			strs = genera_random(4)
			key = 'random_'+str(i)
			redisObj.r.set(key, strs)

	#print(redisObj.r.get('random_199'))
	#print(redisObj.r.get('random_150'))


	