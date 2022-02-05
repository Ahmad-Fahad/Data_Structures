class Node:
	def __init__(self, data=None):
		self.data  = data
		self.left  = None
		self.right = None
	def add_left(self, node):
		self.left = node
	def add_right(self, node):
		self.right = node

def create_Tree():
	n_2 = Node(2)
	n_7 = Node(7)
	n_9 = Node(9)
	n_2.add_left(n_7)
	n_2.add_right(n_9)
	n_1 = Node(1)
	n_6 = Node(6)
	n_7.add_left(n_1)
	n_7.add_right(n_6)
	n_5  = Node(5)
	n_10 = Node(10)
	n_6.add_left(n_5)
	n_6.add_right(n_10)
	n_8 = Node(8)
	n_9.add_right(n_8)
	n_3 = Node(3)
	n_4 = Node(4)
	n_8.add_left(n_3)
	n_8.add_right(n_4)
	return n_2

def pre_Order(node):
	print(node.data, end=" ")
	if node.left:
		pre_Order(node.left)
	if node.right:
		pre_Order(node.right)

def post_Order(node):
	if node.left:
		post_Order(node.left)
	if node.right:
		post_Order(node.right)
	print(node.data, end=" ")

def in_Order(node):
	if node.left:
		in_Order(node.left)
	print(node.data, end=" ")
	if node.right:
		in_Order(node.right)

if __name__ == "__main__":
	root = create_Tree()
	pre_Order(root)
	print()
	print("............................")
	post_Order(root)
	print()
	print("............................")
	in_Order(root)

