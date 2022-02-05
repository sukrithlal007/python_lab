lst = []
n = int(input("Enter number of elements : "))
for i in range(n):
            ele =int(input("enter the number"))
            lst.append(ele)
print(lst)
for i in range(len(lst)):
    if lst[i]>100:
        lst[i]='over'
print(lst)

