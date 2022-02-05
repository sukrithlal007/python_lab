#l=[2,6,7,8,10,300,5]
"""i=0
c1,c2=0,0
while i <len(l):
    if(l[i]%2==0):
        print("even=",l[i])
        c1=c1+1
    else:
        print("odd=",l[i])
        c2=c2+1
    i=i+1
print("even count=",c1,"odd count=",c2)"""

mylist=input("list").split(',')
mylist=list(map(int,mylist))
odd=even=0;
while mylist:
    if mylist.pop(0)%2:
        odd+=1
    else:even+=1
print("even count=",even,"odd count=",odd)     
