data = [None]*20

data[0]  = 5
data[2]  = 12
data[3]  = 8
data[7]  = 13
data[9]  = 3
data[12] = 6
data[15] = 9

nextPointer = [None]*20

nextPointer[0]  = 3
nextPointer[2]  = 9
nextPointer[3]  = 12
nextPointer[7]  = 15
nextPointer[9]  = 7
nextPointer[12] = 2

pre_index = [None]*20

pre_index[0]  = None
pre_index[2]  = 12
pre_index[3]  = 0
pre_index[7]  = 9
pre_index[9]  = 2
pre_index[12] = 3
pre_index[15] = 7

head = 0

i = head
while nextPointer[i] != None:
	print(i, data[i])
	index = i
	i = nextPointer[i]

print("Last Node")
print(index, data[index])
print()

i = index
while pre_index[i] != None:
	i = pre_index[i]
	print(i, data[i])