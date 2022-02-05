class Queue:
	def __init__(self):
		self.lst   = []
		self.front = 0
		self.rear  = 0
	def enQueue(self, item):
		self.lst.insert(self.rear, item)
		self.rear += 1
	def deQueue(self):
		item = self.lst[self.front]
		self.front += 1
		return item
	def is_empty(self):
		if self.front == self.rear:
			return True
		return False
		
q = Queue()
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)

while not q.is_empty():
	print(q.is_empty())
	qq = q.deQueue()
	print(qq)