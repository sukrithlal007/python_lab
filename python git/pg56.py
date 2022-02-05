def reverse(b):
    if len(b)==1:
        return b
    else:
        return b[-1]+reverse(b[:-1])

n=(input("Enter a atring:"))
print(reverse(n))
