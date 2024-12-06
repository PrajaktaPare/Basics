numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def checkeven(i):
    return i%2==0
        
filter_list=filter(checkeven,numbers);
print(list(filter_list))        
        