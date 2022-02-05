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

head = 0

print(data)
print(nextPointer)


#......Traverse............

i = head
while nextPointer[i] != None:
	print(data[i])
	i = nextPointer[i]

#......Search...............

s = 13
i = head
while nextPointer[i] != None:
	if s == data[i]:
		index = i
		break
	preData = data[i]
	i = nextPointer[i]

print(preData, index)
