n = 5

for i in range(1, n+1):
    for k in range(1, i+1):
        print("*", end="")
    print()
for i in range(n):

    for j in range(n - i-1):
         print('*', end='')
    print()
