
'''
	 创建一个区域快
'''
import datetime
import hashlib

class Block(object):
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()


	def hash_block(self):
		sha = hashlib.sha256()
		shastr = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
		sha.update(shastr)
		return sha.hexdigest()



#创建区域源
def create_genesis_block():
	block = Block(0, datetime.datetime.now(), 'Genesis Block', '0')
	return block

#
def next_block(last_block):
	next_index = last_block.index + 1
	next_timestamp = datetime.datetime.now()
	next_date = 'next_new_block_' + str(next_index)
	next_hash = last_block.hash
	return Block(next_index, next_timestamp, next_date, next_hash) 



if __name__=='__main__':
	blockchain = [create_genesis_block()]

	#last_block = blockchain[0]
	for i in range(20):
		last_b = blockchain[i]
		blockchain.append(next_block(last_b))

	for i in blockchain:
		print('Block #{}has been added to the blockchain'.format(i.index))
		print('Hash:{}\n'.format(i.hash))