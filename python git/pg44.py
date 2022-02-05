n=input("Enter the list").split(',')
print(len(n))
m=[]
i=0
while i<len(n):
    a=int(n[i],2) 
    if(a%5==0):
      m.append(a)
    i=i+1
print(m)
