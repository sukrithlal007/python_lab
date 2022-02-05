d={1:2,3:4,4:3,2:1,0:0}
print('original:',d)
d1=sorted(d.items())
print('ascending:',d1)
d2=sorted(d.items(),reverse=True)
print('descending:',d2)
