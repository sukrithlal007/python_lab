x=input("enter the word")
l=len(x)
if l>2:
    if x[-3:] == 'ing':
         x+='ly'

    else:
         x+='ing'
print(x)       
