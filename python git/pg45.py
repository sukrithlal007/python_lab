def add(a):
    if a[0]=='is':
        return(a)
    else:
        s=['is']+a
        return(s)
 
n=input("Enter the list").split()
v=add(n)
g=' '
print(g.join(v))
