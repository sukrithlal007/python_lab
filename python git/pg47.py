def con(s,a):
    h=s;
    for i in range(1,a):
       h=h+" "+s
    return(h) 
s=input("Enter a string")
a=int(input("Enter a number"))
v=con(s,a)
print(v)
