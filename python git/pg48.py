def check(a,b):
  
        return a==b,a+b==5,abs(a-b)==5
    

a=int(input("Enter a number"))
b=int(input("Enter a number"))
v=tuple(check(a,b))
print("both values=",v[0])
print("sum=5",v[1])
print("difference=5",v[2])
