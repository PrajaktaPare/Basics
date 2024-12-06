def m(a,*args):
    mul=a
    for i in args:
        mul*=i
    print(mul)

m(2,3,4)    
m(1,2,3,4,5)