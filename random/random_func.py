
'''

	随机生成n*4的license(优惠码)的处理，包含数字和字母
'''
import random


total_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def genera_random(nums):
	final_str = ''
	for i in range(0,nums):
		tmp = ''.join(random.sample(total_str, 4))
		final_str += tmp + '-'
	return final_str[:-1] # 除去最后多加的一个'-'


if __name__ == '__main__':
	print(genera_random(4))
