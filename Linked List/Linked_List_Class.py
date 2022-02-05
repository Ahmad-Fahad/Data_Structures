class Node:
	def __init__(self, data=None, next=None):
		self.data=data
		self.next=next  # always a object
	def __repr__(self):
		return repr(self.data)

class Linked_List:
	def __init__(self):
		self.head = Node()
	def __repr__(self):
		nodes = list()
		i     = self.head.next
		while i:
			nodes.append(repr(i))
			i = i.next
		return ",".join(nodes)

	def prepend(self, data):
		node           = Node(data, self.head.next) #self.head.next -->next of head now_ next of node1
		self.head.next = node

	def append(self, data):
		node = Node(data)
		if self.head.next == None:
			self.head.next = node
			return
		i = self.head.next
		while i.next:
			i  = i.next
		i.next = node

	def insert(self, pre_data, data):
		node = Node(data)
		i = self.head.next
		while i:
			if i.data == pre_data:
				break
			i = i.next
		temp      = i.next
		i.next    = node
		node.next = temp 

	def remove(self, data):
		pre_data = self.head
		i = self.head.next
		while i:
			if i.data == data:
				break
			pre_data = i
			i = i.next
		if i == None:
			return None
		if pre_data == self.head:
			self.head.next = i.next
		else:
			pre_data.next = i.next

	def search(self, data):
		i = self.head.next
		while i:
			if i.data == data:
				return i
			i = i.next
		return False



ll = Linked_List()

ll.append(5)
ll.append(10)
ll.prepend(1)

x = 5
if ll.search(x) == False:
	print("Not Found")
else:
	print("Found")

ll.append(50)
ll.insert(10,33)
print(repr(ll))
ll.remove(5)
print(repr(ll))


"""
	def insert(self, pre_data, data):
		i = self.head.next
		while i:
			if i.data == pre_data:
				node = Node(data, i.next)
				i.next = node
				break
			i = i.next
"""