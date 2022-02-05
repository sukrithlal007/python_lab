n=int(input("Enter the range"))
a,b=0,1
print(a)
for x in range(n):
    a,b=b,a+b
    print(a)
