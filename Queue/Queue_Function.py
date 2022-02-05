def enQueue(i):
	lst.append(i)
def deQueue():
	return lst.pop(0)

lst = ['a','b','c','d','e']
enQueue('t')
enQueue('g')
enQueue('h')
print(lst)
d = deQueue()
print(d)
d = deQueue()
print(d)
d = deQueue()
print(d)
d = deQueue()
print(d)
d = deQueue()
print(d)

print(lst)