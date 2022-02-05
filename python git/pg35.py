a=int(input("enter the first number"))
b=int(input("enter the second number"))
print(a,b)
if a>b:
 s=b;
else:
 s=a;
for i in range(1,s+1):
  if (a%i==0)and(b%i==0):
      gcd=i;
print("GCD",gcd)      
