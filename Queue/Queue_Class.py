class Queue:
	def __init__(self):
		self.lst = list()
	def enQueue(self, item):
		self.lst.append(item)
	def deQueue(self):
		return self.lst.pop(0)
	def is_empty(self):
		if self.lst == []:
			return True
		return False
		
st = Queue()
st.enQueue(1)
st.enQueue(2)
st.enQueue(3)
st.enQueue(4)
st.enQueue(5)

while not st.is_empty():
	print(st.is_empty())
	pp = st.deQueue()
	print(pp)