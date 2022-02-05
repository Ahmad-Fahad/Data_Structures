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

#......Pre Insert...........
#.......New Node...........
n_data  = 777
n_index = 17

#..................
#....main algo.....
temp              = head
head              = n_index
data[head]        = n_data
nextPointer[head] = temp

#......Traverse...........
i = head
while nextPointer[i] != None:
	print(data[i])
	i = nextPointer[i]

print(".................")

#......Middle Insert...........
#.......New Node...........

n_data  = 11111
n_index = 18

#.....After......

pre_data = 3

#................
#................
#...search pre data....

i = head
while nextPointer[i] != None:
	if pre_data == data[i]:
		index = i
		break
	i = nextPointer[i]

#....main algo.....
temp                 = nextPointer[index]
nextPointer[index]   = n_index
nextPointer[n_index] = temp
data[n_index]        = n_data 

#......Traverse...........
i = head
while nextPointer[i] != None:
	print(data[i])
	i = nextPointer[i]

print(".................")

#......Post Insert...........
#.......New Node...........

n_data  = 888888
n_index = 19

#................
#...search last data....

i = head
while nextPointer[i] != None:
	index = i
	i     = nextPointer[i]
	

#....Main Algo.....

nextPointer[index] = n_index
data[n_index]      = n_data

#......Traverse...........

i = head
while nextPointer[i] != None:
	print(data[i]) # little problem to be fixed. insert ok . print not show
	i = nextPointer[i]
	#print(data[i])  

print(".................")