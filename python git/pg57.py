def binary(d):
    if d==0:
     return ''
    else:
     return(str(binary(d//2)+str(d%2)))
n=int(input("Enter a number: "))
print(binary(n))
