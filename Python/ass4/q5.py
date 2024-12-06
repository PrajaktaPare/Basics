p=lambda x,y:x**y

print(p(2,3))

def addlist(l1,l2):
    return list(map(lambda x,y:x+y,l1,l2))

l1=[1,2,3,4]
l2=[5,6,7,8]
print(addlist(l1,l2))
