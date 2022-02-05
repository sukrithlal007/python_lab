n=list(input("enter a list").split(","))
m=[]
i=0
print(n)
while i<len(n):
 if n[i] not in m:
     m.append(n[i])
 i=i+1
m.sort()
print(m)
