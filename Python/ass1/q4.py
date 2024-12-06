len=eval(input("Enter length of Rectangle : "));
wid=eval(input("Enter width of Rectangle : "));

def area():
    a=len*wid;
    print(f"Area of rectangle is {a}")
    
def perimeter():
    p=(2*len) +( 2*wid);
    print(f"Perimeter of Rectangle is {p}")
    
area()
perimeter()        