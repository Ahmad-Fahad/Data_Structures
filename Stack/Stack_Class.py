class Stack:
	def __init__(self):
		self.lst = list()
	def push(self, item):
		self.lst.append(item)
	def pop(self):
		return self.lst.pop()
	def is_empty(self):
		if self.lst == []:
			return True
		return False
		
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)

while not st.is_empty():
	print(st.is_empty())
	pp = st.pop()
	print(pp)