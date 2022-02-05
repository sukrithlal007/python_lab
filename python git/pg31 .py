import math
a=int(input("Enter the  starting range"))
b=int(input("Enter the ending range"))
for i in range(a,b):
    x=math.sqrt(i)
    y=(x-math.floor(x))
    if y==0:
        t=i
        while(t>0):
            if((t%10)%2!=0):
                break;
            t=int(t/10)
        else:
            print("even perfect square:",i)
        
     
