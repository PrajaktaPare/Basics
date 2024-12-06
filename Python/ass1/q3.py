num1=eval(input("Enter 1st number : "))
num2=eval(input("Enter 2nd number : "))
operator=eval(input("""Enter your choice : 
                    1.Addition
                    2.Subtract
                    3.Multiply
                    4.Divide\n"""))

if operator==1:
    print(f"Addition is {num1+num2}");
elif operator==2:
    print(f"Subtraction is {num1-num2}");
elif operator==3:
    print(f"Multiplication is {num1*num2}");
else:
    print(f"Division is {num1/num2}") 
    
               