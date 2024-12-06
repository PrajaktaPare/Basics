dvalue=eval(input("Enter value of degree : "))
dunit=input("Enter unit(1.degree/2.fahrenheit) :")

if dunit==1:
    print(f"{dvalue}d in fahrenheit is {dvalue*(9/5)}")
    
    
else:
    print(f"{dvalue}f in degree is {(dvalue-32)*(5/9)}")    
    