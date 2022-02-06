class InvalidOperationException:
	pass

# id set/ get 
# record object 

class Record:
	def __init__(self, id, data):  
		self.id   = id
		self.data = data
	def get_id(self):
		return self.id
	def set_id(self, id):
		self.id = id
	def __str__(self):
		return str(self.id+" "+self.data)

 # methods : display_table insert search delete
 # maintain hash table

class Hash_Table:
	def __init__(self, size = 11):
		self.m = size
		self.table = [None]*self.m
		self.n = 0

	def Hash(self, key):
		return (key % self.m)

	def insert(self, record):
		key   = record.get_id()
		h     = self.Hash(key)
		index = h
		for i in range(1, self.m):  # ? --> 1
			if self.table[index] is None or self.table[index].get_id() == -1: # ? -1 for deleted
				self.table[index] = record  # ? why insert an object into property/ attribute
				self.n += 1  # ?
				return
			if self.table[index].get_id() == key:
				raise InvalidOperationException("Duplicate key")
			index = (h + i) % self.m
		return None

	def search(self, key):
		h     = self.Hash(key)
		index = h
		for i in range(1, self.m):
			if self.table[index] is None:
				return None
			if self.table[index].get_id() == key:
				return self.table[index]
			index = (h + i) % self.m
		return None

	def display_table(self):  # ? problem
		for i in range(self.m):
			print(f"[ {i} ]", end='')
			if self.table[i] is not None and self.table[i].get_id() != -1:
				print(self.table[i])
			else:
				print("_")

	def delete(self, key):
		h     = self.Hash(key)
		index = h
		for i in range(1, self.m): 
			if self.table[index] is None:
				return None
			if self.table[index].get_id == key:
				temp = self.table[index]
				self.table[index].set_id(-1)
				self.n = -1
				return temp
			index = (h + i) % self.m



	
# code commenced 
size  = int(input("Enter hash table size : "))
h_table = Hash_Table(size) 

while True:
	print("1-Inser\n2-Search\n3-Delete\n4-Display\n5-Exit")
	option = int(input("Enter Option : "))
	if option == 1:
		id     = int(input("Enter Id : "))
		data   = input("Enter data : ")
		record = Record(id, data)
		h_table.insert(record)
	elif option == 2:
		id     = int(input("Enter Id : "))
		record = h_table.search(id)
		if record is None:
			print("Not Found")
		else:
			print(record)
	elif option == 3:
		id   = int(input("Enter Id : "))
		h_table.delete(id)
	elif option == 4:
		h_table.display_table()
	elif option == 5:
		break
	else:
		print("Invalid Option")
	print()

