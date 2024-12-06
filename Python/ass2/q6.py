s=input("Enter String to reverse : ")
a=" "
for i in range(len(s)-1,-1,-1):
    a+=s[i]
print(f"{a}")    
    