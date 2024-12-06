l=['one','two','three','four','five','six']

print(l)

#Append a new element to the list.
l.append(['seven','eight'])

print(l)

l.extend(['nine','ten'])

print(l)

#Insert an element at the third position.

l.insert(2,'newNUM')
print(l)

#Remove an element from the list.
#l.remove('newNUM')
l.pop(2)
print(l)

#Sort the list in ascending order.
l.sort(key=str)
print(l)

m=sorted(l,key=str)
print(m)