a=(input("enter the sentance:")).lower()
v=0
for i in range(len(a)):
    if a[i] in("a","e","i","o","u"):
        v=v+1;
print("number of vowels are")
print(v)
