a=list(input("enter a string").split())
print(a)
x=a.index('not')
y=a.index('bad')
c=y+1
print(x,y)
v=a[:x]+['good']+a[c:]
string=' '
print(string.join(v))
