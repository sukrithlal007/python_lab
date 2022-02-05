s=input("Enter the strings").split()
i=0
c=0
for i in s:
    if len(i)>=2 and i[0]==i[-1]:
        print(i,end="\t")
