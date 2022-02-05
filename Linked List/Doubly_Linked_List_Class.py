class Node:
	def __init__(self, data=None, next=None, prev=None):
		self.data = data
		self.next = next  
		self.prev = prev
		
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
		first_node      = self.head.next	
		node            = Node(data, first_node)
		self.head.next  = node
		if first_node:
			first_node.prev = node


	def append(self, data):
		node = Node(data)
		if self.head.next == None:
			self.head.next = node
			return
		i = self.head.next
		while i.next:
			i  = i.next
		node.prev = i
		i.next    = node

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
		node.prev = i

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
			i.next.prev   = pre_data
			pre_data.next = i.next

	def search(self, data):
		i = self.head.next
		while i:
			if i.data == data:
				return i
			i = i.next
		return False

	def reverse(self):
		i = self.head.next
		while i.next:
			i = i.next
		c_node = i
		r_lst  = []
		r_lst.append(c_node)
		while c_node.prev:
			c_node = c_node.prev
			r_lst.append(c_node)
		return r_lst

	def test(self):
		print()
		print("Head")
		print(repr(self.head.data))
		print(repr(self.head.next))
		print(repr(self.head.prev))
		print()
		print("Node 1")
		print(repr(self.head.next.data))
		print(repr(self.head.next.next))
		print(repr(self.head.next.prev))
		print()
		

		self.prepend(99)
		print()
		print("Head")
		print(repr(self.head.data))
		print(repr(self.head.next))
		print(repr(self.head.prev))
		print()
		print("Node 1")
		print(repr(self.head.next.data))
		print(repr(self.head.next.next))
		print(repr(self.head.next.prev))
		print()


		print("Node 2")
		print(repr(self.head.next.next.data))
		print(repr(self.head.next.next.next))
		print(repr(self.head.next.next.prev))



ll = Linked_List()

ll.append(5)
ll.append(10)
ll.prepend(1)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print(repr(ll))
rev_lst = ll.reverse()

for i in rev_lst:
	print(repr(i))

ll.prepend(99)
ll.append(111)
ll.insert(5, 5555)
ll.remove(40)

print(repr(ll))
rev_lst = ll.reverse()

for i in rev_lst:
	print(repr(i))

"""

ll.test()





x = 5
if ll.search(x) == False:
	print("Not Found")
else:
	print("Found")

ll.append(50)
ll.insert(10,33)




ll.remove(5)
print(repr(ll))
"""


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