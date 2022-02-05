a=int(input("Enter a number"))
b=int(input("Enter a number"))
def arith(a,b):
    return(a+b,a-b,a*b,a/b)
v=tuple(arith(a,b))
print("add:",v[0])
print("subtract:",v[1])
print("multiplication:",v[2])
print("division:",v[3])
