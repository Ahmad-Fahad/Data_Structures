class Queue:
	def __init__(self, Max_size):
		self.lst       = []
		self.Q_size    = Max_size
		self.Present_Q = 0
		self.front	   = 0
		self.rear	   = 0
	def enQueue(self, data):
		if self.is_full():
			print("Queue is full")
			return
		print("Inserting", data)
		self.lst.insert(self.rear, data)
		self.rear       = (self.rear+1) % self.Q_size
		self.Present_Q += 1
	def deQueue(self):
		if self.is_empty():
			print("Queue is empty")
			return
		data            = self.lst[self.front]
		self.front      = (self.front+1) % self.Q_size
		self.Present_Q -= 1
		return data
	def is_empty(self):
		if self.Present_Q == 0:
			return True
		return False
	def is_full(self): 
		if self.Present_Q == self.Q_size:
			return True
		return False
		
q = Queue(5)
print(q.lst)
print(q.front)
print(q.rear)

q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)

print(q.lst)
print(q.front)
print(q.rear)

q.enQueue(6)
q.enQueue(7)

print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())
print(q.deQueue())

print(q.lst)
print(q.front)
print(q.rear)